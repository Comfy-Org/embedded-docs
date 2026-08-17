# 图像到视频扩展（WanSound）

WanSoundImageToVideoExtend 节点通过生成额外的帧来扩展现有的视频潜在表示，可选地由音频、参考图像和控制视频引导。它接受一个起始视频潜在表示，并生成更长的视频序列，利用提供的条件和音频线索来影响新内容。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 指导视频应包含内容的正面条件提示 | CONDITIONING | 是 | - |
| `negative` | 指定视频应避免内容的负面条件提示 | CONDITIONING | 是 | - |
| `vae` | 用于编码和解码视频帧的变分自编码器 | VAE | 是 | - |
| `length` | 为视频序列生成的总帧数（默认值：77，步长：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `video_latent` | 初始视频潜在表示，作为扩展的起点。宽度、高度、批大小和帧偏移均从此潜在表示中派生。此潜在表示的最后 19 帧也用作新序列的参考运动。 | LATENT | 是 | - |
| `audio_encoder_output` | 可选的音频嵌入，可根据声音特性影响视频生成。提供时，音频会被插值并用于创建音频嵌入桶，该桶将添加到条件中。 | AUDIO_ENCODER_OUTPUT | 否 | - |
| `ref_image` | 可选的参考图像，为视频生成提供视觉引导。图像被放大以匹配目标尺寸并编码为潜在表示，然后添加到正面和负面条件中。仅使用批次中的第一张图像。 | IMAGE | 否 | - |
| `control_video` | 可选的控制视频，可引导生成视频的运动和风格。视频被放大、编码，并添加到正面和负面条件中。控制视频会被截断到指定的 `length`。 | IMAGE | 否 | - |

注意：当提供 `audio_encoder_output` 时，音频嵌入会被添加到正面条件中，而负面条件会接收相同的但设置为零的嵌入。从 `video_latent` 派生的帧偏移决定了新帧在音频序列中的起始位置。如果音频序列没有足够的帧来覆盖请求的扩展长度，则不应用音频条件。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `positive` | 已应用视频上下文的处理后正面条件，包括音频嵌入、参考潜在表示、参考运动，以及控制视频（如果提供） | CONDITIONING |
| `negative` | 已应用视频上下文的处理后负面条件，包括音频嵌入（已置零）、参考潜在表示、参考运动，以及控制视频（如果提供） | CONDITIONING |
| `latent` | 生成包含扩展视频序列的视频潜在表示，初始化为零，维度从输入的 `video_latent` 和目标 `length` 派生 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/zh.md)

---
**Source fingerprint (SHA-256):** `32b58aaba566f346a0388ba804fc92e7ad426bf2e9e7039e5fdb0bf6a746e972`
