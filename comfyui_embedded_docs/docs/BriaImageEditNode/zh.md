# Bria FIBO 图像编辑

Bria FIBO Image Edit 节点允许你通过文本指令修改现有图像。它会将图像和你的提示词发送到 Bria API，API 会使用 FIBO 模型根据你的请求生成新的、经过编辑的图像版本。你还可以提供遮罩（mask），将编辑限制在特定区域内。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用于图像编辑的模型版本。 | COMBO | 是 | `"FIBO"` |
| `image` | 要编辑的输入图像。 | IMAGE | 是 | - |
| `prompt` | 编辑图像的指令（默认：空）。 | STRING | 是 | - |
| `negative_prompt` | 描述你不想在编辑后图像中出现的文本（默认：空）。 | STRING | 是 | - |
| `structured_prompt` | 包含 JSON 格式的结构化编辑提示词的字符串。需要精确、可编程地控制编辑时，可使用此参数代替常规提示词（默认：空）。 | STRING | 是 | - |
| `seed` | 用于初始化随机生成的数字，确保结果可复现（默认：1）。 | INT | 是 | 1 到 2147483647 |
| `guidance_scale` | 数值越高，图像越贴近提示词（默认：3.0）。 | FLOAT | 是 | 3.0 到 5.0 |
| `steps` | 模型将执行的去噪步数（默认：50）。 | INT | 是 | 20 到 50 |
| `moderation` | 审核设置。选择 `"true"` 会显示针对提示词内容、视觉输入和视觉输出的额外审核选项。 | DYNAMICCOMBO | 是 | `"false"`<br>`"true"` |
| `mask` | 如果省略，编辑将应用于整个图像。 | MASK | 否 | - |

**重要限制：**

- 你必须至少提供 `prompt` 和 `structured_prompt` 中的一个输入。两者不能同时为空。
- 当 `moderation` 参数设置为 `"true"` 时，会出现三个额外的布尔输入：`prompt_content_moderation`（默认：false）、`visual_input_moderation`（默认：false）和 `visual_output_moderation`（默认：true）。

## 输出

| 输出名 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `IMAGE` | Bria API 返回的编辑后图像。 | IMAGE |
| `structured_prompt` | 编辑过程中使用或生成的结构化提示词。 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/zh.md)

---
**Source fingerprint (SHA-256):** `e66aaa563a82407408f25b289011a491c8b158822fc2db8912daf73731750081`
