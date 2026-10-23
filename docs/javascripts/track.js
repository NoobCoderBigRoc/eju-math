/**
 * EJU 数学知识库 · 访问统计埋点
 * ---------------------------------
 * 采集地址来自页面 <meta name="analytics-endpoint">，由 mkdocs.yml 的
 * extra.analytics_endpoint 注入；为空则完全静默（本地开发默认关闭）。
 *
 * 隐私：不写 Cookie、不取设备指纹；服务端只保存日盐哈希后的访客标识。
 */
(function () {
  "use strict";

  var meta = document.querySelector('meta[name="analytics-endpoint"]');
  var ENDPOINT = meta && meta.content ? meta.content.replace(/\/+$/, "") : "";
  if (!ENDPOINT) return;

  // 尊重 Do Not Track
  if (navigator.doNotTrack === "1" || window.doNotTrack === "1") return;

  // 本地预览默认不计入统计；若采集端点本身在本地（联调场景）则放行
  var isLocalPage = /^(localhost|127\.0\.0\.1|0\.0\.0\.0|\[::1\])$/.test(location.hostname);
  var isLocalEndpoint = /^https?:\/\/(localhost|127\.0\.0\.1|0\.0\.0\.0)/.test(ENDPOINT);
  if (isLocalPage && !isLocalEndpoint) return;

  var lastPath = "";

  function send() {
    var path = location.pathname + location.search;
    // Material instant loading 会重复触发，过滤同一路径的连续上报
    if (path === lastPath) return;
    lastPath = path;

    var payload = JSON.stringify({
      path: path,
      title: (document.title || "").slice(0, 120),
      referrer: document.referrer || "",
      screen: window.screen ? window.screen.width + "x" + window.screen.height : "",
    });

    try {
      // text/plain 属于 CORS 简单请求，避免预检往返
      var blob = new Blob([payload], { type: "text/plain;charset=UTF-8" });
      if (navigator.sendBeacon && navigator.sendBeacon(ENDPOINT + "/api/collect", blob)) return;
    } catch (e) {
      /* 降级到 fetch */
    }

    try {
      fetch(ENDPOINT + "/api/collect", {
        method: "POST",
        body: payload,
        headers: { "Content-Type": "text/plain;charset=UTF-8" },
        mode: "cors",
        keepalive: true,
        credentials: "omit",
      }).catch(function () {});
    } catch (e) {
      /* 统计失败不影响页面 */
    }
  }

  // Material 的 document$ 在首次加载与每次站内跳转后都会触发
  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(send);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", send);
  } else {
    send();
  }
})();
