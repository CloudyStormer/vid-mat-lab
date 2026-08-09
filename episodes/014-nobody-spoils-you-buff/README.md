# 第 014 集｜没人惯着你，怎么全是福利

## 状态

- 当前剧情版本：`v2 有来有回版`。用户已明确否定旧剧情 v1 的单向福利表达，要求六个场景完整保留“小耗儿提出要求—NPC 嘴硬回怼—反向发福利”。当前完整剪映导出版本为成片 v1。
- v2 已完成 38 秒制作剧本、171 字口播、SRT、15 镜分镜、15 条图片提示词、剪辑/声音/发布方案；15 张 941×1672 正式 v2 关键帧已于 2026-08-07 全部生成并验收。视频生成提示词已追加 v3 纯文字直接粘贴版，删除关键帧路径、母版路径、内部声音编号和 Voice ID 占位符。
- 2026-08-09：剪映成片 v1 与独立封面已归档。成片 87.842 秒、1440×2528、60 fps、含 AAC 双声道；封面 1440×2528。两份项目副本均与用户提供源文件 SHA-256 一致，当前进入待发布阶段。
- v1 的 21 秒稿和 10 张关键帧保留作历史版本，不得继续作为当前剧情方向生成动态。
- 创建日期：2026-08-06。
- 画面规格：抖音竖屏 9:16，建议 1080×1920。
- 视觉风格：与小耗儿系列一致的原创 Q 版二维手绘动画。
- 内容栏目：生活压力轻短梗｜“没人惯着你”反向 Buff。

## 核心梗

小时候总被说“在外面没人惯着你”，长大后这句话像反向诅咒：小耗儿不要什么，NPC 偏给什么；NPC 嘴上都说“没人惯你”，实际全在发福利。

## 当前生产版结构｜v2

- 0.0—0.6 秒：黑底大字与惊雷，完全后期制作，不交给视频模型生成文字。
- 0.6—7.0 秒：小耗儿在街头完整说出“诅咒”设定；童年画面后期闪回。
- 7.0—32.6 秒：牛肉面、找零、奶茶、送上门、准点下班、免费黑卡六组正反打；每组先说请求，再回怼发福利。
- 32.6—34.6 秒：小耗儿被固定福利道具围住，说“我怎么觉得……不太对呢？”
- 34.6—38.0 秒：亮黄背景挠头憋笑，以屏幕文字点题互动。

## 时长结论

- 用户确认原稿包含 171 个口播汉字。
- 即使按每秒 5.8 字的自然语速上限，纯朗读仍需约 29.5 秒；加上说话人切换和结尾停留后不可能自然装进 20 秒。
- 当前 v2 使用 38.0 秒完整原词时间线，平均约每秒 5.0 字，不暴力倍速、不让两人抢词。

## 声音原则

- 小耗儿统一使用内部声音配置 `VO-XH-01`，实际 `provider_voice_id` / `reference_audio` 必须在批量生成前登记。
- 六名不同场景 NPC 作为同一个喜剧功能型角色，统一使用 `VO-NPC-01`，强化重复梗；同样必须绑定一套实际声音资产。
- 每个视频源片都必须有非空音轨；无对白人物全部闭嘴。
- BGM、惊雷、舀肉、钢镚、布丁、堆包裹、拉闸、拍桌、卡片飞行、憋笑与爱心动效全部后期添加。

## 身份加固

