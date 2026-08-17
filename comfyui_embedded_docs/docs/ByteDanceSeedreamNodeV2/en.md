# ByteDance Seedream 4.5 & 5.0

This node creates or edits images using ByteDance Seedream models (4.0, 4.5, 5.0 Lite, and 5.0 Pro). It generates new images from a text prompt, and can edit existing images based on reference images and a single-sentence instruction, supporting resolutions up to 4K.

## Inputs

The `model` selector determines which model-specific inputs are available. The tables below list the common inputs, the inputs for each model, and the growable reference-image slots.

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | The Seedream model version to use for generation. Each model has different capabilities, limits, and pricing. | DYNAMIC_COMBO | Yes | `"seedream 5.0 pro"`<br>`"seedream 5.0 lite"`<br>`"seedream-4-5-251128"`<br>`"seedream-4-0-250828"` |
| `prompt` | Text prompt for creating or editing an image. | STRING | Yes | Any text (non-empty) |
| `seed` | Seed to use for generation (default: 0). | INT | Yes | 0 to 2147483647 |
| `watermark` | Whether to add an "AI generated" watermark to the image (default: False). | BOOLEAN | Yes | True / False |
| `thinking` | Enable the model's prompt-optimization reasoning ("thinking") for better adherence. Can substantially increase generation time — notably on Seedream 5.0 Pro. Can only be disabled for text-to-image (not when reference images are provided). (default: True) | BOOLEAN | No | True / False |

### seedream 5.0 pro Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Pick a recommended size. Select Custom to use the width and height below. | COMBO | Yes | Model-specific presets (includes Custom) |
| `width` | Custom width for image. Value is working only if `size_preset` is set to Custom (default: 2048). | INT | Yes | 1024 to 3136 (step 2) |
| `height` | Custom height for image. Value is working only if `size_preset` is set to Custom (default: 2048). | INT | Yes | 1024 to 2496 (step 2) |

### seedream 5.0 lite Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Pick a recommended size. Select Custom to use the width and height below. | COMBO | Yes | Model-specific presets (includes Custom) |
| `width` | Custom width for image. Value is working only if `size_preset` is set to Custom (default: 2048). | INT | Yes | 1024 to 6240 (step 2) |
| `height` | Custom height for image. Value is working only if `size_preset` is set to Custom (default: 2048). | INT | Yes | 1024 to 4992 (step 2) |
| `max_images` | Maximum number of images to generate. With 1, exactly one image is produced. With >1, the model generates between 1 and max_images related images (e.g., story scenes, character variations). Total images (input + generated) cannot exceed 15. (default: 1) | INT | Yes | 1 to 14 |
| `fail_on_partial` | If enabled, abort execution if any requested images are missing or return an error. (default: False) | BOOLEAN | Yes | True / False |

### seedream-4-5-251128 Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Pick a recommended size. Select Custom to use the width and height below. | COMBO | Yes | Model-specific presets (includes Custom) |
| `width` | Custom width for image. Value is working only if `size_preset` is set to Custom (default: 2048). | INT | Yes | 1024 to 6240 (step 2) |
| `height` | Custom height for image. Value is working only if `size_preset` is set to Custom (default: 2048). | INT | Yes | 1024 to 4992 (step 2) |
| `max_images` | Maximum number of images to generate. With 1, exactly one image is produced. With >1, the model generates between 1 and max_images related images (e.g., story scenes, character variations). Total images (input + generated) cannot exceed 15. (default: 1) | INT | Yes | 1 to 10 |
| `fail_on_partial` | If enabled, abort execution if any requested images are missing or return an error. (default: False) | BOOLEAN | Yes | True / False |

### seedream-4-0-250828 Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Pick a recommended size. Select Custom to use the width and height below. | COMBO | Yes | Model-specific presets (includes Custom) |
| `width` | Custom width for image. Value is working only if `size_preset` is set to Custom (default: 2048). | INT | Yes | 1024 to 6240 (step 2) |
| `height` | Custom height for image. Value is working only if `size_preset` is set to Custom (default: 2048). | INT | Yes | 1024 to 4992 (step 2) |
| `max_images` | Maximum number of images to generate. With 1, exactly one image is produced. With >1, the model generates between 1 and max_images related images (e.g., story scenes, character variations). Total images (input + generated) cannot exceed 15. (default: 1) | INT | Yes | 1 to 10 |
| `fail_on_partial` | If enabled, abort execution if any requested images are missing or return an error. (default: False) | BOOLEAN | Yes | True / False |

### Reference Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `images` | Optional reference image(s) for image-to-image or multi-reference generation. Growable slot: connect 1..N items (`image_1`, `image_2`, ..., `image_N`); the maximum count depends on the selected model (10 for seedream 5.0 pro, seedream-4-5-251128, and seedream-4-0-250828; 14 for seedream 5.0 lite). | IMAGE | No | 0 to 10<br>0 to 14 (seedream 5.0 lite) |

### Notes

- Custom `width` and `height` values only take effect when `size_preset` is set to Custom.
- Resolution limits (based on width × height):
  - seedream 5.0 pro: minimum 0.92 MP, maximum 4.19 MP.
  - seedream 5.0 lite and seedream-4-5-251128: minimum 3.68 MP.
  - seedream-4-0-250828: minimum 0.92 MP.
  - seedream 5.0 lite, seedream-4-5-251128, and seedream-4-0-250828: maximum 16.78 MP.
- Reference images must have an aspect ratio between 1:3 and 3:1.
- When `max_images` is greater than 1 (available on seedream 5.0 lite, seedream-4-5-251128, and seedream-4-0-250828), the total number of images (reference images plus generated images) cannot exceed 15.
- `thinking` can only be disabled for text-to-image; it must be enabled when reference images are provided.
- seedream 5.0 pro always generates a single image and does not show the `max_images` or `fail_on_partial` inputs.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `image` | The generated or edited image. If multiple images were requested with `max_images`, they are returned concatenated into a single batch. | IMAGE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV2/en.md)

---
**Source fingerprint (SHA-256):** `b57e0d85a586aaeb7cf02ceaaddcd2d36cdac20f5251cba48de602a979420f1c`
