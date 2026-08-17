# Recraft V4 文本转矢量

Recraft V4 Text to Vector 节点根据文本描述生成可缩放矢量图形（SVG）图像。它连接外部 API，使用 Recraft V4 和 V4.1 模型生成图像。该节点根据您的提示词输出一个或多个 SVG 图像。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用于生成的模型。选择模型会更改可用的 `size` 选项。 | DYNAMIC_COMBO | 是 | `"recraftv4_1_vector"`<br>`"recraftv4_1_utility_vector"`<br>`"recraftv4_1_pro_vector"`<br>`"recraftv4_1_utility_pro_vector"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | 图像生成的提示词。最多 10,000 个字符。 | STRING | 是 | N/A |
| `negative_prompt` | 此输入会被忽略：Recraft V4 和 V4.1 模型不支持负面提示词。 | STRING | 是 | N/A |
| `n` | 要生成的图像数量（默认值：1）。 | INT | 是 | 1 到 6 |
| `seed` | 用于确定节点是否应重新运行的种子；无论种子如何，实际结果都是非确定性的（默认值：0）。 | INT | 是 | 0 到 18446744073709551615 |
| `recraft_controls` | 通过 Recraft Controls 节点对生成过程的可选附加控制。 | CUSTOM | 否 | N/A |

### recraftv4_1_vector、recraftv4_1_utility_vector 和 recraftv4 输入

这三个模型共享相同的 `size` 选项。

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `size` | 生成图像的尺寸（默认值：`"1024x1024"`）。 | COMBO | 是 | `"1024x1024"`<br>`"1152x896"`<br>`"896x1152"`<br>`"1216x832"`<br>`"832x1216"`<br>`"1344x768"`<br>`"768x1344"`<br>`"1536x640"`<br>`"640x1536"` |

### recraftv4_1_pro_vector、recraftv4_1_utility_pro_vector 和 recraftv4_pro 输入

这三个模型共享相同的 `size` 选项。

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `size` | 生成图像的尺寸（默认值：`"2048x2048"`）。 | COMBO | 是 | `"2048x2048"`<br>`"2304x1792"`<br>`"1792x2304"`<br>`"2432x1664"`<br>`"1664x2432"`<br>`"2688x1536"`<br>`"1536x2688"`<br>`"3072x1280"`<br>`"1280x3072"` |

**注意：** `size` 参数是一个动态输入，其可用选项会根据所选的 `model` 而变化。`seed` 值不保证外部 API 能重现相同结果。`negative_prompt` 输入会被忽略，因为 Recraft V4 和 V4.1 模型不支持负面提示词。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `output` | 生成的可缩放矢量图形（SVG）图像。 | SVG |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/zh.md)

---
**Source fingerprint (SHA-256):** `822f6b9fef67ef6beb1eba099c41c72570a1f79e316612201c81f6e5eb91408d`
