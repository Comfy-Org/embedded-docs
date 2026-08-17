# EmptyCosmosLatentVideo

The EmptyCosmosLatentVideo node creates an empty latent video tensor with specified dimensions. It generates a zero-filled latent representation that can be used as a starting point for video generation workflows, with configurable width, height, length, and batch size parameters. The spatial dimensions of the latent are downsampled by a factor of 8.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `width` | The width of the latent video in pixels (default: 1280, must be divisible by 16) | INT | Yes | 16 to MAX_RESOLUTION |
| `height` | The height of the latent video in pixels (default: 704, must be divisible by 16) | INT | Yes | 16 to MAX_RESOLUTION |
| `length` | The number of frames in the latent video (default: 121, must be divisible by 8) | INT | Yes | 1 to MAX_RESOLUTION |
| `batch_size` | The number of latent videos to generate in a batch (default: 1) | INT | Yes | 1 to 4096 |

The latent tensor uses 16 channels. Spatial dimensions are divided by 8 compared to the pixel dimensions (height // 8, width // 8), and the frame count is compressed to ((length - 1) // 8) + 1 latent frames.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `samples` | The generated empty latent video tensor with zero values. Shape: (batch_size, 16, ((length - 1) // 8) + 1, height // 8, width // 8) | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/en.md)

---
**Source fingerprint (SHA-256):** `7ee194324b02367ed853f6d36bc51742081bac6a9469c4a619586e0560a1b33b`
