# Recraft V4 文本转图像

此节点使用 Recraft V4 和 V4.1 AI 模型根据文本描述生成图像。它会将您的提示词发送到外部 API，并返回生成的图像。您可以通过指定模型、图像大小和要创建的图像数量来控制输出。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用于生成的模型。 | DYNAMIC_COMBO | 是 | `"recraftv4_1"`<br>`"recraftv4_1_utility"`<br>`"recraftv4_1_pro"`<br>`"recraftv4_1_utility_pro"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | 图像生成的提示词。最多 10,000 个字符。 | STRING | 是 | N/A |
| `negative_prompt` | 此输入会被忽略：Recraft V4 和 V4.1 模型不支持负面提示词。 | STRING | 是 | N/A |
| `n` | 要生成的图像数量（默认值：1）。 | INT | 是 | 1 到 6 |
| `seed` | 用于确定节点是否应重新运行的种子；无论种子取值如何，实际结果都是非确定性的（默认值：0）。 | INT | 是 | 0 到 18446744073709551615 |
| `recraft_controls` | 通过 Recraft Controls 节点对生成过程进行的可选附加控制。 | CUSTOM | 否 | N/A |

### recraftv4_1、recraftv4_1_utility 和 recraftv4 输入

由 `recraftv4_1`、`recraftv4_1_utility` 和 `recraftv4` 共用。

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `size` | 生成图像的大小（默认值："1024x1024"）。 | COMBO | 是 | 多个选项可用（标准 Recraft V4 尺寸，包含 "1024x1024"） |

### recraftv4_1_pro、recraftv4_1_utility_pro 和 recraftv4_pro 输入

由 `recraftv4_1_pro`、`recraftv4_1_utility_pro` 和 `recraftv4_pro` 共用。

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `size` | 生成图像的大小（默认值："2048x2048"）。 | COMBO | 是 | 多个选项可用（Pro 版 Recraft V4 尺寸，包含 "2048x2048"） |

**注意：** `size` 参数是动态输入，其可用选项会根据所选的 `model` 而变化。`seed` 值不保证图像输出可重现。如果您使用 Infinite Style Library 中的样式 ID，请确保它不是矢量艺术样式，因为这可能会返回 SVG 数据而不是图像。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `output` | 生成的图像或图像批次。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/zh.md)

---
**Source fingerprint (SHA-256):** `0b345a2f84d20a5a86681c358796a3ee3a5a101aab62441a978c610854e02c8a`
