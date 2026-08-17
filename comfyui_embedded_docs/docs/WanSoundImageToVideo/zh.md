# 图像到视频（WanSound）

WanSoundImageToVideo 节点用于根据图像准备视频生成，并支持可选的音频条件。它接收正向和负向条件提示以及 VAE 模型，以构建条件输入和空潜空间张量；同时还可结合参考图像、音频编码、控制视频和运动参考来指导视频生成过程。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 正向条件提示，用于指导生成视频中应出现的内容 | CONDITIONING | 是 | - |
| `negative` | 负向条件提示，用于指定生成视频中应避免的内容 | CONDITIONING | 是 | - |
| `vae` | 用于对视频潜空间表示进行编码和解码的 VAE 模型 | VAE | 是 | - |
| `width` | 输出视频的宽度（以像素为单位）（默认值：832，必须能被 16 整除） | INT | 是 | 16 to MAX_RESOLUTION (step: 16) |
| `height` | 输出视频的高度（以像素为单位）（默认值：480，必须能被 16 整除） | INT | 是 | 16 to MAX_RESOLUTION (step: 16) |
| `length` | 生成视频的帧数（默认值：77，必须能被 4 整除） | INT | 是 | 1 to MAX_RESOLUTION (step: 4) |
| `batch_size` | 同时生成的视频数量（默认值：1） | INT | 是 | 1 to 4096 |
| `audio_encoder_output` | 可选的音频编码，可根据声音特征影响视频生成。提供时，音频特征会被插值并用作视频生成的条件。 | AUDIOENCODEROUTPUT | 否 | - |
| `ref_image` | 可选的参考图像，为视频内容提供视觉指导。图像会按指定的宽度和高度放大，然后编码为潜空间表示。仅使用输入批次中的第一张图像。 | IMAGE | 否 | - |
| `control_video` | 可选的控制视频，用于指导生成视频的运动和结构。视频会按指定的尺寸放大并编码，然后用于条件化输出。仅使用前 `length` 帧。 | IMAGE | 否 | - |
| `ref_motion` | 可选的运动参考，为视频中的运动模式提供指导。如果输入超过 73 帧，则仅使用最后 73 帧。如果提供的帧数少于 73，则序列将用中性帧填充。 | IMAGE | 否 | - |

**注意：** 可选输入（`audio_encoder_output`、`ref_image`、`control_video`、`ref_motion`）可以单独使用，也可以组合使用。控制视频条件始终会应用；当未提供 `control_video` 时，会使用空（零）控制视频。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 为视频生成而修改的正向条件。当提供了相应的可选输入时，它包含音频嵌入、参考潜空间表示、运动参考和控制视频条件。 | CONDITIONING |
| `negative` | 为视频生成而修改的负向条件。当提供了相应的可选输入时，它包含音频嵌入（置零）、参考潜空间表示、运动参考和控制视频条件。 | CONDITIONING |
| `latent` | 用作视频生成起点的空潜空间张量。该潜空间张量的形状为 [batch_size, 16, latent_t, height/8, width/8]，其中 latent_t = ((length - 1) // 4) + 1。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/zh.md)

---
**Source fingerprint (SHA-256):** `b1148cd00d8999dd6842e3c2fb13655fda8f20d5befed975a6d1652688b2807c`
