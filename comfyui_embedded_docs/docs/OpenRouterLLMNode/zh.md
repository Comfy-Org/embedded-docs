# OpenRouter LLM

OpenRouter LLM 节点通过 OpenRouter 服务将文本提示（可选附带图像或视频）发送至一组精选的语言模型，并返回生成的文本响应。该节点支持来自 Anthropic (Claude)、OpenAI (GPT)、Google (Gemini)、xAI (Grok)、DeepSeek、Qwen、Mistral、Z.AI (GLM)、Moonshot (Kimi) 以及 Perplexity Sonar 的模型，并在所选模型支持时显示模型专属选项，例如推理努力程度和网页搜索上下文。

## 输入

`model` 选择器是动态的：选择一个模型将显示该模型专属的小部件（推理努力程度、网页搜索上下文、图像和视频插槽），以及以下通用输入。

### 通用输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用于生成响应的 OpenRouter 模型。选择模型后会显示其模型专属输入（请参阅下面的模型部分）。 | DYNAMIC_COMBO | 是 | 34 个精选的 OpenRouter 模型选项 |
| `prompt` | 输入给模型的文本。必须包含至少一个非空白字符。 | STRING | 是 | 多行文本 |
| `seed` | 采样种子。设置为 0 以省略。大多数模型仅将其作为提示。 (默认: 0) | INT | 是 | 0 到 2147483647 |
| `system_prompt` | 决定模型行为的基础指令。 (默认: "") | STRING | 否 | 多行文本 |

**关于 `seed` 的说明：** 此参数具有“生成后控制”行为，这意味着根据用户的小部件设置，它可以在每次节点执行后自动更改（例如，随机化、递增或固定）。

**关于 `system_prompt` 的说明：** 此参数为可选参数，并在用户界面中标记为高级参数。

### Anthropic Claude 输入

由 `anthropic/claude-opus-5`、`anthropic/claude-opus-4.8`、`anthropic/claude-opus-4.7`、`anthropic/claude-fable-5`、`anthropic/claude-sonnet-5` 和 `anthropic/claude-haiku-4.5` 共享。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理努力程度。'off' 完全禁用推理。 (默认: "off") | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

### OpenAI GPT 输入

由 `openai/gpt-5.6-sol-pro`、`openai/gpt-5.6-sol`、`openai/gpt-5.6-terra-pro`、`openai/gpt-5.6-terra`、`openai/gpt-5.6-luna-pro`、`openai/gpt-5.6-luna`、`openai/gpt-5.5-pro` 和 `openai/gpt-5.5` 共享。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理努力程度。'off' 完全禁用推理。 (默认: "off") | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

### Google Gemini 3.5 Flash 输入

适用于 `google/gemini-3.5-flash`。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理努力程度。'off' 完全禁用推理。 (默认: "off") | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

### xAI Grok 输入

由 `x-ai/grok-4.5`、`x-ai/grok-4.20` 和 `x-ai/grok-4.3` 共享。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理努力程度。'off' 完全禁用推理。 (默认: "off") | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

### DeepSeek 输入

由 `deepseek/deepseek-v4-pro`、`deepseek/deepseek-v4-flash` 和 `deepseek/deepseek-v3.2` 共享。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理努力程度。'off' 完全禁用推理。 (默认: "off") | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

### Qwen 3.6 Plus 和 Flash 输入

由 `qwen/qwen3.6-plus` 和 `qwen/qwen3.6-flash` 共享。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理努力程度。'off' 完全禁用推理。 (默认: "off") | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

### Mistral Large 2512 输入

适用于 `mistralai/mistral-large-2512`。该模型不添加任何模型专属参数小部件；仅适用通用输入和 `images` 参考插槽。

### Mistral Medium 3.5 输入

适用于 `mistralai/mistral-medium-3-5`。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理努力程度。'off' 完全禁用推理。 (默认: "off") | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

### Moonshot Kimi K3 和 K2.6 输入

由 `moonshotai/kimi-k3` 和 `moonshotai/kimi-k2.6` 共享。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理努力程度。'off' 完全禁用推理。 (默认: "off") | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

### Perplexity Sonar Pro 输入

适用于 `perplexity/sonar-pro`。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | 要检索的网页搜索上下文量。越大 = 越有依据，但速度越慢/价格越贵。 (默认: "medium") | COMBO | 否 | "low"<br>"medium"<br>"high" |

### Perplexity Sonar Reasoning Pro 和 Deep Research 输入

由 `perplexity/sonar-reasoning-pro` 和 `perplexity/sonar-deep-research` 共享。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | 要检索的网页搜索上下文量。越大 = 越有依据，但速度越慢/价格越贵。 (默认: "medium") | COMBO | 否 | "low"<br>"medium"<br>"high" |
| `reasoning_effort` | 推理努力程度。'off' 完全禁用推理。 (默认: "off") | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

### 仅推理模型

由 `qwen/qwen3.6-max-preview`、`z-ai/glm-4.6`、`z-ai/glm-5` 和 `moonshotai/kimi-k2-thinking` 共享。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理努力程度。'off' 完全禁用推理。 (默认: "off") | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

### 参考输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `images` | 可选的参考图像 — 以 URL 形式发送。可增长插槽：连接 `image_1` 至 `image_N`，其中 N 取决于所选模型。 | IMAGE | 否 | 0 至 N 张图像（N = 8、10 或 20，取决于模型） |
| `videos` | 可选的参考视频 — 以 URL 形式发送。可增长插槽：连接 `video_1` 至 `video_N`。仅在支持视频的模型上可用。 | VIDEO | 否 | 0 至 4 个视频 |

**关于模型能力和限制的说明：**

- 图像支持：Anthropic Claude、OpenAI GPT、Google Gemini 3.5 Flash 和 xAI Grok 模型最多支持 20 张图像；Qwen 3.6 Plus/Flash 和 Moonshot Kimi K3/K2.6 最多支持 10 张图像；Mistral Large 2512 和 Mistral Medium 3.5 最多支持 8 张图像。DeepSeek、Qwen 3.6 Max Preview、Z.AI GLM、Moonshot Kimi K2 Thinking 和 Perplexity Sonar 模型不接受图像。
- 视频支持：只有 `google/gemini-3.5-flash`、`qwen/qwen3.6-plus` 和 `qwen/qwen3.6-flash` 接受视频，最多 4 个视频。
- 如果连接的图像或视频数量超过所选模型的支持范围，节点将引发错误。
- 当 `reasoning_effort` 设置为 "low"、"medium" 或 "high" 时，模型会在内部进行推理，但不会返回推理轨迹；"off" 则完全禁用推理。
- `search_context_size` 小部件仅对 Perplexity Sonar 模型显示。`reasoning_effort` 和 `search_context_size` 小部件被标记为高级参数。
- 节点会根据所选模型显示一个近似价格徽章（每 1K Token 的美元价格）。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `output` | 所选 OpenRouter 模型生成的文本响应。 | STRING |

**关于错误的说明：** 如果 OpenRouter 返回 API 错误、空响应（无 choices）或模型的拒绝答复，节点将引发错误。

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterLLMNode/zh.md)

---
**Source fingerprint (SHA-256):** `534ab9ecc12e35a23a4d8f3e10f4f82d95db8e902ac8a2f2ee0ea68246516f62`
