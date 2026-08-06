# 第 014 集｜没人惯着你，怎么全是福利

## 状态

- 当前阶段：21 秒生产稿、10 张正式关键帧、10 条独立有声视频提示词和完整剪辑/声音/发布包已完成；待登记实际声音锚点后生成动态。
- 创建日期：2026-08-06。
- 画面规格：抖音竖屏 9:16，建议 1080×1920。
- 视觉风格：与小耗儿系列一致的原创 Q 版二维手绘动画。
- 内容栏目：生活压力轻短梗｜“没人惯着你”反向 Buff。

## 核心梗

小时候总被说“在外面没人惯着你”，长大后这句话像反向诅咒：小耗儿不要什么，NPC 偏给什么；NPC 嘴上都说“没人惯你”，实际全在发福利。

## 生产版结构

- 0.0—0.6 秒：黑底大字与惊雷，完全后期制作，不交给视频模型生成文字。
- 0.6—3.0 秒：街头小耗儿＋童年闪回，建立“我妈说，外面没人惯着你”。
- 3.0—15.0 秒：牛肉面、找零、奶茶、送上门、准点下班、免费黑卡六连反向福利。
- 15.0—17.0 秒：小耗儿抱满福利，口是心非说头疼。
- 17.0—21.0 秒：亮黄背景眨眼收束，引导点赞留言。

## 声音原则

- 小耗儿统一使用内部声音配置 `VO-XH-01`，实际 `provider_voice_id` / `reference_audio` 必须在批量生成前登记。
- 六名不同场景 NPC 作为同一个喜剧功能型角色，统一使用 `VO-NPC-01`，强化重复梗；同样必须绑定一套实际声音资产。
- 每个视频源片都必须有非空音轨；无对白人物全部闭嘴。
- BGM、惊雷、舀肉、钢镚、布丁、堆包裹、拉闸、拍桌、卡片飞行、憋笑与爱心动效全部后期添加。

## 身份加固

- 永久原版 `assets/brand/resistor-mascot-identity-master-original.jpg` 是唯一最高身份源。
- 新建的 `assets/brand/resistor-mascot-multiview-v1/` 保存正、背、左、右、左 3/4、右 3/4 六视图；正面文件与永久原版字节完全一致，其他五张只作角度参考。用户判退纵长鸡蛋轮廓后，右侧面、左 3/4 与右 3/4 已重做为横向饱满的近圆正式版，旧图只在 `archive-rejected-roundness/` 追溯。
- 本集 10 个镜头均为正面或接近正面，图片提示词逐条同时引用永久原版与正面角度图。
- 10 条视频提示词逐条包含完整逐帧身份锁，明确禁止动画中变脸、瘦身、长手长腿、纹路跳位、头顶标志变形、肢体增生和换画风。
- 本集 10 条图片提示词与 10 条视频提示词已同步加入圆度硬门槛：正面、背面和 3/4 的机体宽度不得低于高度的 95%，纯侧面不得低于 92%，任何帧都禁止纵向鸡蛋化。
- 初版 04、09、10 因短臂被拉长而判退；当前正式版已返工通过，失败图只保留在关键帧归档目录作追溯。

## 当前交付入口

- 原始草稿：[01-research/source-prompt-v1.md](01-research/source-prompt-v1.md)
- 制作简报：[01-research/brief-v1.md](01-research/brief-v1.md)
- 21 秒制作剧本：[02-script/production-script-v1.md](02-script/production-script-v1.md)
- 口播：[02-script/voiceover-v1.md](02-script/voiceover-v1.md)
- 字幕：[02-script/subtitles-v1.srt](02-script/subtitles-v1.srt)
- 连续性锁定：[03-visuals/continuity-v1.md](03-visuals/continuity-v1.md)
- 10 张关键帧：[03-visuals/keyframes-v1/README.md](03-visuals/keyframes-v1/README.md)
- 分镜表：[03-visuals/storyboard-v1.csv](03-visuals/storyboard-v1.csv)
- 图片提示词：[04-prompts/image-prompts-v1.md](04-prompts/image-prompts-v1.md)
- 10 条独立有声视频提示词：[04-prompts/video-prompts-v1.md](04-prompts/video-prompts-v1.md)
- 剪辑方案：[05-editing/edit-plan-v1.md](05-editing/edit-plan-v1.md)
- 声音方案：[05-editing/sound-plan-v1.md](05-editing/sound-plan-v1.md)
- 声音锚点登记：[05-editing/voice-anchor-register-v1.md](05-editing/voice-anchor-register-v1.md)
- 发布材料：[06-publishing/publishing-v1.md](06-publishing/publishing-v1.md)
- 交付状态：[07-deliverables/README.md](07-deliverables/README.md)

## 下一步

1. 为 `VO-XH-01` 与 `VO-NPC-01` 各制作并人工验收一条 6—10 秒干声锚点，登记实际声音资产、模型、哈希和 seed。
2. 先试生镜头 01 与 03，确认固定音色、逐字对白、无牙口型、非空音轨和逐帧身份不漂移。
3. 批量生成其余 8 条有声源片，按 21 秒方案剪辑并完成五点抽帧验收。
