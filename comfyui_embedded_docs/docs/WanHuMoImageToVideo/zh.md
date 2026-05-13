> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/zh.md)

### 概述

WanHuMoImageToVideo 节点通过生成视频帧的潜在表示，将图像转换为视频序列。它处理条件输入，并可结合参考图像和音频嵌入来影响视频生成。该节点输出修改后的条件数据以及适用于视频合成的潜在表示。

### 输入

| 参数 | 数据类型 | 是否必填 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 正向条件输入，引导视频生成朝向期望内容 |
| `negative` | CONDITIONING | 是 | - | 负向条件输入，引导视频生成远离不期望内容 |
| `vae` | VAE | 是 | - | 用于将参考图像编码到潜在空间的 VAE 模型 |
| `width` | INT | 是 | 16 至 MAX_RESOLUTION | 输出视频帧的宽度（像素），默认值：832，必须能被 16 整除 |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION | 输出视频帧的高度（像素），默认值：480，必须能被 16 整除 |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION | 生成视频序列的帧数，默认值：97，必须满足 (length - 1) 能被 4 整除 |
| `batch_size` | INT | 是 | 1 至 4096 | 同时生成的视频序列数量，默认值：1 |
| `audio_encoder_output` | AUDIOENCODEROUTPUT | 否 | - | 可选的音频编码数据，可根据音频内容影响视频生成 |
| `ref_image` | IMAGE | 否 | - | 可选的参考图像，用于引导视频生成的风格和内容 |

**注意：** 当提供参考图像时，它会被编码并添加到正向和负向条件中。当提供音频编码器输出时，它会被处理并整合到条件数据中。如果两者均未提供，则参考潜在表示和音频嵌入均使用零填充的占位张量。

### 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 修改后的正向条件，已整合参考图像和/或音频嵌入 |
| `negative` | CONDITIONING | 修改后的负向条件，已整合参考图像和/或音频嵌入 |
| `latent` | LATENT | 生成的潜在表示，包含视频序列数据 |

---
**Source fingerprint (SHA-256):** `6301671d04748ce80c561a65df80c7ca146b91bcce8851872df40211af29fd39`
