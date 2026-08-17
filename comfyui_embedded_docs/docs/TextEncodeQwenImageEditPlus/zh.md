# 文本编码（QwenImageEditPlus）

TextEncodeQwenImageEditPlus 节点处理文本提示和可选图像，为图像生成或编辑任务生成 conditioning 数据。它使用专门的模板来分析输入图像，并理解文本指令应如何修改图像，然后将此信息编码以供后续生成步骤使用。该节点最多可处理三张输入图像，并在提供 VAE 时可选地生成参考 latent。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `clip` | 用于分词和编码的 CLIP 模型 | CLIP | 是 | - |
| `prompt` | 描述所需图像修改的文本指令（支持多行输入和动态提示） | STRING | 是 | - |
| `vae` | 可选的 VAE 模型，用于从输入图像生成参考 latent | VAE | 否 | - |
| `image1` | 用于分析和修改的第一个可选输入图像 | IMAGE | 否 | - |
| `image2` | 用于分析和修改的第二个可选输入图像 | IMAGE | 否 | - |
| `image3` | 用于分析和修改的第三个可选输入图像 | IMAGE | 否 | - |

**注意：** 当提供 VAE 时，节点会从所有输入图像生成参考 latent。该节点可同时处理最多三张图像。图像会自动缩放至约 384×384 像素的目标区域（保持宽高比）以进行视觉-语言处理，并缩放至约 1024×1024 像素且尺寸可被 8 整除的目标区域以进行 VAE 编码。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `CONDITIONING` | 编码后的 conditioning 数据，包含文本令牌和可选的参考 latent，用于图像生成 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/zh.md)

---
**Source fingerprint (SHA-256):** `5eea53a84045924b44d445244e6149b341188d22573aaaced87bac8a139dac96`
