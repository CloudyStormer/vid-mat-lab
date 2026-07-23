# 第 006 集素材与提示词总清单

本文件是第 006 集的完整资产入口。以后换电脑或开启新会话时，先读本集 `README.md`，再读本清单，不需要依赖聊天记录寻找“星爷宣传”相关素材。

## 当前优先使用

| 类型 | 文件 | 状态与用途 |
|---|---|---|
| 事实核验 | [`01-research/fact-check.md`](01-research/fact-check.md) | 发布前必须遵守；不使用未经正式确认的票房和续集结论 |
| 原宣传段口播 | [`02-script/voiceover-v1.md`](02-script/voiceover-v1.md) | 木箱广播段四句口播 |
| 黑幕开场口播 | [`02-script/intro-voiceover-v2.md`](02-script/intro-voiceover-v2.md) | “等一下”黑幕揭场段口播 |
| 正式广播首帧 | [`03-visuals/01-stadium-broadcast-start.png`](03-visuals/01-stadium-broadcast-start.png) | 卡通化星爷在左侧观察，小电阻已站在木箱并持喇叭 |
| 正式广播尾帧 | [`03-visuals/02-stadium-broadcast-end.png`](03-visuals/02-stadium-broadcast-end.png) | 同机位广播波、足球与远景球员 |
| 正式封面 | [`03-visuals/cover-poster-v2.png`](03-visuals/cover-poster-v2.png) | 星爷版 1080×1920 抖音封面 |
| 黑幕开场关键帧 | [`03-visuals/intro-v1/README.md`](03-visuals/intro-v1/README.md) | 四张图的顺序、时长与连续性说明 |
| Grok 候选视频 | [`03-visuals/README.md`](03-visuals/README.md) | 本集共归档 5 段候选：2 段 10 秒、3 段 6 秒；先筛选再进入剪映 |
| 星爷版图片提示词 | [`04-prompts/image-prompts-v2-with-stephen.md`](04-prompts/image-prompts-v2-with-stephen.md) | 正式首帧、尾帧和封面图的生成依据 |
| 黑幕开场图片提示词 | [`04-prompts/intro-image-prompts-v1.md`](04-prompts/intro-image-prompts-v1.md) | 四张黑幕揭场关键帧 |
| 跳台段最终提示词 | [`04-prompts/intro-curtain-reveal-v7-start-end-jump-no-clipping.md`](04-prompts/intro-curtain-reveal-v7-start-end-jump-no-clipping.md) | 强制首尾帧、短腿冻结和防穿帮 |
| 正式广播最终提示词 | [`04-prompts/video-prompt-v6-final-zero-head-orb.md`](04-prompts/video-prompt-v6-final-zero-head-orb.md) | 零头顶球、结构高于口型的最终版 |
| 剪辑说明 | [`05-editing/README.md`](05-editing/README.md) | 时间线、验收项和导出参数 |
| 发布包 | [`06-publishing/README.md`](06-publishing/README.md) | 标题、配文、话题、AI 标识和发布设置 |
| 成片目录 | [`07-deliverables/README.md`](07-deliverables/README.md) | 最终剪映成片生成后放入此目录 |

## 视频素材

