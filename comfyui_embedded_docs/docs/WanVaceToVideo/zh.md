# WanVace视频

WanVaceToVideo 节点处理视频生成模型的视频条件数据。它接收正负条件输入以及视频控制数据，并为视频生成准备潜在表示。该节点处理视频放大、遮罩和 VAE 编码，以创建适合视频模型的条件结构。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 用于引导生成的正向条件输入 | CONDITIONING | 是 | - |
| `negative` | 用于引导生成的负向条件输入 | CONDITIONING | 是 | - |
| `vae` | 用于对图像和视频帧进行编码的 VAE 模型 | VAE | 是 | - |
| `width` | 输出视频宽度（像素）（默认值：832，步长：16） | INT | 是 | 16 到 MAX_RESOLUTION |
| `height` | 输出视频高度（像素）（默认值：480，步长：16） | INT | 是 | 16 到 MAX_RESOLUTION |
| `length` | 视频帧数（默认值：81，步长：4） | INT | 是 | 1 到 MAX_RESOLUTION |
| `batch_size` | 同时生成的视频数量（默认值：1） | INT | 是 | 1 到 4096 |
| `strength` | VACE 控制的条件强度（默认值：1.0，步长：0.01）。这不是 LoRA 强度。LoRA 权重通过单独的 LoRA 节点应用。 | FLOAT | 是 | 0.0 到 1000.0 |
| `control_video` | 用于控制条件的可选输入视频。如果未提供，将自动创建中性灰色视频。如果提供，会将其放大到 `width` × `height`，并限制为前 `length` 帧；如果帧数较少，则缺失帧用中性灰色填充。 | IMAGE | 否 | - |
| `control_masks` | 用于控制要修改视频哪些区域的可选遮罩。如果未提供，将使用全白遮罩。如果提供，遮罩会放大到 `width` × `height`，限制为 `length` 帧，如果帧数较少，则用白色填充。 | MASK | 否 | - |
| `reference_image` | 用于额外条件的可选参考图像。如果提供，会将其放大到 `width` × `height`，由 VAE 编码，并前置到潜在序列中。 | IMAGE | 否 | - |

**注意：** 当提供 `control_video` 时，会将其放大到指定的 `width` 和 `height`。如果提供了 `control_masks`，它们也会被放大到相同的尺寸。当提供 `reference_image` 时，会通过 VAE 编码并前置到潜在序列中。`length` 参数决定帧数，潜在长度计算公式为 `((length - 1) // 4) + 1`。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 带有视频控制数据（vace_frames、vace_mask、vace_strength）的正向条件 | CONDITIONING |
| `negative` | 带有视频控制数据（vace_frames、vace_mask、vace_strength）的负向条件 | CONDITIONING |
| `latent` | 准备好用于视频生成的空潜在张量，形状为 [batch_size, 16, latent_length, height/8, width/8] | LATENT |
| `trim_latent` | 使用参考图像时需要修剪的潜在帧数（如果未提供参考图像则为 0） | INT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/zh.md)

---
**Source fingerprint (SHA-256):** `2039b7509ce5b731e9e41d9cd2dad022d4c5004751f571a4cf88c1ba0cae405b`
