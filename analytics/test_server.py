#!/usr/bin/env python3
"""EJU Analytics 关键逻辑单测（标准库 unittest，无需第三方依赖）。

运行：cd analytics && ADMIN_TOKEN=<redacted> python3 -m unittest test_server -v
覆盖：可信代理判定 / 客户端 IP / Origin 校验 / 限流表清理 / 鉴权失败限速 / 访客哈希。
"""

import os
import time
import unittest

os.environ.setdefault("ADMIN_TOKEN", "test-token")
os.environ.setdefault("ALLOWED_ORIGINS", "https://noobcoderbigroc.github.io")

import server  # noqa: E402


class FakeHandler:
    def __init__(self, peer="203.0.113.9", headers=None):
        self.client_address = (peer, 12345)
        self.headers = headers or {}

    def header(self, name, default=""):
        return self.headers.get(name, default)


class ClientIpTest(unittest.TestCase):
    def test_untrusted_peer_xff_ignored(self):
        h = FakeHandler(peer="203.0.113.9", headers={"X-Forwarded-For": "1.2.3.4"})
        self.assertEqual(server.client_ip(h), "203.0.113.9")

    def test_trusted_proxy_xff_used(self):
        h = FakeHandler(peer="127.0.0.1", headers={"X-Forwarded-For": "1.2.3.4, 10.0.0.1"})
        self.assertEqual(server.client_ip(h), "1.2.3.4")

    def test_trusted_proxy_without_xff(self):
        h = FakeHandler(peer="127.0.0.1")
        self.assertEqual(server.client_ip(h), "127.0.0.1")


class OriginTest(unittest.TestCase):
    def _handler(self, origin=None):
        class H(server.Handler):
            def __init__(self):
                self.headers = {"Origin": origin} if origin else {}
        return H()

    def test_allowed_origin(self):
        self.assertTrue(self._handler("https://noobcoderbigroc.github.io")._origin_allowed())

    def test_foreign_origin_rejected(self):
        self.assertFalse(self._handler("https://evil.example.com")._origin_allowed())

    def test_missing_origin_rejected(self):
        self.assertFalse(self._handler(None)._origin_allowed())


class RateLimitTest(unittest.TestCase):
    def setUp(self):
        server._rate.clear()

    def test_limit_enforced(self):
        ip = "198.51.100.7"
        for _ in range(server.RATE_LIMIT):
            self.assertTrue(server.rate_ok(ip))
        self.assertFalse(server.rate_ok(ip))

    def test_stale_entries_pruned(self):
        old = time.time() - server.RATE_WINDOW - 10
        for i in range(5000):
            server._rate[f"10.0.{i // 256}.{i % 256}"] = [old, 1]
        self.assertTrue(server.rate_ok("192.0.2.1"))
        self.assertLess(len(server._rate), 5000)


class AuthRateTest(unittest.TestCase):
    def setUp(self):
        server._auth_fails.clear()

    def test_lockout_after_30_failures(self):
        ip = "198.51.100.99"
        for _ in range(30):
            self.assertTrue(server._auth_attempt_ok(ip))
        self.assertFalse(server._auth_attempt_ok(ip))


class VisitorIdTest(unittest.TestCase):
    def test_stable_within_day_and_changes_across_days(self):
        a = server.visitor_id("1.2.3.4", "UA", "2026-11-11")
        b = server.visitor_id("1.2.3.4", "UA", "2026-11-11")
        c = server.visitor_id("1.2.3.4", "UA", "2026-11-12")
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)


if __name__ == "__main__":
    unittest.main()