- 永久原版 `assets/brand/resistor-mascot-identity-master-original.jpg` 是唯一最高身份源。
- 新建的 `assets/brand/resistor-mascot-multiview-v1/` 保存正、背、左、右、左 3/4、右 3/4 六视图；正面文件与永久原版字节完全一致，其他五张只作角度参考。用户判退纵长鸡蛋轮廓后，右侧面、左 3/4 与右 3/4 已重做为横向饱满的近圆正式版，旧图只在 `archive-rejected-roundness/` 追溯。
- v2 的 15 个镜头均为正面或接近正面的正反打，图片提示词逐条同时引用永久原版、正面角度图和 v1 同场景参考。
- v2 的 15 条视频提示词逐条包含完整逐帧身份锁，明确禁止动画中变脸、瘦身、长手长腿、纹路跳位、头顶标志变形、肢体增生和换画风。
- v2 图片与视频提示词均明确“小耗”“小耗子”只是口语简称，禁止生成鼠耳、鼠尾、毛发、长鼻或牙齿。
- 初版 04、09、10 因短臂被拉长而判退；当前正式版已返工通过，失败图只保留在关键帧归档目录作追溯。

## 当前交付入口｜v2 有来有回版

- 用户确认原稿：[01-research/source-prompt-v2-conversational.md](01-research/source-prompt-v2-conversational.md)
- 制作简报与时长审计：[01-research/brief-v2-conversational.md](01-research/brief-v2-conversational.md)
- 38 秒制作剧本：[02-script/production-script-v2-conversational.md](02-script/production-script-v2-conversational.md)
- 完整口播：[02-script/voiceover-v2-conversational.md](02-script/voiceover-v2-conversational.md)
- 剪映字幕：[02-script/subtitles-v2-conversational.srt](02-script/subtitles-v2-conversational.srt)
- 连续性与正反打锁定：[03-visuals/continuity-v2-conversational.md](03-visuals/continuity-v2-conversational.md)
- 15 张关键帧计划：[03-visuals/keyframes-v2-conversational/README.md](03-visuals/keyframes-v2-conversational/README.md)
- 15 镜分镜表：[03-visuals/storyboard-v2-conversational.csv](03-visuals/storyboard-v2-conversational.csv)
- 15 条图片提示词：[04-prompts/image-prompts-v2-conversational.md](04-prompts/image-prompts-v2-conversational.md)
- 15 条独立有声视频提示词（v2，保留追溯）：[04-prompts/video-prompts-v2-conversational.md](04-prompts/video-prompts-v2-conversational.md)
- 15 条纯文字直接粘贴视频提示词（当前使用）：[04-prompts/video-prompts-v3-standalone-text.md](04-prompts/video-prompts-v3-standalone-text.md)
- 剪辑方案：[05-editing/edit-plan-v2-conversational.md](05-editing/edit-plan-v2-conversational.md)
- 声音方案：[05-editing/sound-plan-v2-conversational.md](05-editing/sound-plan-v2-conversational.md)
- 声音锚点登记：[05-editing/voice-anchor-register-v1.md](05-editing/voice-anchor-register-v1.md)
- 发布材料：[06-publishing/publishing-v2-conversational.md](06-publishing/publishing-v2-conversational.md)
- 交付状态：[07-deliverables/README.md](07-deliverables/README.md)
- 完整制作包总入口：[07-deliverables/complete-production-package-v2-conversational.md](07-deliverables/complete-production-package-v2-conversational.md)
- 剪映成片 v1：[07-deliverables/episode-014-v1.mp4](07-deliverables/episode-014-v1.mp4)
- 独立封面：[07-deliverables/episode-014-v1-cover.jpg](07-deliverables/episode-014-v1-cover.jpg)
- 成片校验清单：[07-deliverables/MANIFEST.md](07-deliverables/MANIFEST.md)

## 历史版本

- v1 的 21 秒生产稿、10 张正式关键帧和对应提示词均保留在原 `*-v1.*` 文件中，用于追溯本次“单向展示缺少来回”的失败原因。
- v1 不是当前批准方向；未得到用户新的明确指令前，不再按 v1 批量生成动态。

## 下一步

1. 发布前完整播放复核字幕、声音、封面和 AI 内容标识。
2. 发布后登记发布时间、作品链接以及 24/72 小时数据。
3. 如需调整成片或封面，新建 v2 文件，不覆盖当前 v1。
