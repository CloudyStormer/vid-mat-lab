# 第 013 集交付状态｜v2 小耗儿单主角版

## 当前结论

- 当前生产版本：`v2-all-xiaohao`；v1 原样保留为历史记录。
- 17 张竖屏关键帧、22 秒制作剧本、11 句口播、分镜、图片提示词、17 条独立有声视频提示词、剪辑、声音和发布材料均已建立。
- 全部对白只由小耗儿使用 `VO-XH-01` 说；内部编号不是平台真实 Voice ID。
- 正式动态、干声锚点、剪映工程与成片尚未生成或验收，不得标成已完成。

## v2 文件

- [单集入口](../README.md)
- [制作简报](../01-research/brief-v2-all-xiaohao.md)
- [制作剧本](../02-script/production-script-v2-all-xiaohao.md)
- [口播](../02-script/voiceover-v2-all-xiaohao.md)
- [字幕（沿用同文同时码 v1）](../02-script/subtitles-v1.srt)
- [视觉连续性](../03-visuals/continuity-v2-all-xiaohao.md)
- [分镜表](../03-visuals/storyboard-v2-all-xiaohao.csv)
- [关键帧](../03-visuals/keyframes-v2-all-xiaohao/README.md)
- [图片提示词](../04-prompts/image-prompts-v2-all-xiaohao.md)
- [视频提示词](../04-prompts/video-prompts-v2-all-xiaohao.md)
- [剪辑方案](../05-editing/edit-plan-v2-all-xiaohao.md)
- [声音方案](../05-editing/sound-plan-v2-all-xiaohao.md)
- [声音锚点登记](../05-editing/voice-anchor-register-v2-all-xiaohao.md)
- [发布材料](../06-publishing/publishing-v2-all-xiaohao.md)

## 仍需完成

1. 为 `VO-XH-01` 生成 6—10 秒无 BGM、无混响干声样片，并登记提供方、模型、实际 Voice ID / 参考音频、哈希和 seed。
2. 生成并验收 17 个源片：每条必须有非空音轨；11 个对白镜逐字正确且只有小耗儿开口，6 个建立镜只有连续环境底噪。
3. 剪辑统一添加字幕、场景标签、一次性音效和一条有授权的 BGM；导出后复核 22 秒时长、声音和 AI 标识。

## 阻塞

实际声音锚点仍未登记，因此当前不可批量生成对白镜，也不可声称已经锁定声纹。
