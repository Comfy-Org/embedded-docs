# LTXV 参考音频（ID-LoRA）

LTXV Reference Audio 节点在音频生成中为 ID-LoRA 说话人身份迁移设置参考音频片段。它将该片段编码到 conditioning 中，使生成的音频采用说话人的声音特征，并可选地使用身份引导修补模型，在没有参考音频的情况下额外执行一次前向传播，以增强说话人身份效果。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要使用身份引导进行修补的模型。 | MODEL | 是 | - |
| `positive` | 正向 conditioning 输入。 | CONDITIONING | 是 | - |
| `negative` | 负向 conditioning 输入。 | CONDITIONING | 是 | - |
| `reference_audio` | 要迁移其说话人身份的参考音频片段。建议约 5 秒（训练时长）。较短或较长的音频片段可能会降低语音身份迁移效果。 | AUDIO | 是 | - |
| `audio_vae` | 用于编码的 LTXV 音频 VAE。 | VAE | 是 | - |
| `identity_guidance_scale` | 身份引导的强度。每一步都会在没有参考音频的情况下额外执行一次前向传播，以增强说话人身份。设为 0 可禁用（不进行额外传播）。（默认值：3.0） | FLOAT | 否 | 0.0 - 100.0 |
| `start_percent` | 身份引导生效的 sigma 范围的起始点。（默认值：0.0） | FLOAT | 否 | 0.0 - 1.0 |
| `end_percent` | 身份引导生效的 sigma 范围的结束点。（默认值：1.0） | FLOAT | 否 | 0.0 - 1.0 |

注意：身份引导仅在 `start_percent` 和 `end_percent` 定义的 sigma 范围内生效；超出该范围时，去噪输出保持不变。参考音频会被添加到正向和负向 conditioning 中。如果参考音频的采样率与音频 VAE 的采样率不同，音频会自动重采样以匹配 VAE。

## 输出

| 输出名 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 已使用身份引导功能修补的模型。 | MODEL |
| `positive` | 正向 conditioning，现包含编码后的参考音频数据。 | CONDITIONING |
| `negative` | 负向 conditioning，现包含编码后的参考音频数据。 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/zh.md)

---
**Source fingerprint (SHA-256):** `ae15c5838656324667d099614b325b863341f05afda43054658999574522dd49`
