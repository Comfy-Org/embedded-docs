# Anthropic Claude

Generate text responses from an Anthropic Claude model. This node sends a text prompt and optional images to a Claude model and returns the generated text response.

## Inputs

The `model` parameter is a dynamic selector: when you choose a model, additional model-specific settings such as token limit, temperature, and reasoning effort appear below it.

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text input to the model. Must be non-empty after stripping whitespace. (default: empty string) | STRING | Yes | N/A |
| `model` | The Claude model used to generate the response. | DYNAMIC_COMBO | Yes | `"Opus 5"`<br>`"Opus 4.8"`<br>`"Fable 5"`<br>`"Sonnet 5"`<br>`"Opus 4.7"`<br>`"Opus 4.6"`<br>`"Sonnet 4.6"`<br>`"Sonnet 4.5"`<br>`"Haiku 4.5"` |
| `seed` | Seed controls whether the node should re-run; results are non-deterministic regardless of seed. (default: 0) | INT | Yes | 0 to 2147483647 |
| `images` | Optional image(s) to use as context for the model. Growable slot: connect `image_1` through `image_20`; up to 20 images. (default: none) | IMAGE | No | 0 to 20 images |
| `system_prompt` | Foundational instructions that dictate the model's behavior. (default: empty string) | STRING | No | N/A |

### Opus 5 and Fable 5 Inputs

Shared by Opus 5 and Fable 5. These models always use extended thinking and do not expose a temperature setting.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Maximum number of tokens to generate (includes reasoning tokens when enabled). (default: 32768) | INT | Yes | 4096 to 64000 |
| `reasoning_effort` | Extended thinking effort. Reasoning is always enabled for this model. (default: "high") | COMBO | Yes | `"low"`<br>`"medium"`<br>`"high"` |

### Opus 4.8 and Sonnet 5 Inputs

Shared by Opus 4.8 and Sonnet 5. These models do not expose a temperature setting.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Maximum number of tokens to generate (includes reasoning tokens when enabled). (default: 32768) | INT | Yes | 4096 to 64000 |
| `reasoning_effort` | Extended thinking effort. "off" disables reasoning. (default: "off") | COMBO | Yes | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

### Opus 4.7, Opus 4.6, Sonnet 4.6, and Sonnet 4.5 Inputs

Shared by Opus 4.7, Opus 4.6, Sonnet 4.6, and Sonnet 4.5. For Opus 4.7, the temperature input is shown but is ignored, and the API uses the default value of 1.0.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Maximum number of tokens to generate (includes reasoning tokens when enabled). (default: 32768) | INT | Yes | 4096 to 64000 |
| `temperature` | Controls randomness. 0.0 is deterministic, 1.0 is most random. Ignored for Opus 4.7 and any model when reasoning_effort is set. (default: 1.0) | FLOAT | Yes | 0.0 to 1.0 (step 0.01) |
| `reasoning_effort` | Extended thinking effort. "off" disables reasoning. (default: "off") | COMBO | Yes | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

### Haiku 4.5 Inputs

This model does not support extended thinking, so no `reasoning_effort` setting is available.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Maximum number of tokens to generate (includes reasoning tokens when enabled). (default: 32768) | INT | Yes | 4096 to 64000 |
| `temperature` | Controls randomness. 0.0 is deterministic, 1.0 is most random. (default: 1.0) | FLOAT | Yes | 0.0 to 1.0 (step 0.01) |

### Parameter Constraints

- Up to 20 images can be provided per request. The combined pixel count for uploaded images is limited to 1568 × 1568 pixels.
- Temperature is not configurable for Opus 5, Fable 5, Opus 4.8, and Sonnet 5. When a temperature input is available, it is ignored for Opus 4.7 and for any model when `reasoning_effort` is set to something other than "off".
- Reasoning is always enabled for Opus 5 and Fable 5, so the `reasoning_effort` options for these models do not include "off". The Haiku 4.5 model does not support extended thinking and therefore has no `reasoning_effort` setting.
- If Claude declines to answer a request for safety reasons, the node raises an error instead of returning text.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `output` | The generated text response from the Claude model. If no visible text is generated, the output is `"Empty response from Claude model."`. Thinking or reasoning blocks are not included in the output. | STRING |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/en.md)

---
**Source fingerprint (SHA-256):** `b0381e7981e5886d66b6976c7ddcad3f142bdd803271a6ac8567293dcddaa98a`
