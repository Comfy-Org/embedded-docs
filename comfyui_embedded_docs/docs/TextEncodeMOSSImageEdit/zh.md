# Text Encode MOSS-Image Edit

将编辑指令与参考图像一起编码为用于 MOSS-Image 编辑 LoRA 的 conditioning。将输出连接为正向 conditioning，并使用相同的参考图像再运行一个实例以生成负向 conditioning。参考图像会按其到达时的尺寸使用，因此在连接前请先进行缩放。此节点在 ComfyUI 中标记为实验性。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `clip` | 用于对指令进行分词并编码的 CLIP 模型。 | CLIP | 是 | - |
| `prompt` | 描述编辑操作的指令。支持多行文本和动态提示词。 | STRING | 是 | 任意文本 |
| `vae` | 用于将参考图像编码为参考 latent 的 VAE。 | VAE | 是 | - |
| `edit_format` | 编辑 LoRA 训练时使用的布局。它决定采用哪种参考 latent 方法，以及文本编码器是否也能看到参考图像。 | COMBO | 是 | `"ai-toolkit"`<br>`"ai-toolkit (kv_cache off)"`<br>`"Moss-Image-Edit"` |
| `images` | 可增长槽位：连接一张或多张参考图像（`image_1`、`image_2`……）。每张图像都按其到达时的尺寸使用，其 alpha 通道会被丢弃，并通过 VAE 编码为参考 latent。 | IMAGE | 是 | 1 张或多张图像 |

**注意：** 使用 `"ai-toolkit"` 和 `"ai-toolkit (kv_cache off)"` 时，文本编码器也会看到每一张参考图像，这些图像会被缩小到最大 384x384 像素，并在提示词中前置一个 `Picture N:` 标记，因此指令可以通过编号来引用它们。使用 `"Moss-Image-Edit"` 时，参考图像仅以参考 latent 的形式进入模型，文本编码器只会看到指令本身。此外，`"ai-toolkit (kv_cache off)"` 会让参考图像持续关注正在生成的图像，因此它们会在每个采样步骤中重新计算。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `conditioning` | 编码后的指令，附带参考 latent 以及相匹配的参考 latent 方法。 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMOSSImageEdit/zh.md)

---
**Source fingerprint (SHA-256):** `30e4edbb129f647cdce4ec95f78c002ecdc9a4f8fc5a45f1477fdc555b541dae`
