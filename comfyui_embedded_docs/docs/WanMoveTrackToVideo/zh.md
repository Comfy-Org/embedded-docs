> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/zh.md)

WanMoveTrackToVideo 节点用于准备视频生成所需的 conditioning 和潜在空间数据，并可整合可选的运动跟踪信息。它将起始图像序列编码为潜在表示，并能够融合来自对象轨迹的位置数据，以引导生成视频中的运动。该节点输出修改后的正向和负向 conditioning，以及一个可供视频模型使用的空潜在张量。

## 输入

| 参数 | 数据类型 | 是否必需 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 待修改的正向 conditioning 输入。 |
| `negative` | CONDITIONING | 是 | - | 待修改的负向 conditioning 输入。 |
| `vae` | VAE | 是 | - | 用于将起始图像编码到潜在空间的 VAE 模型。 |
| `tracks` | TRACKS | 否 | - | 包含对象路径的可选运动跟踪数据。 |
| `strength` | FLOAT | 否 | 0.0 - 100.0 | 轨迹 conditioning 的强度。（默认值：1.0） |
| `width` | INT | 否 | 16 - MAX_RESOLUTION | 输出视频的宽度。必须能被 16 整除。（默认值：832） |
| `height` | INT | 否 | 16 - MAX_RESOLUTION | 输出视频的高度。必须能被 16 整除。（默认值：480） |
| `length` | INT | 否 | 1 - MAX_RESOLUTION | 视频序列的帧数。（默认值：81） |
| `batch_size` | INT | 否 | 1 - 4096 | 潜在输出的批次大小。（默认值：1） |
| `start_image` | IMAGE | 是 | - | 要编码的起始图像或图像序列。 |
| `clip_vision_output` | CLIPVISIONOUTPUT | 否 | - | 可选的 CLIP 视觉模型输出，用于添加到 conditioning 中。 |

**注意：** `strength` 参数仅在提供了 `tracks` 时生效。如果未提供 `tracks` 或 `strength` 为 0.0，则不会应用轨迹 conditioning。`start_image` 用于创建 conditioning 所需的潜在图像和遮罩；如果未提供，该节点仅透传 conditioning 并输出一个空潜在张量。

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 修改后的正向 conditioning，可能包含 `concat_latent_image`、`concat_mask` 和 `clip_vision_output`。 |
| `negative` | CONDITIONING | 修改后的负向 conditioning，可能包含 `concat_latent_image`、`concat_mask` 和 `clip_vision_output`。 |
| `latent` | LATENT | 一个空潜在张量，其维度由 `batch_size`、`length`、`height` 和 `width` 输入决定。 |

---
**Source fingerprint (SHA-256):** `9677addf5b94b42efd3015f51380c1fa9b16d4a5105cc7f24de0be34c0042bbc`
