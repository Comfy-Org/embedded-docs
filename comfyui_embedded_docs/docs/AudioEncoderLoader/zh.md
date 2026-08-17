# 加载音频编码器

`AudioEncoderLoader` 节点从您的 audio encoders 文件夹中的文件加载音频编码器模型。它接受音频编码器模型的文件名作为输入，并返回加载后的模型，该模型随后可用于工作流中的音频处理任务。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `audio_encoder_name` | 选择要加载的音频编码器模型文件 | COMBO | 是 | audio_encoders 文件夹中可用的音频编码器文件列表 |

注意：所选文件必须包含有效的音频编码器模型。如果文件无效且不包含有效模型，节点将引发错误。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `audio_encoder` | 已加载的音频编码器模型，可随时用于音频处理工作流 | AUDIO_ENCODER |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/zh.md)

---
**Source fingerprint (SHA-256):** `780d0c7fcf571e5ef02d273791e5d2e894baa6d5900d845ed65e9ce669769f7e`
