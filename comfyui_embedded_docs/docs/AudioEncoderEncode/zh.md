# 音频编码器编码

AudioEncoderEncode 节点通过使用音频编码器模型对音频数据进行编码来处理音频数据。它接收音频输入，并将其转换为可在 conditioning 流程中用于进一步处理的编码表示。此节点将原始音频波形转换为适合基于音频的机器学习应用的格式。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `audio_encoder` | 用于处理音频输入的音频编码器模型 | AUDIO_ENCODER | 是 | - |
| `audio` | 包含波形和采样率信息的音频数据 | AUDIO | 是 | - |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `output` | 由音频编码器生成的编码音频表示 | AUDIO_ENCODER_OUTPUT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderEncode/zh.md)

---
**Source fingerprint (SHA-256):** `85f77152ccc1e3f4687e2b655283e69e03d90b862d6a676dcb89ea973dd70a63`
