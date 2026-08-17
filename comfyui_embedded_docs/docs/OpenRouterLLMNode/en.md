# OpenRouter LLM

The OpenRouter LLM node sends a text prompt (and optionally images or videos) to a curated set of language models available through the OpenRouter service and returns the generated text response. It supports models from Anthropic (Claude), OpenAI (GPT), Google (Gemini), xAI (Grok), DeepSeek, Qwen, Mistral, Z.AI (GLM), Moonshot (Kimi), and Perplexity Sonar, and shows model-specific options such as reasoning effort and web search context when the selected model supports them.

## Inputs

The `model` selector is dynamic: choosing a model reveals model-specific widgets (reasoning effort, web search context, image and video slots) in addition to the common inputs below.

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | The OpenRouter model used to generate the response. Selecting a model reveals its model-specific inputs (see the model sections below). | DYNAMIC_COMBO | Yes | 34 curated OpenRouter model options |
| `prompt` | Text input to the model. Must contain at least one non-whitespace character. | STRING | Yes | Multiline text |
| `seed` | Seed for sampling. Set to 0 to omit. Most models treat this as a hint only. (default: 0) | INT | Yes | 0 to 2147483647 |
| `system_prompt` | Foundational instructions that dictate the model's behavior. (default: "") | STRING | No | Multiline text |

**Note on `seed`:** This parameter has a "control_after_generate" behavior, meaning it can be set to automatically change (e.g., randomize, increment, or fixed) after each node execution, depending on the user's widget settings.

**Note on `system_prompt`:** This parameter is optional and is marked as an advanced parameter in the user interface.

### Anthropic Claude Inputs

Shared by `anthropic/claude-opus-5`, `anthropic/claude-opus-4.8`, `anthropic/claude-opus-4.7`, `anthropic/claude-fable-5`, `anthropic/claude-sonnet-5`, and `anthropic/claude-haiku-4.5`.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Reasoning effort. 'off' disables reasoning entirely. (default: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

### OpenAI GPT Inputs

Shared by `openai/gpt-5.6-sol-pro`, `openai/gpt-5.6-sol`, `openai/gpt-5.6-terra-pro`, `openai/gpt-5.6-terra`, `openai/gpt-5.6-luna-pro`, `openai/gpt-5.6-luna`, `openai/gpt-5.5-pro`, and `openai/gpt-5.5`.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Reasoning effort. 'off' disables reasoning entirely. (default: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

### Google Gemini 3.5 Flash Inputs

Applies to `google/gemini-3.5-flash`.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Reasoning effort. 'off' disables reasoning entirely. (default: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

### xAI Grok Inputs

Shared by `x-ai/grok-4.5`, `x-ai/grok-4.20`, and `x-ai/grok-4.3`.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Reasoning effort. 'off' disables reasoning entirely. (default: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

### DeepSeek Inputs

Shared by `deepseek/deepseek-v4-pro`, `deepseek/deepseek-v4-flash`, and `deepseek/deepseek-v3.2`.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Reasoning effort. 'off' disables reasoning entirely. (default: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

### Qwen 3.6 Plus and Flash Inputs

Shared by `qwen/qwen3.6-plus` and `qwen/qwen3.6-flash`.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Reasoning effort. 'off' disables reasoning entirely. (default: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

### Mistral Large 2512 Inputs

Applies to `mistralai/mistral-large-2512`. This model adds no model-specific parameter widgets; only the common inputs and the `images` reference slot apply.

### Mistral Medium 3.5 Inputs

Applies to `mistralai/mistral-medium-3-5`.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Reasoning effort. 'off' disables reasoning entirely. (default: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

### Moonshot Kimi K3 and K2.6 Inputs

Shared by `moonshotai/kimi-k3` and `moonshotai/kimi-k2.6`.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Reasoning effort. 'off' disables reasoning entirely. (default: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

### Perplexity Sonar Pro Inputs

Applies to `perplexity/sonar-pro`.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | How much web search context to retrieve. Larger = more grounded but slower/pricier. (default: "medium") | COMBO | No | "low"<br>"medium"<br>"high" |

### Perplexity Sonar Reasoning Pro and Deep Research Inputs

Shared by `perplexity/sonar-reasoning-pro` and `perplexity/sonar-deep-research`.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | How much web search context to retrieve. Larger = more grounded but slower/pricier. (default: "medium") | COMBO | No | "low"<br>"medium"<br>"high" |
| `reasoning_effort` | Reasoning effort. 'off' disables reasoning entirely. (default: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

### Reasoning-Only Models

Shared by `qwen/qwen3.6-max-preview`, `z-ai/glm-4.6`, `z-ai/glm-5`, and `moonshotai/kimi-k2-thinking`.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Reasoning effort. 'off' disables reasoning entirely. (default: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

### Reference Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `images` | Optional reference image(s) — sent as URLs. Growable slot: connect `image_1` through `image_N`, where N depends on the selected model. | IMAGE | No | 0 to N images (N = 8, 10, or 20 depending on the model) |
| `videos` | Optional reference video(s) — sent as URLs. Growable slot: connect `video_1` through `video_N`. Only available on models with video support. | VIDEO | No | 0 to 4 videos |

**Note on model capabilities and limits:**

- Image support: up to 20 images for Anthropic Claude, OpenAI GPT, Google Gemini 3.5 Flash, and xAI Grok models; up to 10 images for Qwen 3.6 Plus/Flash and Moonshot Kimi K3/K2.6; up to 8 images for Mistral Large 2512 and Mistral Medium 3.5. The DeepSeek, Qwen 3.6 Max Preview, Z.AI GLM, Moonshot Kimi K2 Thinking, and Perplexity Sonar models do not accept images.
- Video support: only `google/gemini-3.5-flash`, `qwen/qwen3.6-plus`, and `qwen/qwen3.6-flash` accept videos, with a maximum of 4 videos.
- The node raises an error if more images or videos are connected than the selected model supports.
- When `reasoning_effort` is set to "low", "medium", or "high", the model reasons internally but does not return the reasoning trace; "off" disables reasoning entirely.
- The `search_context_size` widget only appears for Perplexity Sonar models. The `reasoning_effort` and `search_context_size` widgets are marked as advanced parameters.
- The node displays an approximate price badge (USD per 1K tokens) based on the selected model.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `output` | The generated text response from the selected OpenRouter model. | STRING |

**Note on errors:** the node raises an error if OpenRouter returns an API error, an empty response (no choices), or a refusal from the model.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterLLMNode/en.md)

---
**Source fingerprint (SHA-256):** `534ab9ecc12e35a23a4d8f3e10f4f82d95db8e902ac8a2f2ee0ea68246516f62`
