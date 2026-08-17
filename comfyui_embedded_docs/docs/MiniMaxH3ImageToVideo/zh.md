# MiniMax H3 图像转视频

MiniMax H3 图像转视频节点用于准备使用 MiniMax H3 模型生成视频所需的条件输入（conditioning）和空潜空间表示（latent）。它接收文本提示词，并可选择接收视频首帧和/或尾帧的图像，然后将这些输入转换为模型输入。关键帧图像会被调整大小、编码，并附加到视频开头和结尾的 conditioning 中。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `clip` | 用于对提示词进行分词，并将关键帧图像编码为 conditioning 的 CLIP 模型。 | CLIP | 是 |  |
| `vae` | 用于在提供关键帧图像时将其编码到潜空间中的 VAE 模型。 | VAE | 是 |  |
| `prompt` | 描述要生成的视频的文本提示词。支持多行和动态提示词。 | STRING | 是 |  |
| `width` | 视频宽度（像素），默认值：1344。 | INT | 是 | 32 to MAX_RESOLUTION (step 32) |
| `height` | 视频高度（像素），默认值：768。 | INT | 是 | 32 to MAX_RESOLUTION (step 32) |
| `length` | 24 fps 下的帧数，会向上对齐到模型的 17k+5 网格（124 ≈ 5 秒；训练范围约为 124-362，更长未测试），默认值：124。 | INT | 是 | 5 to 3600 (step 17) |
| `first_frame` | 可选图像，用作视频的第一帧。该图像会被拉伸到整个画布大小，因此不保留其宽高比。仅使用输入批次中的第一张图像。 | IMAGE | 否 |  |
| `last_frame` | 可选图像，用作视频的最后一帧。该图像会被裁剪以覆盖画布，同时保留其宽高比。仅使用输入批次中的第一张图像。 | IMAGE | 否 |  |

当提供 `first_frame` 和/或 `last_frame` 时，关键帧图像会通过 VAE 编码，并分别附加到 conditioning 的第 0 帧和最后一帧。如果两者均未提供，则此节点仅根据提示词工作。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `positive` | 包含编码后的提示词，以及在提供关键帧图像时，编码后的关键帧位于 MiniMax H3 模型视频的第一帧和最后一帧的 conditioning。 | CONDITIONING |
| `latent` | 表示要生成的视频及其伴随音轨的空 latent，包含请求的宽度、高度和帧数。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageToVideo/zh.md)

---
**Source fingerprint (SHA-256):** `d1bdf3f8c66ef20ff11c35203d2c266a88dcf8cc00c65dbb0aea2b1dd16befd6`
