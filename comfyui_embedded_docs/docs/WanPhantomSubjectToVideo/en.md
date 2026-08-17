# WanPhantomSubjectToVideo

The WanPhantomSubjectToVideo node generates video content by processing conditioning inputs and optional reference images. It creates latent representations for video generation and can incorporate visual guidance from input images when provided. The node prepares conditioning data with time-dimensional concatenation for Wan video models and outputs modified conditioning along with generated latent video data.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `positive` | Positive conditioning input for guiding video generation | CONDITIONING | Yes | - |
| `negative` | Negative conditioning input to avoid certain characteristics | CONDITIONING | Yes | - |
| `vae` | VAE model for encoding images when provided | VAE | Yes | - |
| `width` | Output video width in pixels (default: 832, must be divisible by 16) | INT | Yes | 16 to MAX_RESOLUTION |
| `height` | Output video height in pixels (default: 480, must be divisible by 16) | INT | Yes | 16 to MAX_RESOLUTION |
| `length` | Number of frames in the generated video (default: 81, must be divisible by 4) | INT | Yes | 1 to MAX_RESOLUTION |
| `batch_size` | Number of videos to generate simultaneously (default: 1) | INT | Yes | 1 to 4096 |
| `images` | Optional reference images for time-dimensional conditioning | IMAGE | No | - |

**Note:** When `images` are provided, they are automatically upscaled to match the specified `width` and `height`, and only the first `length` frames are used for processing. Each image is reduced to its first 3 color channels before being encoded by the VAE. When `images` are not provided, the conditioning inputs pass through unchanged.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `positive` | Modified positive conditioning with time-dimensional concatenation when images are provided | CONDITIONING |
| `negative_text` | Modified negative conditioning with time-dimensional concatenation when images are provided | CONDITIONING |
| `negative_img_text` | Negative conditioning with zeroed time-dimensional concatenation when images are provided | CONDITIONING |
| `latent` | Zero-filled latent video representation with 16 channels, a temporal dimension of ((length - 1) // 4) + 1, and spatial dimensions of height // 8 and width // 8 | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/en.md)

---
**Source fingerprint (SHA-256):** `a1853382f6e564f66262b69dd7b06cc58e26b93386a460a98e6fcc2ff6acf12b`
