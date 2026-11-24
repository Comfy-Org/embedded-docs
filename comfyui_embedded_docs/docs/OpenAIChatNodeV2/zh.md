# OpenAI ChatGPT

此节点使用 OpenAI 的 GPT 模型生成文本回复。它发送文本提示词，并可选地将图像或文件作为上下文，然后以字符串形式返回答案。所有设置都位于 `model` 选择器内：选择某个模型后，会显示该模型自身的 `reasoning_effort` 级别、token 上限、种子和系统提示词，因此无需单独的配置节点。此节点取代了早期的 OpenAI ChatGPT 节点，源代码现在将该节点标记为已弃用。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用于生成回复的模型。每个模型会提供其支持的 `reasoning_effort` 级别（默认：`"gpt-6.2-sol"`）。 | DYNAMIC_COMBO | 是 | `"gpt-6.2-sol"`<br>`"gpt-6.2-astra"`<br>`"gpt-6-astra"`<br>`"gpt-6.1-sol"`<br>`"gpt-6.1-terra"`<br>`"gpt-6-sol"`<br>`"gpt-6-luna"`<br>`"gpt-5.6-sol"`<br>`"gpt-5.6-terra"`<br>`"gpt-5.6-luna"`<br>`"gpt-5.5-pro"`<br>`"gpt-5.5"` |
| `prompt` | 输入给模型的文本（默认：空字符串）。 | STRING | 是 | - |
| `images` | 可增长槽位：连接 1..16 个项（`image_1`、`image_2`……）。可选，用作模型上下文的图像。 | IMAGE | 否 | 0 到 16 张图像 |
| `files` | 可选，用作模型上下文的文件。接受来自 OpenAI ChatGPT Input Files 节点的输入。 | OPENAI_INPUT_FILES | 否 | - |
| `reasoning_effort` | 模型在回答前进行推理的程度。级别越高，使用的 token 越多，耗时也越长。可用的级别取决于所选模型（默认：`"medium"`，`gpt-5.5-pro` 默认为 `"high"`）。 | COMBO | 是 | 见下方各模型列表 |
| `max_output_tokens` | 生成的最大 token 数，包含推理 token。如果该值过低而 `reasoning_effort` 较高，可能没有剩余空间留给答案（默认：32768）。 | INT | 是 | 16 到 128000 |
| `seed` | 种子控制节点是否应重新运行；无论种子为何，结果都是非确定性的（默认：42）。 | INT | 是 | 0 到 2147483647 |
| `system_prompt` | 规定模型行为的基础指令（默认：空字符串）。 | STRING | 否 | - |

### 各模型的推理强度级别

- `gpt-6.2-sol`、`gpt-6.2-astra`、`gpt-6-astra`、`gpt-6.1-sol`：`"low"`、`"medium"`、`"high"`、`"xhigh"`、`"max"`，默认 `"medium"`。
- `gpt-6.1-terra`、`gpt-6-sol`、`gpt-6-luna`、`gpt-5.6-sol`、`gpt-5.6-terra`、`gpt-5.6-luna`：`"none"`、`"low"`、`"medium"`、`"high"`、`"xhigh"`、`"max"`，默认 `"medium"`。
- `gpt-5.5-pro`：`"medium"`、`"high"`、`"xhigh"`，默认 `"high"`。
- `gpt-5.5`：`"none"`、`"low"`、`"medium"`、`"high"`、`"xhigh"`，默认 `"medium"`。

### 行为说明

- 仅返回答案文本。模型在思考的评论阶段输出的消息会被跳过。
- 如果在答案写出之前 token 预算耗尽，节点会报错并提示增大 `max_output_tokens`。
- 图像按其自身分辨率并以 API 的自动细节级别发送，因此大图像会消耗更多 token。
- 每个请求都会存储在 OpenAI 一侧，返回的文本会用换行符将答案各部分拼接起来。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `output` | OpenAI 模型生成的文本回复。 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNodeV2/zh.md)

---
**Source fingerprint (SHA-256):** `129c13a6c7b76d142c0a23234ab5e707a1dd39a99055974277d46a39593aa7ba`
