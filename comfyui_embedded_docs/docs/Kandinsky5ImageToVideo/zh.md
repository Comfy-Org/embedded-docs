# 图像到视频（Kandinsky5）

Kandinsky5ImageToVideo 节点使用 Kandinsky 模型为视频生成准备 conditioning 和潜在空间数据。它创建一个空的视频潜在张量，并可选地编码起始图像以引导生成视频的初始帧，相应地修改 positive 和 negative conditioning。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 引导视频生成的正面 conditioning 提示。 | CONDITIONING | 是 | N/A |
| `negative` | 引导视频生成远离某些概念的负面 conditioning 提示。 | CONDITIONING | 是 | N/A |
| `vae` | 用于将可选的起始图像编码到潜在空间中的 VAE 模型。 | VAE | 是 | N/A |
| `width` | 输出视频的宽度（像素）（默认值：768）。 | INT | 是 | 16 到 8192（步长 16） |
| `height` | 输出视频的高度（像素）（默认值：512）。 | INT | 是 | 16 到 8192（步长 16） |
| `length` | 视频中的帧数（默认值：121）。 | INT | 是 | 1 到 8192（步长 4） |
| `batch_size` | 同时生成的视频序列数量（默认值：1）。 | INT | 是 | 1 到 4096 |
| `start_image` | 可选的起始图像。如果提供，则将其编码并用于替换模型输出潜在张量中的噪声起始部分。 | IMAGE | 否 | N/A |

**注意：** 当提供 `start_image` 时，它会使用双线性插值调整为指定的 `width` 和 `height`。仅使用图像的前 `length` 帧进行编码。随后，编码后的潜在张量会与一个标记起始帧的掩码一起注入到 `positive` 和 `negative` conditioning 中，从而用干净的编码图像替换生成视频的噪声起始段。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 修改后的正面 conditioning，可能已更新为包含编码后的起始图像数据。 | CONDITIONING |
| `negative` | 修改后的负面 conditioning，可能已更新为包含编码后的起始图像数据。 | CONDITIONING |
| `latent` | 一个用零填充的空视频潜在张量，其形状根据指定的 `batch_size`、`length`、`height` 和 `width` 确定。 | LATENT |
| `cond_latent` | 所提供起始图像的干净编码潜在表示。用于替换模型输出潜在张量中的噪声起始部分。当未提供 `start_image` 时为空。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/zh.md)

---
**Source fingerprint (SHA-256):** `7212f0ea912578d3b72dddf1333a20054a881e3f22c2b8abd9645fc21e75a08b`
