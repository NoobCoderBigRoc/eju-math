# EJU Math 访问统计后台

给静态站点补上「访问量采集 + 存储 + 看板」三段式后台。**零第三方依赖**（Python 标准库 + SQLite + 原生 JS），单文件服务、单文件看板。

## 架构

```
浏览器 ──sendBeacon──> POST /api/collect ──> SQLite(events) ──聚合──> GET /api/stats ──> 看板
   (docs/javascripts/track.js)                (analytics/data/)         (Bearer Token)
```

静态站点（GitHub Pages）只负责发 beacon，数据落在独立部署的统计服务上——静态托管本身无法跑后端，这是必须拆开的原因。

## 快速启动

```bash
cd analytics
export ADMIN_TOKEN=$(openssl rand -hex 24)   # 记下这个值，看板登录要用
python3 server.py                             # 默认 http://127.0.0.1:8787
```

打开 http://127.0.0.1:8787 ，输入刚才的 `ADMIN_TOKEN` 即可进入看板。

## 接口

| 方法 | 路径 | 鉴权 | 说明 |
| --- | --- | --- | --- |
| POST | `/api/collect` | 无（限流 120/min/IP） | 采集一次浏览，body：`{path,title,referrer,screen}` |
| GET | `/api/stats?days=7` | Bearer | 聚合统计（PV/UV/趋势/热门页/来源/设备/浏览器） |
| GET | `/api/realtime` | Bearer | 最近 30 分钟实时数据 |
| GET | `/api/health` | 无 | 健康检查 |
| GET | `/` | 无（登录后在浏览器持有 token） | 管理看板 |

```bash
curl -X POST http://127.0.0.1:8787/api/collect \
  -H 'Content-Type: text/plain' \
  -d '{"path":"/eju-math/","referrer":"https://www.google.com/"}'

curl -H "Authorization: Bearer $ADMIN_TOKEN" \
  'http://127.0.0.1:8787/api/stats?days=7'
```

## 环境变量

| 变量 | 默认 | 说明 |
| --- | --- | --- |
| `PORT` | `8787` | 监听端口 |
| `ADMIN_TOKEN` | 空 | 看板/API 令牌，**生产必填**，留空则看板不可登录 |
| `ANALYTICS_DB` | `./data/analytics.db` | SQLite 路径 |
| `ALLOWED_ORIGINS` | `*` | 采集接口允许来源，逗号分隔 |
| `SALT` | 自动生成到 `data/.salt` | 访客哈希盐，丢失会导致 UV 口径变化 |
| `RETENTION_DAYS` | `400` | 数据保留天数，启动时清理 |

## 隐私与口径

- **不存原始 IP**：`visitor = sha256(SALT|日期|IP|UA)[:32]`，每日换盐 → 日粒度去重，跨天不可关联；
- **不写 Cookie**、不做设备指纹、遵守 `Do Not Track`；
- 过滤爬虫（UA 含 bot/crawler/spider/headless/curl 等）；
- 站内跳转记为「直接访问」，外链只保留域名（去掉 `www.`）；
- 本地预览默认不采集（`track.js` 内置判断）。

## 部署

### 方案 A：自有服务器 / VPS（推荐，数据完全自持）

```bash
cd analytics
export ADMIN_TOKEN=$(openssl rand -hex 24)
docker compose up -d --build       # 数据持久化在 ./data
```

前置一个 Nginx / Caddy 反代并启用 HTTPS（看板令牌明文传输必须走 TLS）。Caddy 一行即可：

```
stats.example.com {
    reverse_proxy 127.0.0.1:8787
}
```

### 方案 B：免费容器平台（Fly.io / Render / Railway）

- 启动命令：`python server.py`，监听 `$PORT`
- 挂载持久卷到 `/data`，设置 `ANALYTICS_DB=/data/analytics.db`
- 环境变量同上；**必须**设置 `ADMIN_TOKEN` 与 `ALLOWED_ORIGINS`

### 方案 C：不想运维 → 用现成分析服务

若只是要看访问量，`Cloudflare Web Analytics` / `Umami Cloud` 一行脚本即可，代价是没有自建看板与原始数据。本项目的优势是数据自持、可二次加工。

## 与站点对接

1. 统计服务上线后拿到地址，如 `https://stats.example.com`；
2. 改 `mkdocs.yml`：

   ```yaml
   extra:
     analytics_endpoint: "https://stats.example.com"
   ```

3. 把 `ALLOWED_ORIGINS` 设为站点域名（如 `https://noobcoderbigroc.github.io`）；
4. `git commit && git push` → GitHub Actions 自动重建，站点开始上报。

## 运维

- 备份：`sqlite3 data/analytics.db ".backup 'backup.db'"`（WAL 模式下不要直接 cp）；
- 体积：每万次 PV 约 1.5 MB，400 天保留期足够小型站点；
- 迁移：直接拷贝 db 文件 + 保持 `SALT` 不变即可延续 UV 口径。
