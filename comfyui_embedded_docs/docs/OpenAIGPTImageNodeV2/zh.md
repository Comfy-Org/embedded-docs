# OpenAI GPT 图像 2

此节点使用 OpenAI 的 GPT Image API 生成图像。它支持多种 GPT Image 模型、用于编辑的可选参考图像，以及用于局部重绘（inpainting）的可选蒙版。当提供参考图像时，节点会向 API 发送编辑请求；否则发送普通的生成请求。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要使用的 OpenAI GPT Image 模型。选择模型后会显示该模型特有的其他参数。 | DYNAMIC_COMBO | 是 | `"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` |
| `prompt` | GPT Image 的文本提示（默认：""）。 | STRING | 是 | 不适用 |
| `n` | 生成图像的数量（默认：1）。 | INT | 是 | 1 到 8 |
| `seed` | 用于可复现性的种子（默认：0）。尚未在后端实现。 | INT | 是 | 0 到 2147483647 |

### gpt-image-2 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model.size` | 图像尺寸。选择 "Custom" 可使用自定义宽度和高度（默认："auto"）。 | COMBO | 是 | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | 仅当 `size` 为 "Custom" 时使用。必须是 16 的倍数（默认：1024）。 | INT | 否 | 1024 到 3840 |
| `model.custom_height` | 仅当 `size` 为 "Custom" 时使用。必须是 16 的倍数（默认：1024）。 | INT | 否 | 1024 到 3840 |
| `model.background` | 返回带背景或不带背景的图像（默认："auto"）。 | COMBO | 是 | `"auto"`<br>`"opaque"` |
| `model.quality` | 图像质量，影响成本和生成时间（默认："low"）。 | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"` |

### gpt-image-1.5 和 gpt-image-1 输入

这两个模型共享同一组模型特有参数。

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model.size` | 图像尺寸（默认："auto"）。 | COMBO | 是 | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `model.background` | 返回带背景或不带背景的图像（默认："auto"）。 | COMBO | 是 | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | 图像质量，影响成本和生成时间（默认："low"）。 | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"` |

### 参考输入

这些输入适用于所有模型。

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model.images` | 用于图像编辑的可选参考图像。可增长插槽：最多连接 16 张图像（`image_1` 到 `image_16`）。 | IMAGE | 否 | 0 到 16 张图像 |
| `model.mask` | 用于局部重绘的可选蒙版（白色区域将被替换）。需要恰好一张参考图像。 | MASK | 否 | 不适用 |

**参数约束与限制：**

- 当 `model.size` 为 "Custom"（仅限 gpt-image-2）时，`model.custom_width` 和 `model.custom_height` 必须是 16 的倍数，最长边不得超过 3840 像素，宽高比不得超过 3:1，总像素数必须在 655,360 到 8,294,400 之间。
- 蒙版需要恰好一张参考图像。没有输入图像时不能使用蒙版，也不能与多张输入图像同时使用。
- 提供蒙版时，蒙版的高度和宽度必须与输入图像的高度和宽度一致。
- 参考图像在发送到 API 之前会被缩小到最大 2048 x 2048 总像素。
- `seed` 参数尚未在后端实现。
- 如果 API 在单个响应中返回不同尺寸的图像，所有图像都会调整大小以匹配第一张图像的尺寸。

## 输出

| 输出名 | 描述 | 数据类型 |
| --- | --- | --- |
| `image` | 生成的图像（单张或多张），堆叠为形状为 (N, H, W, C) 的单一批次张量。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/zh.md)

---
**Source fingerprint (SHA-256):** `fb3491f949151fbd3f5825ec9f9ae124019767d083f56966ef34af278aef50c0`
