# WanPhantom主体转视频

WanPhantomSubjectToVideo 节点通过处理 conditioning 输入和可选的参考图像来生成视频内容。它会为视频生成创建潜在表示，并在提供输入图像时融合其中的视觉引导。该节点为 Wan 视频模型准备具有时间维度拼接的 conditioning 数据，并输出修改后的 conditioning 以及生成的潜在视频数据。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 用于引导视频生成的正面 conditioning 输入 | CONDITIONING | 是 | - |
| `negative` | 用于避免特定特征的负面 conditioning 输入 | CONDITIONING | 是 | - |
| `vae` | 用于在提供图像时进行编码的 VAE 模型 | VAE | 是 | - |
| `width` | 输出视频的宽度（像素，默认值：832，必须能被 16 整除） | INT | 是 | 16 到 MAX_RESOLUTION |
| `height` | 输出视频的高度（像素，默认值：480，必须能被 16 整除） | INT | 是 | 16 到 MAX_RESOLUTION |
| `length` | 生成视频的帧数（默认值：81，必须能被 4 整除） | INT | 是 | 1 到 MAX_RESOLUTION |
| `batch_size` | 同时生成的视频数量（默认值：1） | INT | 是 | 1 到 4096 |
| `images` | 用于时间维度 conditioning 的可选参考图像 | IMAGE | 否 | - |

**注意：** 当提供 `images` 时，它们会自动放大以匹配指定的 `width` 和 `height`，并且仅使用前 `length` 帧进行处理。每张图像在由 VAE 编码之前会缩减为其前 3 个颜色通道。当未提供 `images` 时，conditioning 输入将保持不变地传递。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 提供图像时，经过时间维度拼接的修改后正面 conditioning | CONDITIONING |
| `negative_text` | 提供图像时，经过时间维度拼接的修改后负面 conditioning | CONDITIONING |
| `negative_img_text` | 提供图像时，具有零值时间维度拼接的负面 conditioning | CONDITIONING |
| `latent` | 零填充的潜在视频表示，具有 16 个通道，时间维度为 ((length - 1) // 4) + 1，空间维度为 height // 8 和 width // 8 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/zh.md)

---
**Source fingerprint (SHA-256):** `a1853382f6e564f66262b69dd7b06cc58e26b93386a460a98e6fcc2ff6acf12b`
