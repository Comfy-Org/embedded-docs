# Recraft V4 Text to Image

This node generates images from text descriptions using the Recraft V4 and V4.1 AI models. It sends the prompt and generation settings to the Recraft image generation service and returns the resulting image or images. You can choose the model, the image size, and the number of images to generate.

## Inputs

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | The model to use for generation. Selecting a model determines the available `size` options. | DYNAMIC_COMBO | Yes | `"recraftv4_1"`<br>`"recraftv4_1_utility"`<br>`"recraftv4_1_pro"`<br>`"recraftv4_1_utility_pro"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | Prompt for the image generation. Maximum 10,000 characters. | STRING | Yes | 1 to 10000 characters |
| `negative_prompt` | This input is ignored: negative prompt is not supported by Recraft V4 and V4.1 models. | STRING | Yes | N/A |
| `n` | The number of images to generate (default: 1). | INT | Yes | 1 to 6 |
| `seed` | Seed to determine if node should re-run; actual results are nondeterministic regardless of seed (default: 0). | INT | Yes | 0 to 18446744073709551615 |
| `recraft_controls` | Optional additional controls over the generation via the Recraft Controls node. | CUSTOM | No | N/A |

### recraftv4_1, recraftv4_1_utility, and recraftv4 Inputs

Shared by the `recraftv4_1`, `recraftv4_1_utility`, and `recraftv4` models.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `size` | The size of the generated image (default: 1024x1024). | COMBO | Yes | Multiple options available (standard Recraft V4 sizes) |

### recraftv4_1_pro, recraftv4_1_utility_pro, and recraftv4_pro Inputs

Shared by the `recraftv4_1_pro`, `recraftv4_1_utility_pro`, and `recraftv4_pro` models.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `size` | The size of the generated image (default: 2048x2048). | COMBO | Yes | Multiple options available (Pro Recraft V4 sizes) |

**Notes:**

- The `size` input appears when a model is selected, and its available options depend on the model: the standard models (`recraftv4_1`, `recraftv4_1_utility`, `recraftv4`) share one set of sizes, while the Pro models (`recraftv4_1_pro`, `recraftv4_1_utility_pro`, `recraftv4_pro`) share a different set.
- The `negative_prompt` input is shown in the UI but is not sent to the model; negative prompts are not supported by the Recraft V4 and V4.1 models.
- The `seed` value only determines whether the node re-runs when the value changes; actual image results are nondeterministic regardless of seed.
- If you use a style ID from the Infinite Style Library through the Recraft Controls input, make sure it is not a Vector art style, as this may return SVG data instead of an image.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `output` | The generated image or batch of images. | IMAGE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/en.md)

---
**Source fingerprint (SHA-256):** `0b345a2f84d20a5a86681c358796a3ee3a5a101aab62441a978c610854e02c8a`
