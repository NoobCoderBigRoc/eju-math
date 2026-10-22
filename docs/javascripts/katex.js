// KaTeX 渲染：兼容 Material 的 instant loading（每次导航后重新渲染）
(function () {
  function render() {
    if (typeof renderMathInElement !== "function") return;
    renderMathInElement(document.body, {
      delimiters: [
        { left: "$$", right: "$$", display: true },
        { left: "$", right: "$", display: false },
        { left: "\\(", right: "\\)", display: false },
        { left: "\\[", right: "\\]", display: true },
      ],
      throwOnError: false,
      ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code"],
    });
  }

  // 若主 CDN 失败（国内网络常见），回退到 unpkg
  function ensureKatex(cb) {
    if (typeof window.katex !== "undefined" && typeof window.renderMathInElement === "function") {
      cb();
      return;
    }
    var urls = [
      "https://unpkg.com/katex@0.16.11/dist/katex.min.js",
      "https://unpkg.com/katex@0.16.11/dist/contrib/auto-render.min.js",
    ];
    var pending = urls.length;
    urls.forEach(function (src) {
      var s = document.createElement("script");
      s.src = src;
      s.onload = s.onerror = function () {
        if (--pending === 0) cb();
      };
      document.head.appendChild(s);
    });
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(function () {
      ensureKatex(render);
    });
  } else {
    document.addEventListener("DOMContentLoaded", function () {
      ensureKatex(render);
    });
  }
})();
