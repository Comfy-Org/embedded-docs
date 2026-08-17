# Anthropic Claude

从 Anthropic Claude 模型生成文本响应。此节点将文本提示和可选图像发送到 Claude 模型，并返回生成的文本响应。

## 输入

`model` 参数是一个动态选择器：当您选择模型时，下方会显示额外的模型特定设置，例如 token 限制、温度和推理强度。

### 通用输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 输入给模型的文本。去除首尾空白后必须为非空字符串。（默认：空字符串） | STRING | 是 | N/A |
| `model` | 用于生成响应的 Claude 模型。 | DYNAMIC_COMBO | 是 | `"Opus 5"`<br>`"Opus 4.8"`<br>`"Fable 5"`<br>`"Sonnet 5"`<br>`"Opus 4.7"`<br>`"Opus 4.6"`<br>`"Sonnet 4.6"`<br>`"Sonnet 4.5"`<br>`"Haiku 4.5"` |
| `seed` | `seed` 控制节点是否应重新运行；无论 `seed` 为何，结果都是非确定性的。（默认：0） | INT | 是 | 0 to 2147483647 |
| `images` | 可选的图像（一张或多张），用作模型的上下文。可扩展插槽：可连接 `image_1` 至 `image_20`，最多 20 张图像。（默认：无） | IMAGE | 否 | 0 to 20 images |
| `system_prompt` | 规定模型行为的基础指令。（默认：空字符串） | STRING | 否 | N/A |

### Opus 5 和 Fable 5 输入

由 Opus 5 和 Fable 5 共用。这些模型始终使用扩展思考，且不提供温度设置。

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | 要生成的最大 token 数（启用时包含推理 token）。（默认：32768） | INT | 是 | 4096 to 64000 |
| `reasoning_effort` | 扩展思考强度。此模型始终启用推理。（默认："high"） | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"` |

### Opus 4.8 和 Sonnet 5 输入

由 Opus 4.8 和 Sonnet 5 共用。这些模型不提供温度设置。

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | 要生成的最大 token 数（启用时包含推理 token）。（默认：32768） | INT | 是 | 4096 to 64000 |
| `reasoning_effort` | 扩展思考强度。设为 "off" 可禁用推理。（默认："off"） | COMBO | 是 | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

### Opus 4.7、Opus 4.6、Sonnet 4.6 和 Sonnet 4.5 输入

由 Opus 4.7、Opus 4.6、Sonnet 4.6 和 Sonnet 4.5 共用。对于 Opus 4.7，温度输入会显示但会被忽略，API 使用默认值 1.0。

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | 要生成的最大 token 数（启用时包含推理 token）。（默认：32768） | INT | 是 | 4096 to 64000 |
| `temperature` | 控制随机性。0.0 为确定性输出，1.0 为最大随机性。当 `reasoning_effort` 设置为 "off" 以外的值时，对于 Opus 4.7 和任何模型，此参数都会被忽略。（默认：1.0） | FLOAT | 是 | 0.0 to 1.0 (step 0.01) |
| `reasoning_effort` | 扩展思考强度。设为 "off" 可禁用推理。（默认："off"） | COMBO | 是 | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

### Haiku 4.5 输入

此模型不支持扩展思考，因此没有可用的 `reasoning_effort` 设置。

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | 要生成的最大 token 数（启用时包含推理 token）。（默认：32768） | INT | 是 | 4096 to 64000 |
| `temperature` | 控制随机性。0.0 为确定性输出，1.0 为最大随机性。（默认：1.0） | FLOAT | 是 | 0.0 to 1.0 (step 0.01) |

### 参数约束

- 每个请求最多可提供 20 张图像。上传图像的总像素数限制为 1568 × 1568 像素。
- Opus 5、Fable 5、Opus 4.8 和 Sonnet 5 无法配置温度。当存在温度输入时，对于 Opus 4.7 以及任何 `reasoning_effort` 设置为 "off" 以外值的模型，该输入都会被忽略。
- Opus 5 和 Fable 5 始终启用推理，因此这些模型的 `reasoning_effort` 选项不包含 "off"。Haiku 4.5 模型不支持扩展思考，因此没有 `reasoning_effort` 设置。
- 如果 Claude 出于安全原因拒绝回答请求，节点会引发错误而不是返回文本。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `output` | Claude 模型生成的文本响应。如果未生成可见文本，则输出为 `"Empty response from Claude model."`。思考块或推理块不包含在输出中。 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/zh.md)

---
**Source fingerprint (SHA-256):** `b0381e7981e5886d66b6976c7ddcad3f142bdd803271a6ac8567293dcddaa98a`
