# OpenAI GPT Image 2

This node generates images using OpenAI's GPT Image API. It supports several GPT Image models, optional reference images for editing, and an optional mask for inpainting. When reference images are provided, the node sends an edit request to the API; otherwise it sends a plain generation request.

## Inputs

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | The OpenAI GPT Image model to use. Selecting a model reveals additional parameters specific to that model. | DYNAMIC_COMBO | Yes | `"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` |
| `prompt` | Text prompt for GPT Image (default: ""). | STRING | Yes | N/A |
| `n` | How many images to generate (default: 1). | INT | Yes | 1 to 8 |
| `seed` | Seed for reproducibility (default: 0). Not implemented yet in the backend. | INT | Yes | 0 to 2147483647 |

### gpt-image-2 Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model.size` | Image size. Select "Custom" to use the custom width and height (default: "auto"). | COMBO | Yes | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | Used only when `size` is "Custom". Must be a multiple of 16 (default: 1024). | INT | No | 1024 to 3840 |
| `model.custom_height` | Used only when `size` is "Custom". Must be a multiple of 16 (default: 1024). | INT | No | 1024 to 3840 |
| `model.background` | Return image with or without background (default: "auto"). | COMBO | Yes | `"auto"`<br>`"opaque"` |
| `model.quality` | Image quality, affects cost and generation time (default: "low"). | COMBO | Yes | `"low"`<br>`"medium"`<br>`"high"` |

### gpt-image-1.5 and gpt-image-1 Inputs

These two models share the same set of model-specific parameters.

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model.size` | Image size (default: "auto"). | COMBO | Yes | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `model.background` | Return image with or without background (default: "auto"). | COMBO | Yes | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | Image quality, affects cost and generation time (default: "low"). | COMBO | Yes | `"low"`<br>`"medium"`<br>`"high"` |

### Reference Inputs

These inputs are available for all models.

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model.images` | Optional reference image(s) for image editing. Growable slot: connect up to 16 images (`image_1` to `image_16`). | IMAGE | No | 0 to 16 images |
| `model.mask` | Optional mask for inpainting (white areas will be replaced). Requires exactly one reference image. | MASK | No | N/A |

**Parameter Constraints and Limitations:**

- When `model.size` is "Custom" (gpt-image-2 only), `model.custom_width` and `model.custom_height` must be multiples of 16, the longest edge must not exceed 3840 pixels, the aspect ratio must not exceed 3:1, and the total pixel count must be between 655,360 and 8,294,400.
- A mask requires exactly one reference image. A mask cannot be used without an input image, and it cannot be used with multiple input images.
- When a mask is provided, the mask height and width must match the input image height and width.
- Reference images are downscaled to a maximum of 2048 x 2048 total pixels before being sent to the API.
- The `seed` parameter is not implemented yet in the backend.
- If the API returns images with different dimensions in a single response, all images are resized to match the first image's dimensions.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `image` | The generated image or images, stacked into a single batch tensor of shape (N, H, W, C). | IMAGE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/en.md)

---
**Source fingerprint (SHA-256):** `fb3491f949151fbd3f5825ec9f9ae124019767d083f56966ef34af278aef50c0`