| 仓库文件 | 原始文件名 | 媒体信息 | SHA-256 | 状态 |
|---|---|---|---|---|
| [`03-grok-generated-video-v1.mp4`](03-visuals/03-grok-generated-video-v1.mp4) | `grok-1026b17e-3b97-4a70-b4cb-b6432d2d84fa-720p.mp4` | 10 秒；5,726,702 字节 | `9ED1ADE435D60F2E6EA060B6CBC31AF9D7815690FB330C0622B6C983E23A3C35` | 较早候选，保留作版本记录 |
| [`04-grok-stadium-announcement-v2.mp4`](03-visuals/04-grok-stadium-announcement-v2.mp4) | `grok-a8197faf-0534-4e01-b25c-5e5b091f5eea-720p.mp4` | 10 秒；720×1280；24fps；5,131,187 字节 | `02C88D91982703F009FDE57F9182EE751380C7801E217CDEDB07BF237F68CEC0` | 本轮 10 秒广播候选；待逐帧验收 |
| [`05-grok-clip-7d9b3c20.mp4`](03-visuals/05-grok-clip-7d9b3c20.mp4) | `grok-7d9b3c20-362c-4426-ac70-d079401ffe77-720p.mp4` | 6 秒；720×1280；24fps；2,409,065 字节 | `AE1DE75805308263EBB3C987F99DF8FE9D7F5B818ED27061F73972561EDD2853` | 本轮补充片段；剪辑时确认实际顺序 |
| [`06-grok-clip-f5f98e25.mp4`](03-visuals/06-grok-clip-f5f98e25.mp4) | `grok-f5f98e25-dd75-4f5b-a706-ff4b3f54c616-720p (1).mp4` | 6 秒；720×1280；24fps；3,234,359 字节 | `120348F1D1C617E7299EF0F5CC7E9D3873CBA8568FC775300FA27DFE633A59A4` | 本轮补充片段；剪辑时确认实际顺序 |
| [`07-grok-clip-a10a77d2.mp4`](03-visuals/07-grok-clip-a10a77d2.mp4) | `grok-a10a77d2-47a7-4ae1-9332-a8b7e45a1f86-720p.mp4` | 6 秒；720×1264；24fps；1,458,883 字节 | `5AA8CE0CE7D667B54D61947EEED65ACEB5BA3D0C04B1C1DA4A38C3B33873B8FD` | 本轮补充片段；高度为 1264，进剪映后按 9:16 画布检查边缘 |

五份视频都是生成素材，不等于剪映最终成片。最终成片只能放入 `07-deliverables/`，不得覆盖候选视频。

## 图片素材

### 正式星爷版

- [`03-visuals/01-stadium-broadcast-start.png`](03-visuals/01-stadium-broadcast-start.png)
- [`03-visuals/02-stadium-broadcast-end.png`](03-visuals/02-stadium-broadcast-end.png)
- [`03-visuals/cover-poster-v2.png`](03-visuals/cover-poster-v2.png)

### 黑幕揭场

- [`03-visuals/intro-v1/01-curtain-slit-emerge.png`](03-visuals/intro-v1/01-curtain-slit-emerge.png)
- [`03-visuals/intro-v1/02-stop-important-message.png`](03-visuals/intro-v1/02-stop-important-message.png)
- [`03-visuals/intro-v1/03-curtain-tear-reveal.png`](03-visuals/intro-v1/03-curtain-tear-reveal.png)
- [`03-visuals/intro-v1/04-hop-to-crate.png`](03-visuals/intro-v1/04-hop-to-crate.png)

### 问题记录与历史草稿

- [`05-editing/issues/README.md`](05-editing/issues/README.md)：额外脑袋、上下叠蛋、第三只手和长腿等失败截图与处理记录。
- [`03-visuals/archive/no-stephen-v1/01-stadium-broadcast-start-no-stephen.png`](03-visuals/archive/no-stephen-v1/01-stadium-broadcast-start-no-stephen.png)：无星爷早期首帧。
- [`03-visuals/archive/no-stephen-v1/02-stadium-broadcast-end-no-stephen.png`](03-visuals/archive/no-stephen-v1/02-stadium-broadcast-end-no-stephen.png)：无星爷早期尾帧。
- [`03-visuals/archive/no-stephen-v1/cover-poster-no-stephen-v1.png`](03-visuals/archive/no-stephen-v1/cover-poster-no-stephen-v1.png)：无星爷早期封面。
- 用户最初提供的热门海报未归档为发布素材：其来源和授权状态不明，只用于气氛与热点分析。

## 提示词版本历史

### 图片提示词

