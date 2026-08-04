# 第 013 集｜外耗不是伤人，是把问题还回去

## 状态

- 当前阶段：22 秒竖屏生产包与 17 张关键帧已完成；待锁定声音锚点并生成动态
- 创建日期：2026-08-04
- 画面规格：抖音竖屏 9:16，建议 1080×1920
- 目标时长：22 秒
- 视觉风格：原创 Q 版二维手绘动画，快节奏爽感剪辑
- 内容栏目：生活边界｜把不合理责任还回去

## 与历史单集的关系

本集与第 003 集“把问题原路还回去”同属边界反拨主题，但不是覆盖版：第 003 集是约 85 秒横版八场景成片，本集是 22 秒竖屏六场景快切续作。

## 核心判断

“外耗”不是主动伤人，也不是拿外貌、年龄、职业或疾病攻击别人；爽点来自把不合理要求、责任和成本还给提出它的人。

## 22 秒结构

1. 0.0—1.6 秒：小耗儿红底怼脸钩子。
2. 1.6—3.6 秒：原创配角小欧、小伏与小耗儿三连快切。
3. 3.6—19.0 秒：错餐、家长甩锅、理发推销、插队、服装店先入为主、私教硬推六个场景。
4. 19.0—22.0 秒：三人并排收束：“外耗不是伤人，是把问题还回去。”

## 角色与声音

- 主角：小耗儿，严格使用永久母版；内部声音配置编号 `VO-XH-01`。
- 原创配角：小欧，蓝色插头形电气小伙伴；内部声音配置编号 `VO-XO-01`。
- 原创配角：小伏，珊瑚橙电表形电气小伙伴；内部声音配置编号 `VO-XF-01`。
- 用户草稿中的“小八 / 吉伊”没有提供可核验的原创底稿，因此生产版不猜造型、不复刻第三方角色，改为原创电气系配角；原始草稿完整保存在研究目录。

## 制作策略

- 17 个片段全部独立生成，冲突建立镜与回击镜分开。
- 每个 clip 最多一名说话者、一个主要动作；其他人物闭嘴并保持静止。
- 每条视频提示词都写明“必须有声音”；说话片段强制复用同一平台实际 Voice ID / 参考音频和同一声音描述，内部 `VO-*` 编号不得冒充平台 Voice ID。
- 红底震动、闪白、字幕、数字、BGM、惊雷、打脸和人群笑声均后期制作，不让视频模型自动生成。

## 当前交付

- 原始草稿：[01-research/source-prompt-v1.md](01-research/source-prompt-v1.md)
- 制作简报：[01-research/brief-v1.md](01-research/brief-v1.md)
- 制作剧本：[02-script/production-script-v1.md](02-script/production-script-v1.md)
- 口播：[02-script/voiceover-v1.md](02-script/voiceover-v1.md)
- 字幕：[02-script/subtitles-v1.srt](02-script/subtitles-v1.srt)
- 连续性：[03-visuals/continuity-v1.md](03-visuals/continuity-v1.md)
- 分镜表：[03-visuals/storyboard-v1.csv](03-visuals/storyboard-v1.csv)
- 关键帧：[03-visuals/keyframes-v1/README.md](03-visuals/keyframes-v1/README.md)
- 图片提示词：[04-prompts/image-prompts-v1.md](04-prompts/image-prompts-v1.md)
- 视频提示词：[04-prompts/video-prompts-v1.md](04-prompts/video-prompts-v1.md)
- 剪辑方案：[05-editing/edit-plan-v1.md](05-editing/edit-plan-v1.md)
- 声音方案：[05-editing/sound-plan-v1.md](05-editing/sound-plan-v1.md)
- 声音锚点登记：[05-editing/voice-anchor-register-v1.md](05-editing/voice-anchor-register-v1.md)
- 发布材料：[06-publishing/publishing-v1.md](06-publishing/publishing-v1.md)
- 交付状态：[07-deliverables/README.md](07-deliverables/README.md)

## 下一步

1. 分别为 `VO-XH-01`、`VO-XO-01`、`VO-XF-01` 制作并验收 6—10 秒干声锚点，登记平台实际 Voice ID、参考音频、模型版本和 seed（若支持）。
2. 按 17 条独立提示词生成有声视频；失败时只重做对应片段，同一角色不得逐片更换音色。
3. 剪映按 22 秒时间轴快切，统一添加黄色黑边字幕、一次性音效和一条连续 BGM。
