> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageInpaintingNode/en.md)

This node modifies specific areas of an image based on a text prompt and a mask. It uses the Recraft API to intelligently edit only the masked regions while keeping the rest of the image unchanged.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Yes | - | The input image to be modified |
| `mask` | MASK | Yes | - | The mask defining which areas of the image should be modified |
| `prompt` | STRING | Yes | - | Prompt for the image generation (default: empty string, maximum length: 1000 characters) |
| `n` | INT | Yes | 1-6 | The number of images to generate (default: 1, minimum: 1, maximum: 6) |
| `seed` | INT | Yes | 0-18446744073709551615 | Seed to determine if node should re-run; actual results are nondeterministic regardless of seed (default: 0) |
| `recraft_style` | STYLEV3 | No | - | Optional style parameter for the Recraft API. If not provided, defaults to "realistic_image" style |
| `negative_prompt` | STRING | No | - | An optional text description of undesired elements on an image (default: empty string) |

*Note: The `image` and `mask` must be provided together for the inpainting operation to work. The mask will be automatically resized to match the image dimensions. The `prompt` is validated and has a maximum length of 1000 characters.*

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | The modified image(s) generated based on the prompt and mask. Returns one image per input image multiplied by the `n` parameter |

---
**Source fingerprint (SHA-256):** `3eb6505a19173d8e4ea4216348f9592fd996cdfe2f07a9e79ccec5f738a8fb93`
