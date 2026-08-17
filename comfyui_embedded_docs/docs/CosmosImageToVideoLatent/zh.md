# 图像到视频Latent（Cosmos）

CosmosImageToVideoLatent 节点用于创建图像到视频生成的视频潜在表示。它从空白 latent 开始，并可选地将开始图像和/或结束图像编码到视频序列的首帧或末帧。当提供图像时，它还会生成一个噪声掩码，将编码帧标记为生成过程中保持固定。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `vae` | 用于将输入图像编码到潜在空间的 VAE 模型 | VAE | 是 | - |
| `width` | 输出视频的宽度，以像素为单位（默认值：1280） | INT | 是 | 16 to MAX_RESOLUTION (step 16) |
| `height` | 输出视频的高度，以像素为单位（默认值：704） | INT | 是 | 16 to MAX_RESOLUTION (step 16) |
| `length` | 视频序列中的帧数（默认值：121） | INT | 是 | 1 to MAX_RESOLUTION (step 8) |
| `batch_size` | 输出批次中要生成的视频潜在表示数量（默认值：1） | INT | 是 | 1 to 4096 |
| `start_image` | 可选图像或图像序列，用于编码到视频序列的开头 | IMAGE | 否 | - |
| `end_image` | 可选图像或图像序列，用于编码到视频序列的末尾 | IMAGE | 否 | - |

**注：** 当未提供 `start_image` 或 `end_image` 时，节点返回不带噪声掩码的空白潜在表示。当至少提供一个图像时，结果中包含 `noise_mask`：由所提供图像编码得到的 latent 帧掩码值为 0（保持固定），其余帧的掩码值为 1（待生成）。图像在编码前会调整到目标 `width` 和 `height`，从输入图像中提取的帧数等于其批次维度，最大不超过 `length`。该潜在表示具有 16 个通道，空间维度为 `width / 8` 和 `height / 8`，帧数为 `((length - 1) // 8) + 1`。当提供图像时，潜在表示及其噪声掩码会重复 `batch_size` 次以构成输出批次。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `latent` | 一个 LATENT，包含视频潜在表示 `samples`；当提供 `start_image` 或 `end_image` 时，还包含标记编码帧为固定的 `noise_mask` | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/zh.md)

---
**Source fingerprint (SHA-256):** `0b06ccfcb14c27c81eeebbbff519da1e187970d4cfc19c8796fc3da20688245c`
