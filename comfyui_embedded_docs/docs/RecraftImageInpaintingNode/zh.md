# Recraft 图像修复

此节点根据文本提示词和蒙版修改图像的特定区域。它使用 Recraft API 智能编辑仅蒙版区域，同时保持图像的其余部分不变。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要修改的输入图像 | IMAGE | 是 | - |
| `mask` | 定义图像中哪些区域需要修改的蒙版 | MASK | 是 | - |
| `prompt` | 图像生成的提示词（默认：空字符串，最大长度：1000 个字符） | STRING | 是 | - |
| `n` | 要生成的图像数量（默认：1，最小值：1，最大值：6） | INT | 是 | 1-6 |
| `seed` | 用于决定节点是否重新运行的种子；无论种子如何，实际结果都是非确定性的（默认：0） | INT | 是 | 0-18446744073709551615 |
| `recraft_style` | Recraft API 的可选样式参数。如果未提供，默认为 "realistic_image" 样式 | STYLEV3 | 否 | - |
| `negative_prompt` | 关于图像中不需要元素的可选文本描述（默认：空字符串） | STRING | 否 | - |

*注意：`image` 和 `mask` 必须同时提供，修复（inpainting）操作才能正常工作。蒙版将自动调整大小以匹配图像尺寸。`prompt` 会经过验证，且最大长度为 1000 个字符。如果使用了 Infinite Style Library 中的 `style_id`，请确保它不是矢量艺术风格，因为这可能导致 API 返回 SVG 数据而非图像。*

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `image` | 根据提示词和蒙版生成的修改后图像。每个输入图像按 `n` 参数的数量返回图像 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageInpaintingNode/zh.md)

---
**Source fingerprint (SHA-256):** `539a49aec582f529a13059388222c3998e22d52618738843d9b2b6e0fb1ea5c3`
