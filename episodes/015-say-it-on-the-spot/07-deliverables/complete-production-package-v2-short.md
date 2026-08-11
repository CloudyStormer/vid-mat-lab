# 第 015 集完整制作包 v2-short

## 项目概况

- 单集：第 015 集。
- 版本：`v2-short`。
- 主题：职场边界《别人的锅，别背回家》。
- 结构：自然开场 + 两组职场正反打 + 自然结尾，共 6 镜。
- 画幅与帧率：9:16，1080×1920，60fps。
- 有效成片计划：26.55 秒。
- 状态：静态制作包完成，待动态试生。

## 制作顺序

1. 先查看 [六张关键帧](../03-visuals/keyframes-v2-short/README.md) 与 [连续性设定](../03-visuals/continuity-v2-short.md)。
2. 在同一视频工具会话中先试生镜头 001；确认小耗儿形象、同步口型与声音方向后，再生成 002、003。
3. 顺序试听镜头 001 与 003；只有小耗儿音色可接受且无明显跳变，才继续 004—006。
4. 每次使用对应关键帧，并整框复制 [六条独立视频提示词](../04-prompts/video-prompts-v2-short.md) 中同编号的一条。
5. 按 [分镜表](../03-visuals/storyboard-v2-short.csv) 裁取有效片段，不把固定 6 秒源片剩余空转放入成片。
6. 依照 [剪辑方案](../05-editing/edit-plan-v2-short.md) 合成，导入 [字幕](../02-script/subtitles-v2-short.srt)，再按 [声音方案](../05-editing/sound-plan-v2-short.md) 混音。
7. 发布时使用 [发布材料](../06-publishing/publishing-v2-short.md)。

## 唯一事实源

- 锁定文字：[确认文字](../01-research/source-dialogue-v2-short.md)
- 精确时码与语速：[分镜表](../03-visuals/storyboard-v2-short.csv)
- 逐段复制口播：[口播稿](../02-script/voiceover-v2-short.md)
- 角色与场景连续性：[连续性设定](../03-visuals/continuity-v2-short.md)
- 直接生成命令：[视频提示词](../04-prompts/video-prompts-v2-short.md)
- 声音真实登记：[声音锚点登记](../05-editing/voice-anchor-register-v2-short.md)

## 素材状态

- 新生成并验收：镜头 001、006。
- 从历史 v1 复制并重新编号：镜头 002、003、004、005。
- 六张图片均已登记尺寸、来源与 SHA-256，详见 [关键帧清单](../03-visuals/keyframe-manifest-v2-short.csv)。
- 动态视频、真实声音锚点、成片与封面尚不存在，不得写成已完成。

## 验收底线

- 六句逐字不变；每镜只允许一名说话者。
- 六段语速均为每秒 5.0—5.6 个汉字；0.30 秒闭嘴准备和 0.45 秒自然收口必须完整。
- 小耗儿逐帧保持单一横向近圆电阻体、恰好两短手、两极短腿、唯一无牙小嘴和固定黄蓝标志。
- 正反打听者留在画外，不出现错误口型、同事夸张受惊或多人抢话。
- 当前内部声音编号不得冒充真实平台 Voice ID；未完成实际登记前不得宣称已锁声纹。
- 历史 v1 长合集完整保留，不删除、不覆盖、不伪装成当前短版。
