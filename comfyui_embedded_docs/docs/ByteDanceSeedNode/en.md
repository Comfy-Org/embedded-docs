# ByteDance Seed

ByteDance Seed generates text responses using ByteDance's Seed 2.0 models. Provide a text prompt and optionally include one or more images or videos for multimodal context.

## Inputs

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | The Seed model used to generate the response. | DYNAMIC_COMBO | Yes | `"Seed 2.0 Pro"`<br>`"Seed 2.0 Lite"`<br>`"Seed 2.0 Mini"` |
| `prompt` | Text input to the model. (default: "") | STRING | Yes | N/A |
| `seed` | Seed controls whether the node should re-run; results are non-deterministic regardless of seed. (default: 0) | INT | Yes | 0 to 2147483647 |
| `system_prompt` | Foundational instructions that dictate the model's behavior. (default: "") | STRING | No | N/A |

### Seed 2.0 Pro, Seed 2.0 Lite, and Seed 2.0 Mini Inputs

This setting is shared by all three model options.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `temperature` | Controls randomness. 0.0 is deterministic, higher values are more random. (default: 1.0) | FLOAT | Yes | 0.0 to 2.0 |

### Reference Inputs

The `model` selector provides these growable slots, which connect images and videos to give the model multimodal context.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `images` | Optional image(s) to use as context for the model. Up to 20 images. Growable slot: connect 1..20 items (e.g. `image_1`...`image_20`). | IMAGE | No | `image_1` to `image_20` |
| `videos` | Optional video(s) to use as context for the model. Up to 4 videos. Growable slot: connect 1..4 items (e.g. `video_1`...`video_4`). | VIDEO | No | `video_1` to `video_4` |

**Note:** The `model` selector determines which Seed model is used to generate the response. Each option maps to a specific model ID: `"Seed 2.0 Pro"` → `seed-2-0-pro-260328`, `"Seed 2.0 Lite"` → `seed-2-0-lite-260228`, and `"Seed 2.0 Mini"` → `seed-2-0-mini-260215`.

**Note on constraints:** A maximum of 20 images and 4 videos are supported per request. The `prompt` must be a non-empty string.

**Note on pricing:** Pricing is token-based and shown in the node UI as an approximate range per 1K tokens: Seed 2.0 Mini: $0.00025-$0.0009; Seed 2.0 Lite: $0.0003-$0.002; Seed 2.0 Pro: $0.0005-$0.003.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `output` | The generated text response from the Seed model. | STRING |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedNode/en.md)

---
**Source fingerprint (SHA-256):** `23c9b0e9983a65ce859e2e92acfe71604297f16d711fa094a6617a9915a46020`
