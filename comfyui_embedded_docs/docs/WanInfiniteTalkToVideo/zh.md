> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/zh.md)

WanInfiniteTalkToVideo 节点可根据音频输入生成视频序列。它使用视频扩散模型，以从一个或两个说话者提取的音频特征为条件，生成说话人头视频的潜在表示。该节点可以生成新序列，或利用先前帧的运动上下文来扩展现有序列。

## 输入

| 参数 | 数据类型 | 是否必需 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `mode` | COMBO | 是 | `"single_speaker"`<br>`"two_speakers"` | 音频输入模式。`"single_speaker"` 使用一个音频输入。`"two_speakers"` 启用第二个说话者的输入及对应的遮罩。 |
| `model` | MODEL | 是 | - | 基础视频扩散模型。 |
| `model_patch` | MODELPATCH | 是 | - | 包含音频投影层的模型补丁。 |
| `positive` | CONDITIONING | 是 | - | 用于引导生成的正向条件。 |
| `negative` | CONDITIONING | 是 | - | 用于引导生成的负向条件。 |
| `vae` | VAE | 是 | - | 用于将图像编码到潜在空间及从潜在空间解码的 VAE。 |
| `width` | INT | 否 | 16 - MAX_RESOLUTION | 输出视频的宽度（像素）。必须能被 16 整除。（默认值：832） |
| `height` | INT | 否 | 16 - MAX_RESOLUTION | 输出视频的高度（像素）。必须能被 16 整除。（默认值：480） |
| `length` | INT | 否 | 1 - MAX_RESOLUTION | 要生成的帧数。（默认值：81） |
| `clip_vision_output` | CLIPVISIONOUTPUT | 否 | - | 可选的 CLIP 视觉输出，用于额外的条件控制。 |
| `start_image` | IMAGE | 否 | - | 可选的起始图像，用于初始化视频序列。 |
| `audio_encoder_output_1` | AUDIOENCODEROUTPUT | 是 | - | 包含第一个说话者特征的主音频编码器输出。 |
| `motion_frame_count` | INT | 否 | 1 - 33 | 扩展序列时用作运动上下文的先前帧数。（默认值：9） |
| `audio_scale` | FLOAT | 否 | -10.0 - 10.0 | 应用于音频条件的缩放因子。（默认值：1.0） |
| `previous_frames` | IMAGE | 否 | - | 可选的先前视频帧，用于从中扩展。 |
| `audio_encoder_output_2` | AUDIOENCODEROUTPUT | 否 | - | 第二个音频编码器输出。当 `mode` 设置为 `"two_speakers"` 时必需。 |
| `mask_1` | MASK | 否 | - | 第一个说话者的遮罩，如果使用两个音频输入则必需。 |
| `mask_2` | MASK | 否 | - | 第二个说话者的遮罩，如果使用两个音频输入则必需。 |

**参数约束：**

* 当 `mode` 设置为 `"two_speakers"` 时，参数 `audio_encoder_output_2`、`mask_1` 和 `mask_2` 变为必需。
* 如果提供了 `audio_encoder_output_2`，则必须同时提供 `mask_1` 和 `mask_2`。
* 如果提供了 `mask_1` 和 `mask_2`，则必须同时提供 `audio_encoder_output_2`。
* 如果提供了 `previous_frames`，则其包含的帧数必须至少等于 `motion_frame_count` 指定的数量。

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 已应用音频条件的修补模型。 |
| `positive` | CONDITIONING | 正向条件，可能已通过额外上下文（例如起始图像、CLIP 视觉）进行修改。 |
| `negative` | CONDITIONING | 负向条件，可能已通过额外上下文进行修改。 |
| `latent` | LATENT | 潜在空间中生成的视频序列。 |
| `trim_image` | INT | 扩展序列时，应从运动上下文起始处裁剪的帧数。 |

---
**Source fingerprint (SHA-256):** `6bb976da5cac0b61edb7d4c9d206c7c7ea9ffc0e982034c23c7f2e891e972888`
