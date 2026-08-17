# Hunyuan Video 15超分辨率

HunyuanVideo15SuperResolution 节点用于为视频超分辨率过程准备条件数据。它接收视频的潜在表示，并可选择接收起始图像，将它们与噪声增强值以及可选的 CLIP 视觉数据打包成模型可用来生成更高分辨率输出的格式。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 要与拼接后的潜在数据和噪声增强数据一起修改的正向条件输入。 | CONDITIONING | 是 | 不适用 |
| `negative` | 要与拼接后的潜在数据和噪声增强数据一起修改的负向条件输入。 | CONDITIONING | 是 | 不适用 |
| `vae` | 用于对可选的 `start_image` 进行编码的 VAE。如果提供了 `start_image`，则此项为必填。 | VAE | 否 | 不适用 |
| `start_image` | 可选的起始图像，用于引导超分辨率过程。如果提供，它会被放大、使用 `vae` 编码，并放置在条件潜在数据的起始位置。 | IMAGE | 否 | 不适用 |
| `clip_vision_output` | 可选的 CLIP 视觉嵌入。如果提供，它们会被添加到正向和负向条件中。 | CLIP_VISION_OUTPUT | 否 | 不适用 |
| `latent` | 要纳入条件中的视频潜在表示。 | LATENT | 是 | 不适用 |
| `noise_augmentation` | 应用于条件的噪声增强强度（默认值：0.70）。这是一个高级参数。 | FLOAT | 是 | 0.0 - 1.0（步长 0.01） |

**注意：** 如果你提供了 `start_image`，则还必须连接一个 `vae` 以便对其进行编码。`start_image` 会自动放大以匹配输入 `latent` 所隐含的尺寸，并且 VAE 仅使用其前三个颜色通道（RGB）。

## 输出

| 输出名 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 修改后的正向条件，现在包含拼接后的潜在数据、噪声增强数据以及可选的 CLIP 视觉数据。 | CONDITIONING |
| `negative` | 修改后的负向条件，现在包含拼接后的潜在数据、噪声增强数据以及可选的 CLIP 视觉数据。 | CONDITIONING |
| `latent` | 输入的潜在数据，原样传递，不做更改。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/zh.md)

---
**Source fingerprint (SHA-256):** `c9e64092e78423f5e0dc43446a77240e09100242c25e4fccc91491049fe76be5`
