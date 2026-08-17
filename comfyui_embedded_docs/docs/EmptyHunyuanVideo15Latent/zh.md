# 空Latent视频（Hunyuan1.5）

此节点创建一个专门为 HunyuanVideo 1.5 模型格式化的空潜空间张量。它通过分配一个通道数正确、空间尺寸匹配模型潜空间的零张量，为视频生成生成一个空白起点。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 取值范围 |
| --- | --- | --- | --- | --- |
| `width` | 视频帧的宽度（像素）。 | INT | 是 | - |
| `height` | 视频帧的高度（像素）。 | INT | 是 | - |
| `length` | 视频序列中的帧数。 | INT | 是 | - |
| `batch_size` | 一批中生成的视频样本数量（默认值：1）。 | INT | 否 | - |

**注意：** 生成的潜空间张量的空间维度通过将输入的 `width` 和 `height` 除以 16 来计算。时间维度（帧数）按 `((length - 1) // 4) + 1` 计算。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `samples` | 一个空的潜空间张量，其尺寸适用于 HunyuanVideo 1.5 模型。该张量的形状为 `[batch_size, 32, frames, height//16, width//16]`。输出还包含一个值为 16 的 `downscale_ratio_spacial`。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/zh.md)

---
**Source fingerprint (SHA-256):** `ce7ec75e8433c778d175a3e2ea260a4397aa5507428908b9a32f50fbe9e184c6`
