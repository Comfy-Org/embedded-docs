# Wan22ImageToVideoLatent

The Wan22ImageToVideoLatent node prepares the latent input used for Wan 2.2 video generation. It creates an empty video latent with the specified width, height, and number of frames, and, when a start image is given, encodes that image into the first frames of the latent. It also outputs a noise mask that marks which frames are already filled by the image and which frames still need to be generated.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `vae` | The VAE model used to encode the start image into the latent space | VAE | Yes | - |
| `width` | The width of the output video in pixels (default: 1280, step: 32) | INT | Yes | 32 to MAX_RESOLUTION |
| `height` | The height of the output video in pixels (default: 704, step: 32) | INT | Yes | 32 to MAX_RESOLUTION |
| `length` | The number of frames in the video (default: 49, step: 4) | INT | Yes | 1 to MAX_RESOLUTION |
| `batch_size` | The number of video latents to generate in parallel (default: 1) | INT | Yes | 1 to 4096 |
| `start_image` | Optional image or image sequence placed into the first frames of the video latent. Only the first `length` frames are used. The image is resized to `width` x `height` with bilinear resampling and center cropping before being encoded by the VAE. | IMAGE | No | - |

**Note:** The latent's spatial dimensions are `width / 16` and `height / 16`, so `width` and `height` must be divisible by 16. The latent's temporal dimension is calculated as `((length - 1) // 4) + 1` and it has 48 channels. When a `start_image` is provided, the encoded image fills the first frames of the latent and the `noise_mask` is set to 0 for those frames and 1 for the remaining frames, which tells the sampler to keep the image frames unchanged and generate the rest. When no `start_image` is provided, the latent is filled with zeros and no noise mask is included.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `LATENT` | The generated video latent, repeated `batch_size` times. When a `start_image` is provided, it also contains a `noise_mask` marking the image-encoded frames (0) and the frames to generate (1). | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/en.md)

---
**Source fingerprint (SHA-256):** `3d05980641eeef2e86df7a845aa8b2bd703882db98fe71adef2746ab34a9d717`
