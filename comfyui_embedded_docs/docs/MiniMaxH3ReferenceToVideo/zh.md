# MiniMax H3 参考转视频

MiniMax H3 参考转视频（Reference to Video）节点创建用于 MiniMax H3 参考转视频生成所需的文本条件（text conditioning）和空音频-视频潜在表示（latent）。您提供提示词以及可选的参考图像、视频和音频片段，该节点会将这些参考编码为模型在生成过程中可使用的令牌（tokens）。提示词通过 `<Picture i>`、`<Video k>` 和 `<Audio j>` 标签引用这些参考。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `clip` | 用于将提示词进行分词（tokenize）并将参考媒体编码为条件令牌的 CLIP 模型。 | CLIP | 是 | |
| `vae` | 用于将参考图像和参考视频帧编码到潜在空间的 VAE。 | VAE | 是 | |
| `audio_vae` | 用于将参考音频编码到潜在空间的 VAE（音频采样率 32 kHz）。 | VAE | 是 | |
| `prompt` | 视频的文本提示词。参考媒体可通过 `<Picture i>`、`<Video k>` 和 `<Audio j>` 标签引用（每种类型从 1 开始编号）。支持多行和动态提示词。 | STRING | 是 | |
| `width` | 生成视频的宽度（像素），默认值：1344。 | INT | 是 | 32 to 16384 (step 32) |
| `height` | 生成视频的高度（像素），默认值：768。 | INT | 是 | 32 to 16384 (step 32) |
| `length` | 24 fps 下的帧数；124 ≈ 约 5 秒，训练范围约为 124-362（默认值：124）。 | INT | 是 | 5 to 3600 (step 17) |
| `ref_image_size` | 参考图像尺寸模式。`match` 仅按比例缩小每个参考图像，保持宽高比，使其适应生成画面的像素面积；`max` 使用参考管线中 2048px 的短边以获得最佳身份保真度。参考令牌会贯穿每个采样步骤，因此 `max` 可能慢数倍（默认值：`match`）。 | COMBO | 是 | `"match"`<br>`"max"` |
| `ref_images` | 可选参考图像。每张图像若大于 2048px 短边则缩小，且永远不会放大。可提供多张图像。 | IMAGE | 否 | 0 to 9 |
| `ref_videos` | 可选参考视频帧，24 fps（2-15 秒）。可提供多个视频。 | IMAGE | 否 | 0 to 3 |
| `ref_video_audios` | 可选配对的参考视频音轨，按索引对应；`ref_video_audio_N` 是与同编号 `ref_video_N` 对应的音轨。 | AUDIO | 否 | 0 to 3 |
| `ref_audios` | 可选独立参考音频片段。 | AUDIO | 否 | 0 to 3 |

注释：
- 提示词通过每种类型从 1 开始的标签引用参考媒体：`<Picture i>` 用于图像，`<Video k>` 用于视频，`<Audio j>` 用于音频。参考媒体按固定顺序呈现给模型：先是图像，然后是视频（每个音轨的 `<Audio j>` 标签紧跟在其对应的 `<Video k>` 之前），最后是独立音频。
- 参考视频至少必须包含 5 帧（24 fps 下约 0.2 秒），否则节点会报错。视频帧将被限制在所选 `length` 内，并修剪为受支持的帧数。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `positive` | 包含编码后的提示词以及 MiniMax H3 模型使用的编码参考图像、视频和音频令牌的条件。 | CONDITIONING |
| `latent` | 具有所请求的 `width`、`height` 和 `length`（帧数）的空音频-视频潜在表示。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/zh.md)

---
**Source fingerprint (SHA-256):** `d9a444e712cdc255d7c56a3ab38d0523659f198b3228b9283a7028cfd0e4f3f9`
