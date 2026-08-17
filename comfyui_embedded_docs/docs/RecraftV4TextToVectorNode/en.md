# Recraft V4 Text to Vector

The Recraft V4 Text to Vector node generates Scalable Vector Graphics (SVG) images from a text description. It connects to an external API to generate images using Recraft V4 and V4.1 models. The node outputs one or more SVG images based on your prompt.

## Inputs

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | The model to use for generation. Selecting a model changes the available `size` options. | DYNAMIC_COMBO | Yes | `"recraftv4_1_vector"`<br>`"recraftv4_1_utility_vector"`<br>`"recraftv4_1_pro_vector"`<br>`"recraftv4_1_utility_pro_vector"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | Prompt for the image generation. Maximum 10,000 characters. | STRING | Yes | N/A |
| `negative_prompt` | This input is ignored: negative prompt is not supported by Recraft V4 and V4.1 models. | STRING | Yes | N/A |
| `n` | The number of images to generate (default: 1). | INT | Yes | 1 to 6 |
| `seed` | Seed to determine if node should re-run; actual results are nondeterministic regardless of seed (default: 0). | INT | Yes | 0 to 18446744073709551615 |
| `recraft_controls` | Optional additional controls over the generation via the Recraft Controls node. | CUSTOM | No | N/A |

### recraftv4_1_vector, recraftv4_1_utility_vector, and recraftv4 Inputs

These three models share the same `size` options.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `size` | The size of the generated image (default: `"1024x1024"`). | COMBO | Yes | `"1024x1024"`<br>`"1152x896"`<br>`"896x1152"`<br>`"1216x832"`<br>`"832x1216"`<br>`"1344x768"`<br>`"768x1344"`<br>`"1536x640"`<br>`"640x1536"` |

### recraftv4_1_pro_vector, recraftv4_1_utility_pro_vector, and recraftv4_pro Inputs

These three models share the same `size` options.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `size` | The size of the generated image (default: `"2048x2048"`). | COMBO | Yes | `"2048x2048"`<br>`"2304x1792"`<br>`"1792x2304"`<br>`"2432x1664"`<br>`"1664x2432"`<br>`"2688x1536"`<br>`"1536x2688"`<br>`"3072x1280"`<br>`"1280x3072"` |

**Note:** The `size` parameter is a dynamic input whose available options change based on the selected `model`. The `seed` value does not guarantee reproducible results from the external API. The `negative_prompt` input is ignored because Recraft V4 and V4.1 models do not support negative prompts.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `output` | The generated Scalable Vector Graphics (SVG) image(s). | SVG |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/en.md)

---
**Source fingerprint (SHA-256):** `822f6b9fef67ef6beb1eba099c41c72570a1f79e316612201c81f6e5eb91408d`
