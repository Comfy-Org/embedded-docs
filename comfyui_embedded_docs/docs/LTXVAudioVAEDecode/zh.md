# LTXV音频VAE解码

LTXV Audio VAE Decode 节点将音频的潜在表示解码回音频波形。它使用专门的 Audio VAE 模型执行此解码过程，生成具有特定采样率的音频输出。

## 输入
| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `samples` | 要解码的潜在表示。 | LATENT | 是 | N/A |
| `audio_vae` | 用于解码潜在表示的 Audio VAE 模型。 | VAE | 是 | N/A |

**注意：** 如果提供的潜在表示是嵌套的（包含多个潜在表示），该节点将自动使用序列中的最后一个潜在表示进行解码。

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `Audio` | 解码后的音频波形及其对应的采样率。该波形是一个张量，被移动到与输入潜在表示相同的设备上；采样率由 Audio VAE 模型决定。 | AUDIO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEDecode/zh.md)

---
**Source fingerprint (SHA-256):** `fc94f3cb78ede86ada374444d613411cc9bb5849e5cdb8a24074babee50719b1`
