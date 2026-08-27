# Recraft V4 Text to Image

This node generates images from text descriptions using the Recraft V4 and V4.1 AI models. It sends your prompt to an external API and returns the generated images. You can control the output by specifying the model, image size, and number of images to create.

## Inputs

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | The model to use for generation. | DYNAMIC_COMBO | Yes | `"recraftv4_1"`<br>`"recraftv4_1_utility"`<br>`"recraftv4_1_pro"`<br>`"recraftv4_1_utility_pro"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | Prompt for the image generation. Maximum 10,000 characters. | STRING | Yes | N/A |
| `negative_prompt` | This input is ignored: negative prompt is not supported by Recraft V4 and V4.1 models. | STRING | Yes | N/A |
| `n` | The number of images to generate (default: 1). | INT | Yes | 1 to 6 |
| `seed` | Seed to determine if node should re-run; actual results are nondeterministic regardless of seed (default: 0). | INT | Yes | 0 to 18446744073709551615 |
| `recraft_controls` | Optional additional controls over the generation via the Recraft Controls node. | CUSTOM | No | N/A |

### recraftv4_1, recraftv4_1_utility, and recraftv4 Inputs

Shared by `recraftv4_1`, `recraftv4_1_utility`, and `recraftv4`.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `size` | The size of the generated image (default: "1024x1024"). | COMBO | Yes | Multiple options available (standard Recraft V4 sizes, includes "1024x1024") |

### recraftv4_1_pro, recraftv4_1_utility_pro, and recraftv4_pro Inputs

Shared by `recraftv4_1_pro`, `recraftv4_1_utility_pro`, and `recraftv4_pro`.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `size` | The size of the generated image (default: "2048x2048"). | COMBO | Yes | Multiple options available (pro Recraft V4 sizes, includes "2048x2048") |

**Note:** The `size` parameter is a dynamic input whose available options change based on the selected `model`. The `seed` value does not guarantee reproducible image outputs. If you use a style ID from the Infinite Style Library, make sure it is not a Vector art style, as this may return SVG data instead of an image.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `output` | The generated image or batch of images. | IMAGE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/en.md)

---
**Source fingerprint (SHA-256):** `0b345a2f84d20a5a86681c358796a3ee3a5a101aab62441a978c610854e02c8a`
