# Grok 图像

Grok Image 节点根据文本提示，使用 Grok AI 图像模型生成一张或多张图像。它会将提示和设置发送到外部服务，并将生成的图像作为张量返回，以供工作流中的其他部分使用。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用于图像生成的具体 Grok 模型。不同模型可能在质量、速度或功能上有所不同。 | COMBO | 是 | `"grok-imagine-image-2.0"`<br>`"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `prompt` | 用于生成图像的文本提示。该描述用于引导 AI 生成相应内容。必须至少包含 1 个非空白字符。 | STRING | 是 | N/A |
| `aspect_ratio` | 生成图像所需的宽高比。 | COMBO | 是 | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |
| `number_of_images` | 要生成的图像数量（默认值：1）。 | INT | 是 | 1 to 10 |
| `seed` | 用于决定节点是否应重新运行的种子；无论种子如何，实际结果都是不确定的（默认值：0）。 | INT | 是 | 0 to 2147483647 |
| `resolution` | 生成图像所需的输出分辨率（默认值："1K"）。 | COMBO | 否 | `"1K"`<br>`"2K"` |
| `quality` | 质量级别，仅由 grok-imagine-image-2.0 模型支持（默认值："medium"）。 | COMBO | 否 | 提供多个选项 |

**注意：** `quality` 参数仅在 `model` 设置为 "grok-imagine-image-2.0" 时生效。对于所有其他模型，此设置会被忽略。

**注意：** `seed` 参数主要用于控制节点在工作流中的重新执行时机。由于外部 AI 服务的特性，即使使用相同的种子，生成的图像在不同运行之间也无法复现。

**定价说明：** 生成图像的费用取决于所选的 `model`、`resolution`、`quality` 和 `number_of_images`；总价为单张图像费率乘以 `number_of_images`。对于 "grok-imagine-image-2.0" 模型，使用 "low" 质量时，"1K" 分辨率下每张图像费率为 $0.04，"2K" 分辨率下为 $0.06；使用其他质量级别时，"1K" 分辨率下为 $0.06，"2K" 分辨率下为 $0.08。"grok-imagine-image-quality" 模型在 "1K" 分辨率下每张图像费用为 $0.05，在 "2K" 分辨率下为 $0.07。"grok-imagine-image-pro" 模型每张图像费用为 $0.07。其他模型每张图像费用为 $0.02。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `output` | 生成的单个图像或一批图像。如果 `number_of_images` 为 1，则返回单个图像张量；如果大于 1，则返回一批图像张量。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageNode/zh.md)

---
**Source fingerprint (SHA-256):** `a89f5df0d4827f45013f1af92541d36b5b8c8edc8626e07af4fe2d85ee5486e7`
