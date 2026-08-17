# Grok Image

The Grok Image node generates one or more images based on a text prompt using the Grok AI image models. It sends the prompt and settings to an external service and returns the generated images as tensors that can be used elsewhere in the workflow.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | The specific Grok model to use for image generation. Different models may offer varying quality, speed, or features. | COMBO | Yes | `"grok-imagine-image-2.0"`<br>`"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `prompt` | The text prompt used to generate the image. This description guides the AI on what to create. Must contain at least 1 non-whitespace character. | STRING | Yes | N/A |
| `aspect_ratio` | The desired width-to-height ratio for the generated image. | COMBO | Yes | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |
| `number_of_images` | Number of images to generate (default: 1). | INT | Yes | 1 to 10 |
| `seed` | Seed to determine if node should re-run; actual results are nondeterministic regardless of seed (default: 0). | INT | Yes | 0 to 2147483647 |
| `resolution` | The desired output resolution for the generated images (default: "1K"). | COMBO | No | `"1K"`<br>`"2K"` |
| `quality` | Quality level, supported only by the grok-imagine-image-2.0 model (default: "medium"). | COMBO | No | Multiple options available |

**Note:** The `quality` parameter is only applied when `model` is set to "grok-imagine-image-2.0". For all other models, this setting is ignored.

**Note:** The `seed` parameter is primarily used to control when the node re-executes within a workflow. Due to the nature of the external AI service, the generated images are not reproducible across runs, even with an identical seed.

**Note on pricing:** The cost of generating images depends on the selected `model`, `resolution`, `quality`, and `number_of_images`; the total price is the per-image rate multiplied by `number_of_images`. For the "grok-imagine-image-2.0" model, the per-image rate is $0.04 at "1K" resolution and $0.06 at "2K" with "low" quality, or $0.06 at "1K" and $0.08 at "2K" with other quality levels. The "grok-imagine-image-quality" model costs $0.05 per image at "1K" and $0.07 per image at "2K". The "grok-imagine-image-pro" model costs $0.07 per image. Other models cost $0.02 per image.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `output` | The generated image or a batch of images. If `number_of_images` is 1, a single image tensor is returned. If greater than 1, a batch of image tensors is returned. | IMAGE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageNode/en.md)

---
**Source fingerprint (SHA-256):** `a89f5df0d4827f45013f1af92541d36b5b8c8edc8626e07af4fe2d85ee5486e7`
