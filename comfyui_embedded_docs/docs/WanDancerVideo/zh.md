# WanDancerVideo

WanDancerVideo 节点用于准备条件数据和一个空 latent 张量，以配合 WanDancer 模型进行视频生成。它接收正负条件，并可选地与起始图像、掩码、CLIP 视觉嵌入以及音频特征组合，从而控制生成的视频。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 用于引导视频生成的正面条件。 | CONDITIONING | 是 |  |
| `negative` | 用于引导视频生成的负面条件。 | CONDITIONING | 是 |  |
| `vae` | 用于将起始图像编码到潜在空间的 VAE。 | VAE | 是 |  |
| `width` | 生成视频的宽度（像素），默认值：480。 | INT | 是 | 16 到 MAX_RESOLUTION（步长：16） |
| `height` | 生成视频的高度（像素），默认值：832。 | INT | 是 | 16 到 MAX_RESOLUTION（步长：16） |
| `length` | 生成视频的帧数。对于 WanDancer 应保持为 149（默认值：149）。 | INT | 是 | 1 到 MAX_RESOLUTION（步长：4） |
| `clip_vision_output` | 第一帧的 CLIP 视觉嵌入。 | CLIP_VISION_OUTPUT | 否 |  |
| `clip_vision_output_ref` | 参考图像的 CLIP 视觉嵌入。 | CLIP_VISION_OUTPUT | 否 |  |
| `start_image` | 要编码的初始图像，可以是任意数量的帧。 | IMAGE | 否 |  |
| `mask` | 用于起始图像的图像条件掩码。白色区域保留，黑色区域生成。用于局部生成。 | MASK | 否 |  |
| `audio_encoder_output` | 来自音频编码器的输出，提供音频特征、FPS 和音频注入比例，用于音频条件生成。 | AUDIO_ENCODER_OUTPUT | 否 |  |

**关于参数约束的说明：**
- 当提供 `start_image` 时，它会被调整为 `width` × `height`，限制为 `length` 帧，并编码为一个 latent，该 latent 连同一个 concat 掩码一起附加到两个条件上。
- `mask` 仅在同时提供 `start_image` 时生效。在掩码中，白色区域被保留，黑色区域被生成。当未提供 `mask` 时，起始图像区域作为条件引导，其余帧由模型生成。
- `clip_vision_output_ref` 仅在提供 `clip_vision_output` 时应用。
- `audio_encoder_output` 会将音频特征、FPS 和音频注入比例（默认 1.0）附加到两个条件上。

## 输出

| 输出名 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 附加了额外数据（concat latent、CLIP 视觉、音频）的正面条件。 | CONDITIONING |
| `negative` | 附加了额外数据（concat latent、CLIP 视觉、音频）的负面条件。 | CONDITIONING |
| `latent` | 一个空 latent 张量，其维度与指定的视频长度、高度和宽度相匹配。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/zh.md)

---
**Source fingerprint (SHA-256):** `086a0ec361cf7f7ae7ce9505b55d31d92b025c6c7c9cde192009e6664011ad05`
