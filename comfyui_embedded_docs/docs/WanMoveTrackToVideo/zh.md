# WanMove轨道到视频

WanMoveTrackToVideo 节点为视频生成准备 conditioning 和 latent 数据。它使用 VAE 将起始图像序列编码到潜在空间中，并可选择性地融入运动跟踪信息，以引导生成视频中物体的运动。该节点输出修改后的正向和负向 conditioning，以及准备好用于视频生成模型的空 latent 张量。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 要修改的正向 conditioning 输入。 | CONDITIONING | 是 | - |
| `negative` | 要修改的负向 conditioning 输入。 | CONDITIONING | 是 | - |
| `vae` | 用于将起始图像编码到潜在空间的 VAE 模型。 | VAE | 是 | - |
| `tracks` | 可选的运动跟踪数据，包含物体路径。 | TRACKS | 否 | - |
| `strength` | 跟踪 conditioning 的强度。仅在提供 `tracks` 且值大于 0.0 时生效。（默认值：1.0） | FLOAT | 是 | 0.0 - 100.0 |
| `width` | 输出视频的宽度。按 16 的增量设置。（默认值：832） | INT | 是 | 16 - MAX_RESOLUTION |
| `height` | 输出视频的高度。按 16 的增量设置。（默认值：480） | INT | 是 | 16 - MAX_RESOLUTION |
| `length` | 视频序列中的帧数。按 4 的增量设置。（默认值：81） | INT | 是 | 1 - MAX_RESOLUTION |
| `batch_size` | latent 输出的批量大小。（默认值：1） | INT | 是 | 1 - 4096 |
| `start_image` | 要使用 VAE 编码的起始图像或图像序列。 | IMAGE | 是 | - |
| `clip_vision_output` | 可选的 CLIP 视觉模型输出，用于添加到 conditioning 中。 | CLIP_VISION_OUTPUT | 否 | - |

注意：基于轨迹的运动仅在提供 `tracks` 且 `strength` 大于 0.0 时应用。否则，conditioning 会接收未经修改的编码起始图像。`start_image` 用于创建 latent 图像和用于 conditioning 的掩码；如果不可用，节点仅传递 conditioning 并输出空 latent。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 修改后的正向 conditioning，可能包含 `concat_latent_image`、`concat_mask` 和 `clip_vision_output`。 | CONDITIONING |
| `negative` | 修改后的负向 conditioning，可能包含 `concat_latent_image`、`concat_mask` 和 `clip_vision_output`。 | CONDITIONING |
| `latent` | 一个空的 latent 张量，其维度由 `batch_size`、`length`、`height` 和 `width` 输入决定。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/zh.md)

---
**Source fingerprint (SHA-256):** `b02a1a359d349a0136d84ed77a510c46cb2c8b565650ed54d5fca6c87cd0ab1f`
