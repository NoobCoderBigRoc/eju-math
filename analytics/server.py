#!/usr/bin/env python3
"""
EJU Math 访问统计服务
====================
零第三方依赖（Python 标准库），单文件实现：

  POST /api/collect      采集一次页面浏览（sendBeacon 目标）
  GET  /api/stats        聚合统计（需 Bearer Token）
  GET  /api/realtime     最近 30 分钟实时数据（需 Bearer Token）
  GET  /api/health       健康检查
  GET  /                 管理看板（static/index.html）

环境变量：
  PORT                 监听端口，默认 8787
  ANALYTICS_DB         SQLite 路径，默认 ./data/analytics.db
  ADMIN_TOKEN          看板令牌，必填（生产环境）
  ALLOWED_ORIGINS      采集接口允许的来源，逗号分隔，默认 *；配置后将按 Origin 强制校验
  TRUSTED_PROXIES      可信反向代理的 IP（逗号分隔，默认 127.0.0.1,::1）；仅来自这些地址时才信任 X-Forwarded-For 与国家头
  SALT                 访客哈希盐，留空则自动生成到 data/.salt
  RETENTION_DAYS       数据保留天数，默认 400

隐私设计：不存储原始 IP，仅存 日盐+IP+UA 的 SHA-256 前 16 字节；
每日本地日期参与哈希，跨天无法关联同一访客。
"""

import hashlib
import hmac
import json
import mimetypes
import os
import re
import secrets
import sqlite3
import threading
import time
from contextlib import contextmanager
from datetime import date, datetime, time as dtime, timedelta
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

PORT = int(os.environ.get("PORT", "8787"))
DB_PATH = os.environ.get("ANALYTICS_DB", os.path.join(BASE_DIR, "data", "analytics.db"))
ADMIN_TOKEN = os.environ.get("ADMIN_TOKEN", "")
ALLOWED_ORIGINS = os.environ.get("ALLOWED_ORIGINS", "*")
TRUSTED_PROXIES = [p.strip() for p in os.environ.get("TRUSTED_PROXIES", "127.0.0.1,::1").split(",") if p.strip()]
RETENTION_DAYS = int(os.environ.get("RETENTION_DAYS", "400"))
MAX_BODY = 8 * 1024
RATE_LIMIT = 120          # 每 IP 每分钟最多采集次数
RATE_WINDOW = 60

# ---------------------------------------------------------------- 基础设施

