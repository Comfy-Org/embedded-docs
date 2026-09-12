# Bria 生成式填充

此节点使用 Bria 在图像的蒙版区域内生成对象或场景。它会上传图像和蒙版，将提示发送至 Bria 生成式填充服务，等待操作完成，并返回编辑后的图像。这是一项付费 API 操作（每次请求 US$0.0429）。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要编辑的输入图像。 | IMAGE | 是 | - |
| `mask` | 白色区域将填充生成内容，黑色区域将保留。发送前会对蒙版进行二值化处理，因此部分涂绘的区域会被视为白色。必须与图像具有相同的宽高比。 | MASK | 是 | - |
| `prompt` | 描述要在蒙版区域内生成的内容。必须至少包含 1 个字符。（默认值：""） | STRING | 是 | - |
| `negative_prompt` | 描述生成结果中要避免的内容的提示。如果留空，则不会发送到 API。（默认值：""） | STRING | 是 | - |
| `refine_prompt` | 自动调整提示以获得更好的结果；禁用后则完全按所写内容使用提示。（默认值：true） | BOOLEAN | 是 | true<br>false |
| `seed` | 生成过程使用的种子。（默认值：42） | INT | 是 | 1 to 2147483647 |
| `内容审核` | 审核设置。设置为 "true" 时，将应用下方的审核选项。（默认值："false"） | DYNAMIC_COMBO | 是 | "false"<br>"true" |

### 审核输入（当 `moderation` = "true" 时）

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt_content_moderation` | 对提示应用内容审核。（默认值：false） | BOOLEAN | 否 | true<br>false |
| `visual_input_moderation` | 对输入图像应用内容审核。（默认值：false） | BOOLEAN | 否 | true<br>false |
| `visual_output_moderation` | 对输出图像应用内容审核。（默认值：false） | BOOLEAN | 否 | true<br>false |

**注意：** `prompt` 不能为空。`mask` 必须与 `image` 具有相同的宽高比。蒙版会按 50% 不透明度进行二值化，因此以低于一半不透明度涂绘的区域将被忽略；如果二值化后蒙版不包含任何白色区域，节点将报错。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `image` | 生成的图像，其中蒙版区域已由生成内容填充。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGenFill/zh.md)

---
**Source fingerprint (SHA-256):** `b23e29d4457f859181d68eaeb4b0238de28f4b18932d68438fa2954739cdc66a`
