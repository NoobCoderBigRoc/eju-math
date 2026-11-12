# EJU 数学知识库

参照 [OI Wiki](https://oi-wiki.org/) 组织方式的 EJU（日本留学试验）数学知识系统，纯静态站点。

**在线访问**：https://noobcoderbigroc.github.io/eju-math/

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
├── course1/            # Course 1（项目 1–7，每项目含简介/要点总结/细目页）
├── course2/            # Course 2（项目 8–20，共 13 个项目，同上结构）
├── overrides/          # 主题覆盖（注入统计端点）
├── javascripts/katex.js  # KaTeX 渲染 + CDN 回退
├── javascripts/track.js  # 访问统计埋点
└── stylesheets/extra.css

analytics/              # 访问统计后台（独立部署）
├── server.py           # 采集 + 聚合 API（Python 标准库 + SQLite）
├── static/index.html   # 管理看板
├── Dockerfile
└── docker-compose.yml
```

## 访问统计

站点是纯静态的，统计后台需独立部署（详见 [analytics/README.md](analytics/README.md)）。对接只需两步：

```bash
cd analytics && ADMIN_TOKEN=$(openssl rand -hex 24) python3 server.py   # 本地看板 8787
```

```yaml
# mkdocs.yml
extra:
  analytics_endpoint: "https://stats.example.com"   # 留空则完全关闭埋点
```

## 内容页面模板

每个项目由「○○简介」（含与考纲的对应表）、「○○要点总结」（考前确认页）与考纲细目叶子页组成；叶子页遵循：**定义・公式 → 例题（题面直接展示，思路・解答折叠）→ 易错点 → 相关条目**，说明文字用中文、知识点本体保留日语（规范见 `templates/chapter-template.md`）。新增页面时按模板写入并更新 `mkdocs.yml` 的 `nav`。
