# Recraft 图像到图像

此节点根据文本提示和强度参数修改现有图像。它使用 Recraft API 根据提供的描述对输入图像进行变换，同时根据强度设置保持与原始图像的一定相似度。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要修改的输入图像 | IMAGE | 是 | - |
| `prompt` | 图像生成的提示词（默认：""，最大长度：1000 个字符） | STRING | 是 | - |
| `n` | 要生成的图像数量（默认：1） | INT | 是 | 1-6 |
| `strength` | 定义与原始图像的差异程度，应在 [0, 1] 范围内，其中 0 表示几乎相同，1 表示相似度极低（默认：0.5） | FLOAT | 是 | 0.0-1.0 |
| `seed` | 用于决定节点是否重新执行的种子；无论种子如何，实际结果都是非确定性的（默认：0） | INT | 是 | 0-18446744073709551615 |
| `recraft_style` | 可选的图像生成样式选择。如果未提供，默认为 `realistic_image` | STYLEV3 | 否 | - |
| `negative_prompt` | 对图像中不需要元素的可选文本描述（默认：""） | STRING | 否 | - |
| `recraft_controls` | 通过 Recraft Controls 节点对生成过程进行的可选额外控制 | CONTROLS | 否 | - |

**注意：** `seed` 参数仅触发节点重新执行，但并不能保证确定性结果。强度参数在内部会四舍五入到 2 位小数。提示词会经过验证，且不得超过 1000 个字符。如果未提供 `recraft_style`，节点将默认为 `realistic_image` 样式。如果您使用来自 Infinite Style Library 的 `style_id`，请确保它不是矢量艺术样式，因为这可能导致节点接收 SVG 数据而非图像，从而引发错误。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `image` | 根据输入图像和提示词生成的图像。对于每张输入图像，会生成 `n` 张图像，因此总输出数量等于输入数量乘以 `n`。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/zh.md)

---
**Source fingerprint (SHA-256):** `1932e55d1dc392e6bd42a0bd29f5aaba44b65997b597648a927fba38a27c90ad`
