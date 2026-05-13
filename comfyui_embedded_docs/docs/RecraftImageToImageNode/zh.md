> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/zh.md)

此节点根据文本提示和强度参数修改现有图像。它使用 Recraft API 根据提供的描述转换输入图像，同时根据强度设置保持与原始图像的一定相似度。

## 输入

| 参数 | 数据类型 | 是否必填 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 待修改的输入图像 |
| `prompt` | STRING | 是 | - | 图像生成的提示词（默认值：""，最大长度：1000 个字符） |
| `n` | INT | 是 | 1-6 | 生成的图像数量（默认值：1） |
| `strength` | FLOAT | 是 | 0.0-1.0 | 定义与原始图像的差异程度，取值范围为 [0, 1]，其中 0 表示几乎相同，1 表示差异极大（默认值：0.5） |
| `seed` | INT | 是 | 0-18446744073709551615 | 用于确定节点是否应重新执行的种子；实际结果无论种子如何都是非确定性的（默认值：0） |
| `recraft_style` | STYLEV3 | 否 | - | 图像生成的可选样式选择。如果未提供，默认为 `realistic_image` |
| `negative_prompt` | STRING | 否 | - | 图像中不需要元素的可选文本描述（默认值：""） |
| `recraft_controls` | CONTROLS | 否 | - | 通过 Recraft Controls 节点对生成过程的可选额外控制 |

**注意：** `seed` 参数仅触发节点重新执行，但不能保证确定性结果。`strength` 参数在内部会四舍五入到小数点后两位。提示词会经过验证，且不得超过 1000 个字符。如果未提供 `recraft_style`，节点默认使用 `realistic_image` 样式。

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `image` | IMAGE | 基于输入图像和提示词生成的图像 |

---
**Source fingerprint (SHA-256):** `e47ab70e77186e62c253c976cdd7942cfb949ba6461914d2b4341f3eca8e14aa`
