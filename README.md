# AI & Work Research

Hujialin · Personal Academic Research Workspace

研究 AI 如何改变个体、工作方式、人机协作与组织。

原生 HTML / CSS / JavaScript 静态站点，无构建步骤、无数据库、无 API Key。现已收录 9 篇论文，其中 2 篇已精读，并关联 2 份导图原件和研究笔记。所有统计从 data 文件读取。

## 项目维护

目标仓库：`RenbenAI-Lab/hujialin-ai-work-research`。原生静态站点，源码与研究索引一同维护。浏览器草稿需导出后提交仓库才能同步。

## 本地运行

在本 README 所在目录打开终端：

```powershell
python -m http.server 8000 --bind 127.0.0.1
```

打开 http://127.0.0.1:8000 。不要双击 HTML 使用 `file://`，浏览器可能阻止 fetch 读取数据。按 Ctrl+C 停止服务。Python 仅用于预览和可选备份脚本，不是站点依赖。

## 已实现

- 响应式首页、六个模块、真实统计与无数据提示。
- 论文搜索、主题与状态筛选、字段编辑、阅读状态更新、CSV 导出。
- Zotero CSV 和常见 BibTeX 花括号条目导入，按 DOI / 标题去重。
- 四个一级主题以及新增、编辑、JSON 导出。
- 知识地图索引、图片预览、Markdown 安全文本预览、XMind 附件链接。
- Markdown 笔记导入、笔记编辑和统一论文分析模板。
- 每周任务计划、截止日期、状态、研究问题进展、完成比例、最近更新。
- GPT 讨论链接、日期、结论、论文关联、整理为笔记的标记。
- 浏览器本地草稿、单模块文件导出、全量备份导出、本地应用脚本。

## 保存方式：必须阅读

网页不能直接写回 GitHub。所有表单和状态修改只存入当前浏览器当前站点的 localStorage，页面会显示草稿提示；关闭浏览器通常仍保留，但清理缓存或更换设备不会同步。草稿会优先于仓库文件显示；拉取新数据后，先导出需保留的草稿，再“放弃草稿”并刷新，以显示最新文件。

单模块保存：点击对应模块的导出按钮，将下载的 `papers.csv` 或 `*.json` 放入本地仓库 `data/` 的对应路径，审查差异、提交、正常推送后 Pages 才会更新。请先备份旧文件。

全量保存：点击草稿横幅的“导出全部数据”，得到 `research-data.json`。在仓库根目录运行：

```powershell
python scripts/apply-backup.py "下载文件的绝对路径/research-data.json"
```

默认只校验，不改文件。核对记录数量后执行：

```powershell
python scripts/apply-backup.py "下载文件的绝对路径/research-data.json" --write
```

脚本先把当前 `data/` 复制到 `backups/时间戳/`，再拆分导出数据写入 CSV / JSON。`backups/` 被 Git 忽略，不应上传到 Pages。脚本不会移动或修改 Zotero、Obsidian 或 XMind 的原始文件。提交前用 `git diff` 审查，勿使用强制推送。

## 文件结构

```text
index.html
assets/css/style.css
assets/js/app.js
assets/images/                 # 可放图片
data/
  papers.csv
  themes.json
  tasks.json
  mindmaps.json
  notes.json
  discussions.json
01_Literature/
02_Research_Themes/
03_Research_Notes/
04_Knowledge_Maps/
05_Research_Progress/
06_GPT_Discussions/
templates/
  paper-template.md
  mindmap-template.md
  research-question-template.md
  papers-import.csv
scripts/apply-backup.py
.nojekyll
```

各研究目录包含用途说明，可按主题继续建子目录。空的 assets/images 目录在 Git 中可能不保留，上传图片时自动建立即可。

<a id="import"></a>
## 添加论文与 Zotero 导入

1. Zotero 中选择文献，导出 CSV 或 BibTeX（UTF-8）。无需导出 PDF。
2. 打开 Literature Library → 导入 CSV / BibTeX。
3. 核对标题、作者、年份、期刊、DOI、链接。导入时缺失标题会拒绝整个导入；重复 DOI 或标题跳过，不覆盖已有评价。
4. 给文献设置主题、阅读状态、重要程度和个人评价，然后导出 `papers.csv` 替换 `data/papers.csv`。

本项目 CSV 列名：

```csv
id,title,authors,year,journal,doi,url,theme,status,importance,rating,updatedAt
```

Zotero 的 `Title`、`Author`、`Publication Year` / `Date`、`Publication Title`、`DOI`、`Url`、`Key` 自动映射。含逗号或换行的值需双引号包裹，内部双引号写成两个。CSV 模板仅有表头，没有虚构论文。

主题值使用 `themes.json` 的 ID：`individual`、`tasks-work`、`human-ai`、`organization`；可以在页面新增主题，再导出 `themes.json`。阅读状态仅使用 `Not Started`、`Reading`、`In Progress`、`Completed`，其中 Completed 计入精读数。

BibTeX 支持常见 `@article{...}` / `@inproceedings{...}`、嵌套花括号和引号值；不展开 `@string` 宏、字符串拼接或全部 LaTeX 转义。复杂条目建议改用 Zotero CSV。附件及 PDF 不会自动复制。切问等来源可先转为统一 CSV，或手动添加论文。

## Obsidian 笔记

- 复制想发布的 `.md` 到 `03_Research_Notes/`，原库保留不动。
- 在 Research Notes 中添加记录，`file` 填 `03_Research_Notes/文件名.md`，导出 `notes.json`。
- 也可“导入 Markdown 笔记”，内容存入浏览器草稿，导出后保存在 `notes.json` 的 `content` 字段。
- 新笔记从 `templates/paper-template.md` 开始，已包含要求的十一部分。
- Markdown 显示为安全纯文本，不执行 HTML；Obsidian `[[双向链接]]`、插件和嵌入语法暂不解析。图片建议复制到仓库并用相对路径维护。

