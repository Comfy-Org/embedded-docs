# SV3D条件

SV3D_Conditioning 节点使用 SV3D 模型为 3D 视频生成准备 conditioning 数据。它接收一张初始图像，并通过 CLIP vision 和 VAE 编码器进行处理，以生成正面和负面 conditioning，同时生成潜空间表示。该节点会根据指定的视频帧数，生成用于多帧视频生成的相机仰角和方位角序列。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `clip_vision` | 用于编码输入图像的 CLIP vision 模型 | CLIP_VISION | 是 | - |
| `init_image` | 作为 3D 视频生成起点的初始图像 | IMAGE | 是 | - |
| `vae` | 用于将图像编码到潜空间的 VAE 模型 | VAE | 是 | - |
| `width` | 生成视频帧的输出宽度（默认值：576，必须能被 8 整除） | INT | 是 | 16 到 MAX_RESOLUTION（步长为 8） |
| `height` | 生成视频帧的输出高度（默认值：576，必须能被 8 整除） | INT | 是 | 16 到 MAX_RESOLUTION（步长为 8） |
| `video_frames` | 视频序列要生成的帧数（默认值：21） | INT | 是 | 1 到 4096 |
| `elevation` | 3D 视角下应用于每一帧的相机仰角（以度为单位）（默认值：0.0） | FLOAT | 是 | -90.0 到 90.0（步长为 0.1） |

注意：相机方位角从 0 度开始，每帧增加 360 / (video_frames - 1) 度，因此相机将在整个序列中围绕物体完成一次完整环绕。相同的 `elevation` 值会应用于所有帧。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `positive` | 包含图像嵌入和相机参数的正面 conditioning 数据，用于生成过程 | CONDITIONING |
| `negative` | 使用零嵌入的负面 conditioning 数据，用于对比生成 | CONDITIONING |
| `latent` | 维度与指定视频帧数和分辨率匹配的空潜空间张量 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/zh.md)

---
**Source fingerprint (SHA-256):** `e28173cfa560290e66b032687088cf0b981256ca5c21f6aa608e0fdaec886665`