def _load_salt() -> str:
    env = os.environ.get("SALT")
    if env:
        return env
    path = os.path.join(os.path.dirname(DB_PATH), ".salt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as fh:
            return fh.read().strip()
    value = secrets.token_hex(32)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(value)
    os.chmod(path, 0o600)
    return value


SALT = _load_salt()

SCHEMA = """
CREATE TABLE IF NOT EXISTS events (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    ts       INTEGER NOT NULL,          -- unix 秒
    path     TEXT    NOT NULL,
    title    TEXT,
    ref_host TEXT,                      -- 来源域名，空 = 直接访问
    device   TEXT,                      -- desktop / mobile / tablet
    browser  TEXT,
    os       TEXT,
    country  TEXT,
    visitor  TEXT    NOT NULL,          -- 日盐哈希，日粒度去重
    screen   TEXT
);
CREATE INDEX IF NOT EXISTS idx_events_ts   ON events(ts);
CREATE INDEX IF NOT EXISTS idx_events_path ON events(path);
CREATE INDEX IF NOT EXISTS idx_events_vis  ON events(visitor);
"""

_db_lock = threading.Lock()


@contextmanager
def db_connect():
    conn = sqlite3.connect(DB_PATH, timeout=15)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db() -> None:
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with db_connect() as conn:
        conn.executescript(SCHEMA)
        _cleanup_old(conn)


def _cleanup_old(conn) -> None:
    if RETENTION_DAYS > 0:
        cutoff = int(time.time()) - RETENTION_DAYS * 86400
        conn.execute("DELETE FROM events WHERE ts < ?", (cutoff,))


_last_cleanup = time.time()


def maybe_cleanup() -> None:
    """保留期清理每天最多执行一次（不再只依赖进程启动）。"""
    global _last_cleanup
    now = time.time()
    if now - _last_cleanup < 86400:
        return
    _last_cleanup = now
    with _db_lock, db_connect() as conn:
        _cleanup_old(conn)


# ---------------------------------------------------------------- 解析逻辑

BOT_RE = re.compile(
    r"(bot|crawler|spider|scrapy|headless|phantom|slurp|bingpreview|"
    r"curl|wget|python-requests|go-http-client|facebookexternalhit|semrush|ahrefs)",
    re.I,
)


def is_bot(ua: str) -> bool:
    return bool(BOT_RE.search(ua or ""))


def parse_ua(ua: str):
    ua = ua or ""
    if re.search(r"iPad|Tablet|PlayBook|Silk", ua, re.I):
        device = "tablet"
    elif re.search(r"Mobi|Android|iPhone|iPod", ua, re.I):
        device = "mobile"
    else:
        device = "desktop"

    if "Edg/" in ua:
        browser = "Edge"
    elif "OPR/" in ua or "Opera" in ua:
        browser = "Opera"
    elif "Firefox" in ua:
        browser = "Firefox"
    elif "Chrome" in ua or "CriOS" in ua:
        browser = "Chrome"
    elif "Safari" in ua:
        browser = "Safari"
    else:
        browser = "Other"

    if "Windows" in ua:
        os_name = "Windows"
    elif "Android" in ua:
        os_name = "Android"
    elif re.search(r"iPhone|iPad|iOS", ua):
        os_name = "iOS"
    elif "Mac OS X" in ua:
        os_name = "macOS"
    elif "Linux" in ua:
        os_name = "Linux"
    else:
        os_name = "Other"
    return device, browser, os_name


def visitor_id(ip: str, ua: str, day: str) -> str:
    raw = f"{SALT}|{day}|{ip}|{ua}".encode("utf-8", "ignore")
    return hashlib.sha256(raw).hexdigest()[:32]


def from_trusted_proxy(handler) -> bool:
    return handler.client_address[0] in TRUSTED_PROXIES


def client_ip(handler) -> str:
    # X-Forwarded-For 只能来自可信反向代理，否则任何人都能伪造 IP 绕过限流与 UV 统计
    if from_trusted_proxy(handler):
        fwd = handler.headers.get("X-Forwarded-For", "")
        if fwd:
            return fwd.split(",")[0].strip()
    return handler.client_address[0]


def ref_host(referrer: str, self_host: str) -> str:
    if not referrer:
        return ""
    try:
        host = urlparse(referrer).netloc.lower()
    except ValueError:
        return ""
    if not host or host == self_host.lower():
        return ""          # 站内跳转记为直接访问
    return host[4:] if host.startswith("www.") else host


# ---------------------------------------------------------------- 限流

_rate: dict[str, list] = {}
_rate_lock = threading.Lock()


def rate_ok(ip: str) -> bool:
    now = time.time()
    with _rate_lock:
        if len(_rate) > 4096:  # 顺手清掉已过期的窗口，防止字典无限膨胀
            for stale in [k for k, w in _rate.items() if now - w[0] > RATE_WINDOW]:
                del _rate[stale]
        window = _rate.get(ip)
        if not window or now - window[0] > RATE_WINDOW:
            _rate[ip] = [now, 1]
            return True
        if window[1] >= RATE_LIMIT:
            return False
        window[1] += 1
        return True


_auth_fails: dict[str, list] = {}


def _auth_attempt_ok(ip: str) -> bool:
    """记录一次鉴权失败；10 分钟内失败超过 30 次则拒绝（防 Token 暴力破解）。"""
    now = time.time()
    with _rate_lock:
        fails = [t for t in _auth_fails.get(ip, []) if now - t < 600]
        fails.append(now)
        _auth_fails[ip] = fails
        return len(fails) <= 30


# ---------------------------------------------------------------- 聚合

def _day_start(d: date) -> int:
    return int(datetime.combine(d, dtime.min).timestamp())


def stats(days: int) -> dict:
    days = max(1, min(days, 365))
    today = date.today()
    start_day = today - timedelta(days=days - 1)
    start_ts = _day_start(start_day)
    today_ts = _day_start(today)

    with db_connect() as conn:
        totals = conn.execute(
            "SELECT COUNT(*) pv, COUNT(DISTINCT visitor) uv FROM events WHERE ts >= ?",
            (start_ts,),
        ).fetchone()
        today_row = conn.execute(
            "SELECT COUNT(*) pv, COUNT(DISTINCT visitor) uv FROM events WHERE ts >= ?",
            (today_ts,),
        ).fetchone()

        pv_rows = conn.execute(
            "SELECT date(ts,'unixepoch','localtime') d, COUNT(*) c "
            "FROM events WHERE ts >= ? GROUP BY d", (start_ts,),
        ).fetchall()
        uv_rows = conn.execute(
            "SELECT date(ts,'unixepoch','localtime') d, COUNT(DISTINCT visitor) c "
            "FROM events WHERE ts >= ? GROUP BY d", (start_ts,),
        ).fetchall()
        pv_map = {r["d"]: r["c"] for r in pv_rows}
        uv_map = {r["d"]: r["c"] for r in uv_rows}

        series = []
        for i in range(days):
            d = (start_day + timedelta(days=i)).isoformat()
            series.append({"date": d, "pv": pv_map.get(d, 0), "uv": uv_map.get(d, 0)})

        top_pages = [dict(r) for r in conn.execute(
            "SELECT path, COUNT(*) pv, COUNT(DISTINCT visitor) uv FROM events "
            "WHERE ts >= ? GROUP BY path ORDER BY pv DESC LIMIT 15", (start_ts,),
        )]

        referrers = [dict(r) for r in conn.execute(
            "SELECT CASE WHEN ref_host='' OR ref_host IS NULL THEN '直接访问' ELSE ref_host END src, "
            "COUNT(*) pv FROM events WHERE ts >= ? GROUP BY src ORDER BY pv DESC LIMIT 10",
            (start_ts,),
        )]

        devices = [dict(r) for r in conn.execute(
            "SELECT device, COUNT(*) pv FROM events WHERE ts >= ? GROUP BY device ORDER BY pv DESC",
            (start_ts,),
        )]

        browsers = [dict(r) for r in conn.execute(
            "SELECT browser, COUNT(*) pv FROM events WHERE ts >= ? GROUP BY browser ORDER BY pv DESC LIMIT 6",
            (start_ts,),
        )]

    return {
        "range_days": days,
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "totals": {
            "pv": totals["pv"], "uv": totals["uv"],
            "today_pv": today_row["pv"], "today_uv": today_row["uv"],
        },
        "series": series,
        "top_pages": top_pages,
        "referrers": referrers,
        "devices": devices,
        "browsers": browsers,
    }


def realtime() -> dict:
    since = int(time.time()) - 1800
    with db_connect() as conn:
        row = conn.execute(
            "SELECT COUNT(*) pv, COUNT(DISTINCT visitor) uv FROM events WHERE ts >= ?",
            (since,),
        ).fetchone()
        pages = [dict(r) for r in conn.execute(
            "SELECT path, COUNT(*) pv FROM events WHERE ts >= ? "
            "GROUP BY path ORDER BY pv DESC LIMIT 5", (since,),
        )]
    return {"last_30min_pv": row["pv"], "last_30min_uv": row["uv"], "pages": pages}


# ---------------------------------------------------------------- HTTP

class Handler(BaseHTTPRequestHandler):
    server_version = "EJUAnalytics/1.0"
    timeout = 10  # 连接级超时，防止慢速请求（slowloris）长期占用线程

    # --- 工具
    def _cors(self):
        origin = self.headers.get("Origin", "")
        if ALLOWED_ORIGINS == "*":
            allow = "*"
        else:
            allowed = [o.strip() for o in ALLOWED_ORIGINS.split(",") if o.strip()]
            allow = origin if origin in allowed else (allowed[0] if allowed else "null")
        self.send_header("Access-Control-Allow-Origin", allow)
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.send_header("Access-Control-Max-Age", "86400")
        if allow != "*":
            self.send_header("Vary", "Origin")

    def _json(self, obj, code=200):
        payload = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self._cors()
        self.end_headers()
        self.wfile.write(payload)

    def _auth_ok(self) -> bool:
        if not ADMIN_TOKEN:
            return False
        header = self.headers.get("Authorization", "")
        token = header[7:].strip() if header.lower().startswith("bearer ") else ""
        return bool(token) and hmac.compare_digest(token, ADMIN_TOKEN)

    def log_message(self, fmt, *args):  # 采集接口量大，不逐条打日志
        if urlparse(self.path).path.rstrip("/") == "/api/collect":
            return
        super().log_message(fmt, *args)

    def _origin_allowed(self) -> bool:
        # 配置了来源白名单时按 Origin 强制校验（CORS 响应头本身不是访问控制）
        if ALLOWED_ORIGINS == "*":
            return True
        origin = self.headers.get("Origin", "")
        allowed = [o.strip() for o in ALLOWED_ORIGINS.split(",") if o.strip()]
        return bool(origin) and origin in allowed

    # --- 路由
    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.send_header("Content-Length", "0")
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/") or "/"

        if path == "/api/health":
            return self._json({"ok": True, "time": int(time.time())})

        if path in ("/api/stats", "/api/realtime"):
            if not self._auth_ok():
                if not _auth_attempt_ok(client_ip(self)):
                    return self._json({"error": "too many attempts"}, 429)
                return self._json({"error": "unauthorized"}, 401)
            if path == "/api/stats":
                qs = parse_qs(parsed.query)
                try:
                    days = int(qs.get("days", ["7"])[0])
                except ValueError:
                    days = 7
                return self._json(stats(days))
            return self._json(realtime())

        # 静态看板
        if path == "/" or path == "/index.html":
            return self._serve_file("index.html", "text/html; charset=utf-8")
        if path.startswith("/static/"):
            name = os.path.basename(path)
            ctype = mimetypes.guess_type(name)[0] or "application/octet-stream"
            if ctype.startswith("text/") or ctype == "application/javascript":
                ctype += "; charset=utf-8"
            return self._serve_file(name, ctype)

        return self._json({"error": "not found"}, 404)

    def _serve_file(self, name: str, ctype: str):
        full = os.path.join(STATIC_DIR, name)
        if not os.path.isfile(full):
            return self._json({"error": "not found"}, 404)
        with open(full, "rb") as fh:
            body = fh.read()
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-cache")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        if ctype.startswith("text/html"):
            self.send_header("Content-Security-Policy",
                             "default-src 'self'; script-src 'self' 'unsafe-inline'; "
                             "style-src 'self' 'unsafe-inline'; img-src 'self' data:")
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        path = urlparse(self.path).path.rstrip("/")
        if path != "/api/collect":
            return self._json({"error": "not found"}, 404)

        if not self._origin_allowed():
            return self._json({"error": "forbidden origin"}, 403)

        ip = client_ip(self)
        if not rate_ok(ip):
            return self._json({"error": "rate limited"}, 429)

        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            length = 0
        if length <= 0 or length > MAX_BODY:
            return self._json({"error": "bad body"}, 400)

        try:
            data = json.loads(self.rfile.read(length).decode("utf-8", "ignore"))
        except (ValueError, UnicodeDecodeError):
            return self._json({"error": "invalid json"}, 400)
        if not isinstance(data, dict):
            return self._json({"error": "invalid payload"}, 400)

        ua = self.headers.get("User-Agent", "")
        if is_bot(ua):
            return self._json({"ok": True, "skipped": "bot"}, 202)

        page_path = str(data.get("path", "/"))[:200]
        if not page_path.startswith("/"):
            page_path = "/" + page_path
        title = str(data.get("title", ""))[:120]
        referrer = str(data.get("referrer", ""))[:300]
        screen = str(data.get("screen", ""))[:24]
        country = ""
        if from_trusted_proxy(self):  # 国家头同样只能来自可信代理，否则可任意伪造
            country = (self.headers.get("CF-IPCountry") or self.headers.get("X-Country") or "")[:4]

        self_host = urlparse(f"//{self.headers.get('Host', '')}").netloc
        device, browser, os_name = parse_ua(ua)
        day = date.today().isoformat()
        vid = visitor_id(ip, ua, day)

        maybe_cleanup()
        with _db_lock, db_connect() as conn:
            conn.execute(
                "INSERT INTO events (ts, path, title, ref_host, device, browser, os, country, visitor, screen) "
                "VALUES (?,?,?,?,?,?,?,?,?,?)",
                (int(time.time()), page_path, title, ref_host(referrer, self_host),
                 device, browser, os_name, country, vid, screen),
            )
        return self._json({"ok": True}, 202)


def main():
    if not ADMIN_TOKEN:
        print("⚠️  未设置 ADMIN_TOKEN，看板登录将不可用。请设置后重启。")
    init_db()
    server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"📊 EJU Analytics 运行于 http://127.0.0.1:{PORT}   DB={DB_PATH}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n已停止")


if __name__ == "__main__":
    main()
