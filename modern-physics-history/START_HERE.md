# 上传到 GitHub：照这三步做

这个包已经包含完整正文、PDF 和可直接打开的网页。第一次上传无需安装软件，也无需修改账号、网址或文件路径。

## 1. 建立空仓库

登录 GitHub，点右上角 **＋ → New repository**：

- **Repository name**：可填 `modern-physics-history`。
- **Description**：可填 `从具体问题出发的现代物理学史：研究者、代表成果、推导与文献。`
- 给大家公开阅读，选 **Public**。
- 不勾选自动生成 README 或 `.gitignore`；许可证先选 **No license**，项目包已说明许可尚未选定。

点击 **Create repository**。

## 2. 上传解压后的全部内容

1. 解压 ZIP，进入 `modern-physics-history` 文件夹。
2. 在空仓库页面点 **uploading an existing file**；已有仓库则点 **Add file → Upload files**。
3. 把这个文件夹**里面的全部文件和子目录**拖入上传区域。根目录应直接能看到 `README.md`、`index.html`、`docs`、`pdf`；不要多套一层文件夹。
4. 确认 `.github`、`.gitignore`、`.nojekyll` 也上传。Windows 若未显示它们，在文件管理器中开启隐藏项目显示。
5. 提交说明可写 `发布现代物理学史讨论稿 1.1.0`，提交到默认分支，然后点 **Commit changes**。若页面显示 **Propose changes**，按提示创建并合并 Pull request 后，内容才进入默认分支。

不要只把 ZIP 上传到仓库。包内文件数量在网页单批 100 个文件、单文件 25 MiB 的限制内。上传完成后，README 会显示在仓库首页，PDF 和分章正文即可阅读。

## 3. 发布阅读网页

若只需要一个可阅读、可讨论的 GitHub 仓库，第二步已经完成。要得到排版好的阅读网站，再做以下设置：

**Settings → Pages → Build and deployment**

- **Source**：选 **Deploy from a branch**。
- **Branch**：选默认分支，通常是 `main`。
- **Folder**：选 **/(root)**。
- 点击 **Save**。

等待部署完成，Pages 页面会显示实际网址。把它填到仓库首页右侧 **About → Website**，以后群里可直接分享这个地址。

本项目已带 `index.html` 和 `.nojekyll`，这里不需要选择自定义 GitHub Actions，也不需要创建新工作流或配置密钥。后续把新版 `index.html` 提交到发布分支，网站会跟着更新。

## 上传后检查三件事

1. 首页点“阅读 PDF”能打开文稿，封面显示本次版本与日期。
2. 网页中能搜索“布朗运动”，能从结果跳到相应内容。
3. **Issues → New issue** 能看到内容勘误、文献建议、新章节和推导补充四个模板。

## 已经上传过旧版

在现有仓库的 **Code** 页面点 **Add file → Upload files**，把新版解压文件夹里面的全部文件和子目录拖入，核对修改后提交。这里更新已有文件并加入新文件，不需要删除仓库或重新设置 Pages。

如果仓库已有其他贡献者尚未收入这个包的修改，请先在新分支上传，用 Pull request 比较并保留这些修改，再合并到默认分支。

随包网页、合并稿和 PDF 已同步更新。以后如果只在 GitHub 上修改正文 Markdown，网页和 PDF 不会立即改写：按 [构建说明](handbook/BUILD.md) 取得并更新生成产物。收到完整新版包时，可直接重复本节的上传步骤。

包内没有个人署名、私人联系方式或本地工作区路径。GitHub 仍会显示仓库账号和提交记录；如需隐藏真实邮箱，可在 GitHub 账号的 Emails 设置中启用邮箱隐私。

后续改稿看 [CONTRIBUTING.md](CONTRIBUTING.md)，需要重新编译时看 [handbook/BUILD.md](handbook/BUILD.md)。

操作依据：[创建仓库](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)、[上传文件](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)、[配置 Pages 发布来源](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)、[提交邮箱设置](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address)。
