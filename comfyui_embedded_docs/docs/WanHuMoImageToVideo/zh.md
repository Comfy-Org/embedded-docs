# 万虎魔图像转视频

WanHuMoImageToVideo 节点为图像到视频生成准备条件数据和潜空间。它创建一个空的潜视频张量，可选地使用 VAE 对参考图像进行编码，并可选择性地将音频编码器输出转换为视频时序条件。该节点输出正向和负向条件流，以及一个用于后续视频采样的潜变量张量。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 正向条件输入，引导视频生成朝向期望的内容。 | CONDITIONING | 是 | - |
| `negative` | 负向条件输入，使视频生成避开不希望出现的内容。 | CONDITIONING | 是 | - |
| `vae` | 用于将参考图像编码到潜空间的 VAE 模型。 | VAE | 是 | - |
| `width` | 输出视频帧的宽度（像素），默认值：832；必须能被 16 整除。 | INT | 是 | 16 to MAX_RESOLUTION (step 16) |
| `height` | 输出视频帧的高度（像素），默认值：480；必须能被 16 整除。 | INT | 是 | 16 to MAX_RESOLUTION (step 16) |
| `length` | 生成的视频序列中的帧数，默认值：97；必须满足 `(length - 1)` 能被 4 整除。 | INT | 是 | 1 to MAX_RESOLUTION (step 4) |
| `batch_size` | 同时生成的视频序列数量，默认值：1。 | INT | 是 | 1 to 4096 |
| `audio_encoder_output` | 可选的音频编码器输出，用于根据音频内容影响视频生成。 | AUDIO_ENCODER_OUTPUT | 否 | - |
| `ref_image` | 可选的参考图像，用于指导视频生成的风格和内容。 | IMAGE | 否 | - |

**注意：** 当提供了 `ref_image` 时，会将其调整为 `width` x `height`，使用 `vae` 编码，并作为参考潜变量添加到正向和负向条件中。当未提供参考图像时，使用零参考潜变量。当提供了 `audio_encoder_output` 时，会处理其音频嵌入，并作为音频嵌入添加到两个条件流中；否则使用零音频嵌入。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 添加了参考潜变量和音频嵌入信息的正向条件。 | CONDITIONING |
| `negative` | 添加了参考潜变量和音频嵌入信息的负向条件。 | CONDITIONING |
| `latent` | 表示视频序列的潜变量张量，根据 `batch_size`、`length`、`height` 和 `width` 初始化为零。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/zh.md)

---
**Source fingerprint (SHA-256):** `db674a4a00729a8715988030083e2858f958cd21de73bbbe4ed6d76f5f539419`
