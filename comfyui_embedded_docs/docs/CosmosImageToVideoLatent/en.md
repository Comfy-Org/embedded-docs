# CosmosImageToVideoLatent

The CosmosImageToVideoLatent node creates a video latent for image-to-video generation. It starts with a blank latent and can optionally encode a start image and/or an end image into the first or last frames of the video sequence. When images are provided, it also generates a noise mask that marks the encoded frames as fixed during generation.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `vae` | The VAE model used to encode the input images into latent space | VAE | Yes | - |
| `width` | The width of the output video in pixels (default: 1280) | INT | Yes | 16 to MAX_RESOLUTION (step 16) |
| `height` | The height of the output video in pixels (default: 704) | INT | Yes | 16 to MAX_RESOLUTION (step 16) |
| `length` | The number of frames in the video sequence (default: 121) | INT | Yes | 1 to MAX_RESOLUTION (step 8) |
| `batch_size` | The number of video latents to generate in the output batch (default: 1) | INT | Yes | 1 to 4096 |
| `start_image` | Optional image or sequence of images to encode at the beginning of the video sequence | IMAGE | No | - |
| `end_image` | Optional image or sequence of images to encode at the end of the video sequence | IMAGE | No | - |

**Note:** When neither `start_image` nor `end_image` is provided, the node returns a blank latent without a noise mask. When at least one image is provided, a `noise_mask` is included: latent frames encoded from the supplied images have mask value 0 (kept fixed), while the remaining frames have mask value 1 (to be generated). Images are resized to the target `width` and `height` before encoding, and the number of frames taken from an input image equals its batch dimension, up to a maximum of `length`. The latent has 16 channels, spatial dimensions `width / 8` and `height / 8`, and `((length - 1) // 8) + 1` frames. When images are provided, the latent and its noise mask are repeated `batch_size` times to form the output batch.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `latent` | A LATENT containing the video latent `samples` and, when `start_image` or `end_image` is provided, a `noise_mask` that marks the encoded frames as fixed | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/en.md)

---
**Source fingerprint (SHA-256):** `0b06ccfcb14c27c81eeebbbff519da1e187970d4cfc19c8796fc3da20688245c`
