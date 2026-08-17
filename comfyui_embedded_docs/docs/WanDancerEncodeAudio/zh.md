# WanDancerEncodeAudio

此节点处理音频输入，以提取可用于引导视频生成模型的特征。它分析音频以检测节奏、节拍和其他音乐特性，然后将这些信息打包成适合条件化视频模型的格式，从而使生成的视频能够与音频同步。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `audio` | 待分析和编码的音频输入。 | AUDIO | 是 | - |
| `video_frames` | 目标视频的帧数。用于计算同步所需的帧率（默认值：149）。 | INT | 是 | 最小值：1，最大值：268435456（MAX_RESOLUTION），步长：4 |
| `audio_inject_scale` | 音频特征注入视频模型时的缩放比例（默认值：1.0）。 | FLOAT | 是 | 最小值：0.0，最大值：10.0，步长：0.01 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `audio_encoder_output` | 包含处理后的音频特征、计算出的帧率（fps）和音频注入缩放比例的字典。该输出用于条件化视频生成模型。 | AUDIO_ENCODER_OUTPUT |
| `fps_string` | 描述基于音频长度和视频帧数计算出的帧率（fps）的文本字符串。此字符串旨在用于视频模型的提示词中。 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/zh.md)

---
**Source fingerprint (SHA-256):** `ce27a3bdea2d9e3cf8875c24236a2a0a1429e9bc13a58581e372fb669d2c0018`
