# 文本编码（QwenImageEdit）

TextEncodeQwenImageEdit 节点处理文本提示和可选图像，以生成用于图像生成或编辑的条件数据。它使用 CLIP 模型对输入进行分词，并可选地使用 VAE 对参考图像进行编码，以创建参考潜在表示。当提供图像时，节点会自动调整图像大小，以保持一致的处理维度。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `clip` | 用于文本和图像分词处理的 CLIP 模型 | CLIP | 是 | - |
| `prompt` | 用于条件生成的文本提示，支持多行输入和动态提示 | STRING | 是 | - |
| `vae` | 可选 VAE 模型，用于将参考图像编码为潜在表示 | VAE | 否 | - |
| `image` | 用于参考或编辑目的的可选输入图像 | IMAGE | 否 | - |

**注意：** 当同时提供 `image` 和 `vae` 时，节点会将图像编码为参考潜在表示，并将其附加到条件输出中。图像会自动调整大小，以保持约 1024x1024 像素的一致处理尺度。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `CONDITIONING` | 包含文本令牌和可选参考潜在表示的条件数据，用于图像生成 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEdit/zh.md)

---
**Source fingerprint (SHA-256):** `ec6980a63eab0d6c95be3abea00b2bf3018d30a1267f0b39a21be29a3e9228fe`
