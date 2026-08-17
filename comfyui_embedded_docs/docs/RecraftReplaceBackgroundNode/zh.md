# Recraft 更换背景

根据提供的提示词替换图像背景。此节点使用 Recraft API 根据您的文本描述为图像生成新背景，让您可以在保持主体不变的情况下彻底变换背景。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要处理的输入图像 | IMAGE | 是 | - |
| `prompt` | 图像生成提示词（默认：空） | STRING | 是 | - |
| `n` | 要生成的图像数量（默认：1） | INT | 是 | 1-6 |
| `seed` | 用于确定节点是否重新运行的种子；无论种子如何，实际结果都是不确定的（默认：0） | INT | 是 | 0-18446744073709551615 |
| `recraft_style` | 用于生成背景的可选样式。如果未提供，则默认为“realistic_image”样式 | STYLEV3 | 否 | - |
| `negative_prompt` | 对图像中不需要元素的可选文本描述（默认：空） | STRING | 否 | - |

**注意：** `seed` 参数控制节点何时重新执行，但由于外部 API 的性质，并不保证结果具有确定性。

**注意：** 输入批次中的每个图像都会单独处理；节点会为每个输入图像返回 `n` 个背景替换后的图像。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `IMAGE` | 生成的背景替换后的图像 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/zh.md)

---
**Source fingerprint (SHA-256):** `45a2607ae73cc67caa98d33bf536feda83a2021d960dec7cca76cbe0b9fc47ef`
