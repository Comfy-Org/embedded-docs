# EmptyLTXVLatentVideo

The EmptyLTXVLatentVideo node creates an empty latent tensor for video generation. It produces a zero-filled latent representation with the specified width, height, length, and batch size, ready to be used as a starting point in LTXV video workflows. The latent stores the video in a compressed form: the spatial dimensions are divided by 32 and the frame count is reduced by a factor of 8.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `width` | The width of the latent video in pixels (default: 768, step: 32) | INT | Yes | 64 to MAX_RESOLUTION |
| `height` | The height of the latent video in pixels (default: 512, step: 32) | INT | Yes | 64 to MAX_RESOLUTION |
| `length` | The number of frames in the latent video (default: 97, step: 8) | INT | Yes | 1 to MAX_RESOLUTION |
| `batch_size` | The number of latent videos to generate in a batch (default: 1) | INT | No | 1 to 4096 |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `samples` | The generated empty latent tensor filled with zeros. The latent also carries a `downscale_ratio_spacial` value of 32, which describes the spatial downscaling applied to the width and height. | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/en.md)

---
**Source fingerprint (SHA-256):** `0b1e57baf9730d852b03b6bccbb8a033e2be9b9cd2420a0aa3638c31f6d3cd26`
