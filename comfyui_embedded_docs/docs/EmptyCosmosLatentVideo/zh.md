# 空Latent视频（Cosmos）

The EmptyCosmosLatentVideo node creates an empty latent video tensor with specified dimensions. It generates a zero-filled latent representation that can be used as a starting point for video generation workflows, with configurable width, height, length, and batch size parameters. The spatial dimensions of the latent are downsampled by a factor of 8.

EmptyCosmosLatentVideo 节点创建一个具有指定维度的空潜在视频张量。它生成一个零填充的潜在表示，可作为视频生成工作流的起始点，具有可配置的宽度、高度、长度和批量大小参数。潜在空间的空间维度按 8 倍下采样。

## 输入
| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `width` | The width of the latent video in pixels (default: 1280, must be divisible by 16) | INT | Yes | 16 to MAX_RESOLUTION |
| `height` | The height of the latent video in pixels (default: 704, must be divisible by 16) | INT | Yes | 16 to MAX_RESOLUTION |
| `length` | The number of frames in the latent video (default: 121, must be divisible by 8) | INT | Yes | 1 to MAX_RESOLUTION |
| `batch_size` | The number of latent videos to generate in a batch (default: 1) | INT | Yes | 1 to 4096 |

The latent tensor uses 16 channels. Spatial dimensions are divided by 8 compared to the pixel dimensions (height // 8, width // 8), and the frame count is compressed to ((length - 1) // 8) + 1 latent frames.

潜在张量使用 16 个通道。与像素尺寸相比，空间维度除以 8（`height // 8`、`width // 8`），帧数压缩为 `((length - 1) // 8) + 1` 个潜在帧。

## 输出
| Output Name | Description | Data Type |
| --- | --- | --- |
| `samples` | The generated empty latent video tensor with zero values. Shape: (batch_size, 16, ((length - 1) // 8) + 1, height // 8, width // 8) | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/zh.md)

---
**Source fingerprint (SHA-256):** `7ee194324b02367ed853f6d36bc51742081bac6a9469c4a619586e0560a1b33b`
