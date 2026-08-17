# InstructPixToPix条件

InstructPixToPixConditioning 节点通过将输入图像与正向和负向文本提示条件结合，为 InstructPix2Pix 图像编辑准备条件数据。它使用 VAE 将图像编码为潜在表示，将该潜在表示附加到两个条件集，并创建一个尺寸匹配的零填充潜在张量。如果图像的宽度或高度不是 8 像素的倍数，则在编码前自动裁剪图像。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 包含文本提示和所需图像特征设置的正向条件数据。 | CONDITIONING | 是 | - |
| `negative` | 包含文本提示和不需要的图像特征设置的负向条件数据。 | CONDITIONING | 是 | - |
| `vae` | 用于将输入图像编码为潜在表示的 VAE 模型。 | VAE | 是 | - |
| `pixels` | 要处理并编码到潜在空间的输入图像。 | IMAGE | 是 | - |

**注意：** 输入图像会自动裁剪为宽度和高度均为 8 像素的倍数（向下取整），以确保与 VAE 编码过程兼容。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 附有编码图像潜在张量的正向条件数据。 | CONDITIONING |
| `negative` | 附有编码图像潜在张量的负向条件数据。 | CONDITIONING |
| `latent` | 与编码图像尺寸相同的零填充潜在张量。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/zh.md)

---
**Source fingerprint (SHA-256):** `e9a5a05cdeafe9337ca2033111f1ad4f7314fa33d71a4764f62919857efc79f4`
