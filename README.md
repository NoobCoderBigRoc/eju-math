# EJU 数学知识库

参照 [OI Wiki](https://oi-wiki.org/) 组织方式的 EJU（日本留学试验）数学知识系统，纯静态站点。

## 技术栈

- **框架**：MkDocs Material 9.x（与 OI Wiki 同源方案）
- **数学公式**：KaTeX（经 `pymdownx.arithmatex` 桥接）
- **图表**：Mermaid
- **构建**：纯静态输出，无服务端依赖

## 本地开发

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve          # http://127.0.0.1:8000
mkdocs build          # 产物输出到 site/
```

## 上线方式（三选一）

| 方案 | 命令/步骤 | 适合场景 |
| --- | --- | --- |
| GitHub Pages（推荐） | 推送到 main，`.github/workflows/deploy.yml` 自动部署 | 免费托管 + 自动 CI |
| Docker + 任意服务器 | `docker build -t eju-math . && docker run -p 80:80 eju-math` | 自有服务器/内网 |
| Vercel / Netlify | 构建命令 `mkdocs build`，输出目录 `site` | 免运维、全球 CDN |

## 目录结构

```
docs/
├── index.md            # 首页 + 知识图谱
├── cheatsheet.md       # 跨章节公式速查
├── exam/               # 考试总览、备考策略
├── course1/            # 文科数学 7 章
├── course2/            # 理科数学 8 章
├── javascripts/katex.js  # KaTeX 渲染 + CDN 回退
└── stylesheets/extra.css
```

## 内容页面模板

每个知识点页面遵循：**考纲要求 → 核心公式 → 典型例题（可折叠）→ 易错点**。新增章节时按此模板写入 `docs/courseX/*.md` 并更新 `mkdocs.yml` 的 `nav`。
