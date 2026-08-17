# WanInfiniteTalkToVideo

WanInfiniteTalkToVideo 节点可根据音频生成一段说话人视频片段。它会将视频扩散模型基于一个或两个说话人的音频特征进行条件化，可选地使用起始图像或先前帧作为上下文，并返回修补后的模型、条件以及用于采样的潜在视频。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `mode` | 音频模式。选择 `"single_speaker"` 时使用单个音频输入。选择 `"two_speakers"` 时会添加下方列出的第二说话人输入。 | DYNAMIC_COMBO | 是 | `"single_speaker"`<br>`"two_speakers"` |
| `model` | 要修补的基础视频扩散模型。 | MODEL | 是 | - |
| `model_patch` | 包含音频投影层的模型补丁。 | MODELPATCH | 是 | - |
| `positive` | 用于引导视频生成的正向条件。 | CONDITIONING | 是 | - |
| `negative` | 用于引导视频生成的负向条件。 | CONDITIONING | 是 | - |
| `vae` | 用于将图像和先前帧编码到潜在空间的 VAE。 | VAE | 是 | - |
| `width` | 生成视频的宽度（像素），步长为 16。（默认值：832） | INT | 是 | 16 - MAX_RESOLUTION（步长 16） |
| `height` | 生成视频的高度（像素），步长为 16。（默认值：480） | INT | 是 | 16 - MAX_RESOLUTION（步长 16） |
| `length` | 要生成的帧数。（默认值：81） | INT | 是 | 1 - MAX_RESOLUTION（步长 4） |
| `audio_encoder_output_1` | 第一说话人的音频编码器输出，包含用于条件化的音频特征。 | AUDIOENCODEROUTPUT | 是 | - |
| `start_image` | 可选的起始图像，用于初始化视频的开头。它会被调整为 `width` 和 `height` 指定的大小。 | IMAGE | 否 | - |
| `clip_vision_output` | 可选的 CLIP 视觉输出，会添加到正向和负向条件中。 | CLIPVISIONOUTPUT | 否 | - |
| `motion_frame_count` | 用作运动上下文的先前帧数。（默认值：9） | INT | 是 | 1 - 33（步长 1） |
| `audio_scale` | 应用于音频条件的缩放因子。（默认值：1.0） | FLOAT | 是 | -10.0 - 10.0（步长 0.01） |
| `previous_frames` | 可选的先前视频帧，用于扩展现有序列。节点会使用最后 `motion_frame_count` 帧作为运动上下文。 | IMAGE | 否 | - |

### 单说话人输入

选择 `single_speaker` 时不会添加任何额外输入。

### 双说话人输入

当 `mode` 为 `"two_speakers"` 时，以下输入可用。

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `audio_encoder_output_2` | 第二说话人的音频编码器输出。提供时，`mask_1` 和 `mask_2` 也必须提供。 | AUDIOENCODEROUTPUT | 否 | - |
| `mask_1` | 第一说话人的遮罩，使用两个音频输入时需要。 | MASK | 否 | - |
| `mask_2` | 第二说话人的遮罩，使用两个音频输入时需要。 | MASK | 否 | - |

**参数约束：**

- 如果提供了 `audio_encoder_output_2`，则必须同时提供 `mask_1` 和 `mask_2`。
- 如果同时提供了 `mask_1` 和 `mask_2`，则必须同时提供 `audio_encoder_output_2`。
- 如果提供了 `previous_frames`，其帧数必须至少等于 `motion_frame_count` 指定的数量。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 已应用音频条件和采样包装器的修补后模型。 | MODEL |
| `positive` | 正向条件，可能已通过起始图像或 CLIP 视觉上下文进行修改。 | CONDITIONING |
| `negative` | 负向条件，可能已通过起始图像或 CLIP 视觉上下文进行修改。 | CONDITIONING |
| `latent` | 表示待生成视频的零初始化潜在张量。 | LATENT |
| `trim_image` | 从先前帧扩展时需要从开头裁剪的帧数；开始新序列时为 0。 | INT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/zh.md)

---
**Source fingerprint (SHA-256):** `b7359490c1de86d9c82122bc227295b3b7f8a3493f629365ae0f22f9f34d9a66`