| 版本 | 文件 | 说明 |
|---|---|---|
| v1 | [`image-prompts-v1.md`](04-prompts/image-prompts-v1.md) | 早期无星爷构思，历史版本 |
| v2 | [`image-prompts-v2-with-stephen.md`](04-prompts/image-prompts-v2-with-stephen.md) | 正式星爷版首尾帧与封面 |
| 开场 v1 | [`intro-image-prompts-v1.md`](04-prompts/intro-image-prompts-v1.md) | 黑幕裂开、喊停、揭场和落箱四张关键帧 |

### 正式广播视频提示词

| 版本 | 文件 | 说明 |
|---|---|---|
| v1 | [`video-prompt-v1.md`](04-prompts/video-prompt-v1.md) | 初始构思 |
| v2 | [`video-prompt-v2-with-stephen.md`](04-prompts/video-prompt-v2-with-stephen.md) | 加入卡通化星爷 |
| v3 | [`video-prompt-v3-prop-persistence-mouth.md`](04-prompts/video-prompt-v3-prop-persistence-mouth.md) | 喇叭持续存在与唯一嘴 |
| v4 | [`video-prompt-v4-four-locks-natural-football.md`](04-prompts/video-prompt-v4-four-locks-natural-football.md) | 无头顶球、两手持喇叭和自然踢球 |
| v5 | [`video-prompt-v5-happy-announcement-anatomy-lock.md`](04-prompts/video-prompt-v5-happy-announcement-anatomy-lock.md) | 愉快宣布、五官和短肢锁定 |
| v6 | [`video-prompt-v6-final-zero-head-orb.md`](04-prompts/video-prompt-v6-final-zero-head-orb.md) | 当前最终版：口型与喇叭冲突时优先保结构，头顶球必须为 0 |

### 黑幕揭场视频提示词

| 版本 | 文件 | 说明 |
|---|---|---|
| v1 | [`intro-curtain-reveal-v1.md`](04-prompts/intro-curtain-reveal-v1.md) | 初始三段首尾帧动画 |
| v2 | [`intro-curtain-reveal-v2-anatomy-lock.md`](04-prompts/intro-curtain-reveal-v2-anatomy-lock.md) | 单蛋主体与四肢拓扑 |
| v3 | [`intro-curtain-reveal-v3-exact-reference.md`](04-prompts/intro-curtain-reveal-v3-exact-reference.md) | 参考图外形与短肢冻结 |
| v4 | [`intro-curtain-reveal-v4-single-anchor.md`](04-prompts/intro-curtain-reveal-v4-single-anchor.md) | 单参考帧与固定手部任务 |
| v5 | [`intro-curtain-reveal-v5-two-frame-continuity.md`](04-prompts/intro-curtain-reveal-v5-two-frame-continuity.md) | 二至四段双帧连续衔接 |
| v6 | [`intro-curtain-reveal-v6-three-assets-two-clips.md`](04-prompts/intro-curtain-reveal-v6-three-assets-two-clips.md) | 三项素材压缩为后两段 |
| v7 | [`intro-curtain-reveal-v7-start-end-jump-no-clipping.md`](04-prompts/intro-curtain-reveal-v7-start-end-jump-no-clipping.md) | 当前优先版：跳台首尾帧、短腿冻结与防穿帮 |

## 当前剪辑取舍

1. 开场采用黑幕揭场方案；已有动态可以继续使用，不必为追求复杂动作反复重生成人体错误。
2. 先在五段 Grok 候选中确认每段故事位置，再逐帧检查。头顶圆球、第二张脸、第三只手或长腿任一出现，都不能作为最终镜头。
3. 若最新候选结构正确但口型不明显，可以保留画面，在剪映中以配音、字幕和广播音效补足；结构正确优先于明显口型。
4. 星爷只作为明显卡通化、沉默的场边观察者；不得生成真实发言、背书或未经核验的影片信息。
