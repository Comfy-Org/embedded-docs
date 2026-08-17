# TextEncodeZImageOmni

TextEncodeZImageOmni 节点是一个高级 conditioning 节点，它将文本提示词与可选的参考图像一起编码为适合图像生成模型的 conditioning 格式。该节点最多可处理三张图像，并可选择使用视觉编码器和/或 VAE 对其进行编码以生成参考 latents，然后通过特定的模板结构将这些视觉参考与文本提示词整合在一起。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `clip` | 用于对文本提示词进行分词和编码的 CLIP 模型。 | CLIP | 是 |  |
| `image_encoder` | 可选的视觉编码器模型。如果提供，它将用于对输入图像进行编码，生成的嵌入将添加到 conditioning 中。 | CLIPVision | 否 |  |
| `prompt` | 要编码的文本提示词。此字段支持多行输入和动态提示词。 | STRING | 是 |  |
| `auto_resize_images` | 启用时（默认：True），输入图像将根据其像素面积自动调整大小，然后再传递给 VAE 进行编码。这是一个高级设置。 | BOOLEAN | 否 |  |
| `vae` | 可选的 VAE 模型。如果提供，它将用于将输入图像编码为 latent 表示，并作为参考 latents 添加到 conditioning 中。 | VAE | 否 |  |
| `image1` | 第一张可选的参考图像。 | IMAGE | 否 |  |
| `image2` | 第二张可选的参考图像。 | IMAGE | 否 |  |
| `image3` | 第三张可选的参考图像。 | IMAGE | 否 |  |

**注意：** 该节点最多接受三张图像（`image1`、`image2`、`image3`）。只有在至少提供一张图像时，`image_encoder` 和 `vae` 输入才会被使用。当 `auto_resize_images` 为 True 且连接了 `vae` 时，图像会被调整为总像素面积接近 1024x1024 像素，并且尺寸圆整到 8 的倍数，然后再进行编码。如果未提供任何图像，该节点将仅编码文本提示词，不包含任何视觉参考。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `CONDITIONING` | 最终的 conditioning 输出，包含编码后的文本提示词，如果提供了图像，还可能包含编码后的图像嵌入和/或参考 latents。 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeZImageOmni/zh.md)

---
**Source fingerprint (SHA-256):** `b40a3150f536b6f37e2b53e6d9992fcb4fd32dceb540c0a76773a7ba1af9a7b8`
