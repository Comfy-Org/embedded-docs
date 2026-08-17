# 万相机图像转视频

WanCameraImageToVideo 根据图像准备用于视频生成的条件数据和潜空间数据。它接收正向和负向条件提示，以及可选的起始图像和相机控制，并输出修改后的条件数据和一个空的潜空间张量，供视频模型填充。

## 输入
| 参数 | 说明 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 用于视频生成的正向条件提示 | CONDITIONING | 是 | - |
| `negative` | 要在视频生成中避免的负向条件提示 | CONDITIONING | 是 | - |
| `vae` | 用于将图像编码到潜空间的 VAE 模型 | VAE | 是 | - |
| `width` | 输出视频宽度（像素）（默认值：832，步长：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `height` | 输出视频高度（像素）（默认值：480，步长：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `length` | 视频序列中的帧数（默认值：81，步长：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `batch_size` | 同时生成的视频数量（默认值：1） | INT | 是 | 1 to 4096 |
| `clip_vision_output` | 可选的 CLIP 视觉输出，用于附加条件化 | CLIP_VISION_OUTPUT | 否 | - |
| `start_image` | 用于初始化视频序列的可选起始图像。提供后，视频的前几帧将基于此图像，并应用蒙版将起始帧与生成内容混合。图像会被调整大小以匹配指定的宽度和高度。 | IMAGE | 否 | - |
| `camera_conditions` | 用于视频生成的可选相机嵌入条件。提供后，这些条件将同时应用于正向和负向条件数据。 | WAN_CAMERA_EMBEDDING | 否 | - |

**注意：** 当提供 `start_image` 时，节点会使用它来初始化视频序列，并应用蒙版将起始帧与生成内容混合。`camera_conditions` 和 `clip_vision_output` 参数是可选的，但提供后会同时修改正向和负向提示的条件数据。

## 输出
| 输出名称 | 说明 | 数据类型 |
| --- | --- | --- |
| `positive` | 已应用相机条件、CLIP 视觉输出和/或起始图像数据的修改后正向条件数据 | CONDITIONING |
| `negative` | 已应用相机条件、CLIP 视觉输出和/或起始图像数据的修改后负向条件数据 | CONDITIONING |
| `latent` | 生成供视频模型使用的空视频潜空间表示。潜空间张量的维度为 [batch_size, 16, frames, height/8, width/8]，其中 frames 按 ((length - 1) // 4) + 1 计算。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/zh.md)

---
**Source fingerprint (SHA-256):** `467a82be0dfd6ac1c3b2dd2a6cb02e0d0749de4536a7fbdb000456b817b20ebb`
