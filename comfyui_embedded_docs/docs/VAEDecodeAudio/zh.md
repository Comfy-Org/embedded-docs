# VAE解码（音频）

VAEDecodeAudio 节点使用变分自编码器（VAE）将潜在表示转换回音频波形。它接收编码的音频样本，通过 VAE 处理以重建原始音频，并应用归一化来确保输出电平一致。生成的音频以标准采样率 44100 Hz 返回，如果提供了输入样本的采样率，则使用该采样率。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `samples` | 潜在空间中将要解码回音频波形的编码音频样本 | LATENT | 是 | - |
| `vae` | 用于将潜在样本解码为音频的变分自编码器模型 | VAE | 是 | - |

注意：如果 `samples` 包含嵌套的潜在数据，则仅使用最后一个元素进行解码。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `AUDIO` | 解码后的音频波形，具有归一化音量和采样率（默认：44100 Hz；如果输入 `samples` 中存在采样率，则使用该采样率） | AUDIO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/zh.md)

---
**Source fingerprint (SHA-256):** `2a3f5c912d1d84eea7768979f6b8f0eaa9fe89041f3a3352434f38abd3c09fea`
