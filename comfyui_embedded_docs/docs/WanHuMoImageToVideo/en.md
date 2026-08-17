# WanHuMoImageToVideo

The WanHuMoImageToVideo node prepares the conditioning data and latent space for image-to-video generation. It creates an empty latent video tensor, optionally encodes a reference image with the VAE, and optionally converts audio encoder output into video-timed conditioning. The node outputs positive and negative conditioning streams plus a latent tensor for further video sampling.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `positive` | Positive conditioning input that guides the video generation toward desired content. | CONDITIONING | Yes | - |
| `negative` | Negative conditioning input that steers the video generation away from unwanted content. | CONDITIONING | Yes | - |
| `vae` | VAE model used for encoding the reference image into latent space. | VAE | Yes | - |
| `width` | Width of the output video frames in pixels (default: 832; must be divisible by 16). | INT | Yes | 16 to MAX_RESOLUTION (step 16) |
| `height` | Height of the output video frames in pixels (default: 480; must be divisible by 16). | INT | Yes | 16 to MAX_RESOLUTION (step 16) |
| `length` | Number of frames in the generated video sequence (default: 97; must satisfy `(length - 1)` divisible by 4). | INT | Yes | 1 to MAX_RESOLUTION (step 4) |
| `batch_size` | Number of video sequences to generate simultaneously (default: 1). | INT | Yes | 1 to 4096 |
| `audio_encoder_output` | Optional audio encoder output used to influence video generation based on audio content. | AUDIO_ENCODER_OUTPUT | No | - |
| `ref_image` | Optional reference image used to guide video generation style and content. | IMAGE | No | - |

**Note:** When `ref_image` is provided, it is resized to `width` x `height`, encoded with the `vae`, and added to both positive and negative conditioning as a reference latent. When no reference image is provided, zero reference latents are used. When `audio_encoder_output` is provided, its audio embeddings are processed and added to both conditioning streams as an audio embedding; otherwise a zero audio embedding is used.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `positive` | Positive conditioning with reference latent and audio embedding information added. | CONDITIONING |
| `negative` | Negative conditioning with reference latent and audio embedding information added. | CONDITIONING |
| `latent` | Latent tensor representing the video sequence, initialized with zeros according to `batch_size`, `length`, `height`, and `width`. | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/en.md)

---
**Source fingerprint (SHA-256):** `db674a4a00729a8715988030083e2858f958cd21de73bbbe4ed6d76f5f539419`
