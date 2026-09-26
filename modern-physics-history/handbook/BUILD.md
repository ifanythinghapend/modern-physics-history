# 维护者的构建说明

首次阅读、上传和发布无需构建。仓库已带 `index.html` 与 PDF；这里只说明修改内容后怎样更新。

## 正文来源

`docs/` 中的分章 Markdown 是编辑源，`data/book.json` 保存目录顺序与版本文字。推导单独成文件，通过章节中的包含标记回到原位置。

文献以附录 D 为准，时间轴以附录 A 为准，核心问题出处对应以附录 E 为准。程序导出完整 Markdown、三份 JSON、BibTeX 及推导目录。

## 生成网页

需要 Python 3.10 或更新版本，以及 Node.js 22。安装依赖后，在项目根目录运行：

```bash
python -m pip install -r requirements.txt
npm ci --ignore-scripts
python scripts/build_web.py
python scripts/check_package.py
python -m unittest discover -s tests -v
```

网页输出为根目录 `index.html`，双击即可打开。构建时从章节合并正文，把正文公式排成自带字形的 SVG；发布后不需要 MathJax CDN。浏览器只加载项目内的封面，全文搜索与目录在本地执行。

构建报告写入 `build/web-report.json`。如果出现不支持的 TeX、缺失引用或错误链接，构建会失败，不应发布失败后的文件。

生成后应检查改动小节、公式、表格、手机宽度和引用跳转。提交源文件与新的 `index.html`、`manuscript.md`、生成索引和 BibTeX。默认分支的根目录用于 Pages 发布，网站随这些提交更新。

## 自动工作流

`Check and build` 在提交、Pull request 和手动运行时检查来源并重新生成网页，产物可从 Artifacts 下载。工作流不会自动提交文件，也不负责启用 Pages。Pages 的发布来源按根目录 [START_HERE.md](../START_HERE.md) 设置。

只通过 GitHub 网页修改的维护者，可下载产物并更新仓库中的生成文件，无需在个人电脑安装构建环境。

`Build PDF` 只手动运行，会安装中文 TeX 环境并编译 PDF，再生成与之配套的阅读网页。核对后，将需要发布的文件更新到仓库。

## 离线引用检查

只需要 Python 标准库：

```bash
python scripts/validate_refs.py
python scripts/build_index.py --check
```

检查文献编号、文件与锚点、问题引用对应、推导包含次数及显示公式分隔符。`--check` 比较生成快照是否与源文件一致。

自动检查不能证明史实或科学论断正确，也不能判断文献是否真正支持某项结论。它只检查可机械判断的结构与对应关系。

可选外链探测：

```bash
python scripts/check_links.py
```

报告在 `build/link-report.json`。HTTP 404、410 记为无法找到；限流、访问限制和超时记为无法判定。网页可打开不等同于引用正确。可用 `--limit 5` 先检查少量记录。

## 在本地生成 PDF

除了 Python 依赖，还需要 Pandoc 3.x 与 XeLaTeX，TeX 环境须包含 xeCJK、Fandol 字体、unicode-math、tcolorbox、TikZ、longtable、titlesec、tocloft、fancyhdr、bookmark 等。

安装参考：[Python](https://www.python.org/downloads/)、[Pandoc](https://pandoc.org/installing.html)、[TeX Live](https://www.tug.org/texlive/acquire-netinstall.html)。确保 `python`、`pandoc`、`xelatex`、`kpsewhich` 可从终端调用。

```bash
python scripts/build_pdf.py
python scripts/build_web.py
python scripts/check_package.py
```

PDF 写入 `pdf/modern-physics-history.pdf`，中间文件与日志在 `build/`。编译失败或发现缺字时不覆盖已有 PDF。字体默认由 `kpsewhich` 查找；特殊安装可用 `FANDOL_FONT_DIR` 指向 Fandol OTF 字体目录。

本次 1.1.0 发布的网页、完整 Markdown 和 PDF 使用同一份源稿。后续发布时，核对网页页脚与 PDF 封面的版本、日期，正文变更须重建相应输出。

封面日期和版本文字来自 `data/book.json` 的 `date`、`edition`。不同 TeX 版本可能产生分页差异，生成后应打开改动处检查。

## 关系图

图的节点、箭头与双向关系以第 20 章的 Mermaid 源码为准。网页脚本据此绘制 SVG，当前节点布局在 `build_web.py` 的 `graph_svg` 中；节点结构改变时需检查布局。

PDF 使用 `render_latex.py` 中对应的 TikZ 图；源图改变后，脚本会要求同步核对 `diagram` 和 `expected_diagram`。不要只修改某一种阅读版的图。

## 不提交哪些文件

`node_modules/`、`build/`、虚拟环境及 Python 缓存均由 `.gitignore` 排除。不要把构建日志、个人路径或访问凭据放进仓库。
