# EmptyChromaRadianceLatentImage

The EmptyChromaRadianceLatentImage node creates a blank latent image with specified dimensions for use in chroma radiance workflows. It generates a tensor filled with zeros (containing 3 color channels) that serves as a starting point for latent space operations. The node allows you to define the width, height, and batch size of the empty latent image.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `width` | The width of the latent image in pixels (default: 1024, must be divisible by 16) | INT | Yes | 16 to MAX_RESOLUTION |
| `height` | The height of the latent image in pixels (default: 1024, must be divisible by 16) | INT | Yes | 16 to MAX_RESOLUTION |
| `batch_size` | The number of latent images to generate in a batch (default: 1) | INT | No | 1 to 4096 |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `samples` | The generated empty latent image tensor with the specified dimensions, filled with zeros | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/en.md)

---
**Source fingerprint (SHA-256):** `870cc89fb021c258c214db153cda0a32a63da1b6bf92f09cbd3b8498c363096b`
