# 内耗儿绝缘体｜短视频内容实验室

这个仓库保存账号“内耗儿绝缘体”的内容方法、角色资产和每一集视频的完整交付。它的作用不是只存成品，而是让我们换一台电脑、开启一个新的 Codex 会话后，也能直接接着制作下一集，不依赖聊天记录。

## 当前状态

- 账号：内耗儿绝缘体
- 内容主线：年轻打工人的工作压力、生活与金钱压力、关系矛盾，以及如何减少内耗
- 固定 IP：圆滚滚的白色小电阻人
- 当前画面规格：横版 16:9，建议 1920×1080
- 已归档：[第 001 集｜健身公式不能直接画等号](episodes/001-fitness-formulas-no-equals/README.md)
- 第 001 集状态：已于 2026-07-15 19:50 发布；初始约 40 次播放、留存和互动偏弱，正在等待 24/72 小时数据复盘
- 第 002 集：[刷新数据刷到发疯](episodes/002-refreshing-stats-meltdown/README.md)，成片已由用户在剪映导出，待完成媒体归档
- 当前制作：[第 003 集｜不吵架，也不委屈自己](episodes/003-calm-boundaries-daily-life/README.md)

## 换电脑后怎样继续

先同步仓库：

~~~powershell
git clone git@github.com:CloudyStormer/vid-mat-lab.git
cd vid-mat-lab
git pull
~~~

然后在 Codex 里直接发送：

~~~text
请先完整读取 AGENTS.md、docs/ACCOUNT_POSITIONING.md、
docs/VIDEO_WORKFLOW.md、episodes/README.md，
再读取最新一集的 README。按照仓库规范开始下一集，
不要依赖以前的聊天上下文。
~~~

开始第二集时，从 [单集模板](templates/episode/README.md) 复制一份，建立：

~~~text
episodes/002-英文短标题/
~~~

每次结束前必须更新本集 README 和 [剧集索引](episodes/README.md)，再提交并推送。这样另一台电脑只需执行 git pull。

## 必读文档

- [Codex 仓库工作约定](AGENTS.md)
- [账号定位与表达规范](docs/ACCOUNT_POSITIONING.md)
- [通用视频生产流程](docs/VIDEO_WORKFLOW.md)
- [剧集索引](episodes/README.md)
- [项目商业模式与合规底线](docs/BUSINESS_MODEL.md)

## 目录结构

~~~text
vid-mat-lab/
├─ AGENTS.md                    # 新会话自动遵循的工作约定
├─ README.md                    # 项目入口和跨电脑接续方法
├─ docs/                        # 长期有效的账号与生产方法
├─ assets/
│  └─ brand/                   # 全集共用的 IP 与品牌资产
├─ templates/
│  └─ episode/                 # 新一集的复制模板
├─ episodes/
│  ├─ README.md                # 全部剧集索引
│  └─ 001-.../                 # 一个子目录代表一集视频
└─ analysis/                   # 项目前期商业与可行性分析
~~~

## 单集目录约定

每一集使用三位编号和英文短标题，例如：

~~~text
episodes/002-workplace-emotional-labor/
~~~

标准子目录：

~~~text
01-research/      选题来源、事实核验和参考链接
02-script/        口播、字幕和历史版本
03-visuals/       分镜图片、封面和联系表
04-prompts/       图片与视频生成提示词
05-editing/       剪辑顺序、参数和问题记录
06-publishing/    标题、配文、标签和发布设置
07-deliverables/  导出状态与最终文件说明
~~~

## 一集完成的最低标准

1. 事实和结论可核验，不把“可能”写成“必然”。
2. 口播自然、简短、专业；一个画面对应一个独立语音段落。
3. 画面使用统一 IP，规格和构图一致。
4. 字幕、语音、图片逐段对应，音乐不压人声。
5. 封面、标题、配文、AI 标识和发布设置完整。
6. 本集 README 记录做了什么、遇到什么问题、最终如何解决。
7. 推送到远程仓库后才算完成交接。
