> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawGeneralImageEnhance/en.md)

This node enhances low-resolution images by upscaling them to super-resolution, removing artifacts and noise. It uses an external API to process the image and can automatically adjust the input size to stay within processing limits. The maximum allowed output size is 4 megapixels.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | STRING | Yes | `"generative_portrait"`<br>`"generative"` | The enhancement model to use. The `generative_portrait` model is optimized for portraits, while `generative` is a general-purpose model. |
| `image` | IMAGE | Yes | - | The input image to be enhanced. |
| `upscale_factor` | INT | Yes | `1`<br>`2`<br>`4` | The factor by which to upscale the image's dimensions. A factor of 1 means no upscaling, 2 doubles the dimensions, and 4 quadruples them. |
| `auto_downscale` | BOOLEAN | No | - | Automatically downscale input image if output would exceed the limit. When enabled, the node will attempt to reduce the input image size to fit within the 4 megapixel output limit before applying the requested upscale factor. (default: `False`) |

**Note:** The node will raise an error if the calculated output size (input height × upscale_factor × input width × upscale_factor) exceeds 4,000,000 pixels (4MP) and `auto_downscale` is disabled. When `auto_downscale` is enabled, the node will attempt to downscale the input image to fit within the limit before applying the requested upscale factor. If downscaling by more than 2x would be required, the node will instead reduce the upscale factor.

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | The enhanced and upscaled output image. |

---
**Source fingerprint (SHA-256):** `29f927d39777acdfba2aad107027672d281c202ec78e04942e405c2cc64fcee4`
