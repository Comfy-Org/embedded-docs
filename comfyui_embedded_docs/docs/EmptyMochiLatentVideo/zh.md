# 空Latent视频（Mochi）

EmptyMochiLatentVideo 节点用于创建指定维度的空潜在视频张量。它生成一个零填充的潜在表示，可作为视频生成流程的起点。该节点允许您定义潜在视频张量的宽度、高度、长度和批次大小。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `width` | 潜在视频的宽度（像素），默认值：848，必须能被 16 整除 | INT | 是 | 16 到 MAX_RESOLUTION |
| `height` | 潜在视频的高度（像素），默认值：480，必须能被 16 整除 | INT | 是 | 16 到 MAX_RESOLUTION |
| `length` | 潜在视频的帧数，默认值：25，必须满足 `(length - 1)` 能被 6 整除 | INT | 是 | 7 到 MAX_RESOLUTION |
| `batch_size` | 一批中生成的潜在视频数量，默认值：1 | INT | 否 | 1 到 4096 |

**注意：** 该节点会压缩输入的空间和时间维度。潜在宽度和高度分别计算为 `width / 8` 和 `height / 8`，时间维度计算为 `((length - 1) // 6) + 1`。`length` 参数必须满足 `(length - 1)` 能被 6 整除，即有效值为 7、13、19、25 等。生成的潜在张量具有 12 个通道，最终形状为 `(batch_size, 12, ((length - 1) // 6) + 1, height // 8, width // 8)`。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `samples` | 具有指定维度、包含全零值的空潜在视频张量 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/zh.md)

---
**Source fingerprint (SHA-256):** `1774e1b54b429a946172ba9f609b433d99c0ca2ced2d9e0e3b0b85c82e5141b2`