## XMind 与知识地图

复制 `.xmind` 文件到 `04_Knowledge_Maps/`，新增地图记录：地图名称、主题、相关论文 ID、研究问题和文件路径。保存 `mindmaps.json`。

XMind 原件保留并通过“打开 / 下载附件”访问；要预览，另导出 PNG / JPG 放入仓库，再建立图片地图记录，或者使用 Markdown 索引同时链接图片与原件。不会在线解析 `.xmind`。Markdown 可读取 `.md` 路径并以安全文本预览。外部 Markdown 链接能否预览取决于对方服务器 CORS，仓库内路径最可靠。

统一使用相对于站点根目录的路径，不加 `/` 前缀，例如 `04_Knowledge_Maps/map.png`，这样适配 GitHub Pages 子路径。

## 进度与 GPT 讨论

Research Progress 新增任务，设置任务类型（阅读任务 / 研究问题 / 其他）、主题、计划周、截止日期和进展说明。状态为 Completed 的项目即已完成任务，其余计入待办。导出 `tasks.json`。

GPT Discussions 新增对话标题、日期、主题、核心结论、关联论文 ID 和原始对话链接，再导出 `discussions.json`。“已整理”仅是人工标记，不自动生成笔记。对话链接归档不抓取原始聊天内容。

## JSON 数据约定与统一接口

每个 JSON 文件是记录数组；每条记录有唯一 `id`，更新时间使用 ISO 8601 `updatedAt`。所有文本均支持中文。

- themes：`id, name, description, updatedAt`
- tasks：`id, title, theme, status, kind, week, due, progress, updatedAt`
- mindmaps：`id, title, theme, papers, question, file, updatedAt`
- notes：`id, title, theme, papers, file, content, updatedAt`
- discussions：`id, title, date, theme, conclusion, papers, url, formalized, updatedAt`

`papers` 关联字段为逗号分隔的论文 ID，支持点击论文跳转并生成关系网络；`formalized` 为 `yes` / `no`。统一导入边界为这些静态文件，任何后续转换器都可输出相同格式，无需 API Key。

最近更新基于记录的 `updatedAt`，不是不可变的历史审计日志；同一记录多次修改只展示最新时间。手动编辑文件时请同时更新该字段。

## GitHub Pages 部署

1. 获取并检查 `RenbenAI-Lab/hujialin-ai-work-research` 的有效本地克隆。不要把本交付直接覆盖进已有目录；逐文件比较并合并，尤其保留原有 `data/`、README 与工作流。
2. 合并后确保 `index.html`、`assets/`、`data/` 和 `.nojekyll` 位于仓库根目录。无需 npm install 或构建。
3. 审查 `git diff`，提交并正常推送到你选定的分支（不使用 force）。
4. GitHub 仓库 Settings → Pages → Deploy from a branch → 选择实际分支和 `/ (root)` → Save。需有对应仓库设置权限，本项目不会自行修改权限。
5. 等待部署完成。预计项目地址为 `https://renbenai-lab.github.io/hujialin-ai-work-research/`，以 GitHub Pages 实际返回地址为准。

所有路由使用 `#`，刷新和深链接不需要服务器重写；资源路径相对，无第三方 CDN 和外部字体。Pages 是静态发布，不提供登录访问控制；发布前自行选择允许公开的研究资料。仓库是否支持 Pages 取决于账户和仓库的现有配置。

## 尚未实现

GitHub 写回与跨设备同步、真实用户登录、Zotero API 同步、PDF 全文解析、完整 BibTeX / LaTeX 解析、XMind 在线编辑、Obsidian 插件与双链解析、记录删除、完整版本历史，以及 ChatGPT / 切问自动抓取。现阶段通过本地文件维护和 Git 历史管理这些数据。

## 验证

已进行 JavaScript 语法检查、CSV / Zotero 映射 / BibTeX 与重复数据处理检查、HTTP 数据文件读取、实际浏览器首页与论文编辑检查。测试记录不包含于交付数据。无远端仓库访问权限，因此未验证线上 Pages 部署。已检查 390px 手机视口布局；移动布局使用 720px / 1100px 媒体查询，仍建议在目标手机上验收。

## 2026-11-25 研究资料更新

现有 9 篇论文，其中 2 篇 Completed；导入 2 份 Obsidian Simple Mind Map 原始 Markdown，建立 2 条地图与 2 条笔记索引（指向同一原件副本）。原库文件未修改。论文列表与地图支持双向跳转；Markdown 预览显示可读 textdata，不解析插件压缩布局。未找到引用 SVG，后续可补 PNG/SVG 图形预览。

## 认知地图与进度看板

Knowledge Maps 使用深色关系网络：主题、论文、导图、笔记、讨论以颜色区分。连线只表示已维护的主题归属和论文关联，并非引用或语义相似度。支持节点拖动、背景平移、按钮/滚轮缩放、搜索、主题筛选、节点详情和键盘 Enter 访问。位置调整为临时视图，不写入数据。原始导图文件列表保留在下方。

Research Progress 提供论文阅读与研究任务两个看板，四列对应 Not Started / Reading / In Progress / Completed。支持拖放卡片、状态下拉框、标题/作者/主题搜索、主题筛选、列内新增和编辑；手机可横向滑动查看列，使用下拉框改状态。状态更改仍是浏览器草稿，需要导出论文 CSV 或任务 JSON 后更新 data 文件。

已验证实际拖动论文卡片及数量更新、节点键盘访问与详情；测试草稿已清理。网络当前包含 17 个真实节点和 17 条关联，包含无论文的 Organization 主题节点。
