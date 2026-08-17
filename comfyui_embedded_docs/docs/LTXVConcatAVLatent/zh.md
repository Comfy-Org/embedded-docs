# 拼接 AV 潜空间

## 输入
| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `video_latent` | 视频数据的潜空间表示。 | LATENT | 是 |  |
| `audio_latent` | 要与视频潜空间组合的音频数据的潜空间表示。 | LATENT | 是 |  |

**关于音频长度的说明：** 当 `video_latent` 已经是 AV 潜空间时，`audio_latent` 除了一个维度外，必须在所有维度上与嵌入的音频流匹配。节点会沿该维度对音频进行裁剪或零填充，以适配现有流的长度。填充的尾部保持未掩码状态，以便模型生成该部分。

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `latent` | 包含配对的视频和音频 `samples` 的潜空间。如果任一输入提供了 `noise_mask`，输出还会包含配对的 `noise_mask`；缺失的掩码会被替换为全 1 掩码。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/zh.md)

---
**Source fingerprint (SHA-256):** `0231f9db2ce73132d8555fbb33f295b68aa68a0c1c54e4a0c5d2e1f67b5611cb`
