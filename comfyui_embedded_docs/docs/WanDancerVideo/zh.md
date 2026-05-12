> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/zh.md)

WanDancerVideo 节点用于准备条件数据和一个空的潜空间张量，以便与 WanDancer 模型进行视频生成。它结合了正向和负向条件，并支持可选的输入，如起始图像、遮罩、CLIP 视觉嵌入和音频特征，以控制生成的视频。

## ## 输入

| 参数 | 数据类型 | 是否必需 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | | 用于引导视频生成的正向条件。 |
| `negative` | CONDITIONING | 是 | | 用于引导视频生成的负向条件。 |
| `vae` | VAE | 是 | | 用于将起始图像编码到潜空间中的 VAE。 |
| `width` | INT | 是 | 16 至 MAX_RESOLUTION (步长: 16) | 生成视频的宽度，以像素为单位（默认值：480）。 |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION (步长: 16) | 生成视频的高度，以像素为单位（默认值：832）。 |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION (步长: 4) | 生成视频的帧数。对于 WanDancer 应保持为 149（默认值：149）。 |
| `clip_vision_output` | CLIP_VISION_OUTPUT | 否 | | 第一帧的 CLIP 视觉嵌入。 |
| `clip_vision_output_ref` | CLIP_VISION_OUTPUT | 否 | | 参考图像的 CLIP 视觉嵌入。 |
| `start_image` | IMAGE | 否 | | 要编码的初始图像。可以是任意数量的帧，最多不超过指定的 `length`。 |
| `mask` | MASK | 否 | | 用于起始图像的图像条件遮罩。白色区域保留，黑色区域生成。用于局部生成。 |
| `audio_encoder_output` | AUDIO_ENCODER_OUTPUT | 否 | | 来自音频编码器的输出，提供音频特征、fps 和注入比例，用于音频条件生成。 |

**关于参数约束的说明：**
- `start_image` 和 `mask` 输入是可选的，但可以一起使用。当提供了 `start_image` 时，它会被编码并与潜空间张量拼接。如果还提供了 `mask`，它将控制起始图像的哪些部分被保留（白色）以及哪些部分被重新生成（黑色）。如果未提供 `mask`，则整个起始图像区域将用作条件引导。
- `clip_vision_output` 和 `clip_vision_output_ref` 输入是可选的，可以一起使用，为第一帧和参考图像提供视觉上下文。
- `audio_encoder_output` 输入是可选的，为音频条件生成提供音频特征。

## ## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 附加了额外数据（拼接潜空间、CLIP 视觉、音频）的正向条件。 |
| `negative` | CONDITIONING | 附加了额外数据（拼接潜空间、CLIP 视觉、音频）的负向条件。 |
| `latent` | LATENT | 一个空的潜空间张量，其维度与指定的视频长度、高度和宽度相匹配。 |