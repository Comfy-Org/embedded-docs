# Kandinsky5ImageToVideo

The Kandinsky5ImageToVideo node prepares conditioning and latent space data for video generation using the Kandinsky model. It creates an empty video latent tensor and can optionally encode a starting image to guide the initial frames of the generated video, modifying the positive and negative conditioning accordingly.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `positive` | The positive conditioning prompts to guide the video generation. | CONDITIONING | Yes | N/A |
| `negative` | The negative conditioning prompts to steer the video generation away from certain concepts. | CONDITIONING | Yes | N/A |
| `vae` | The VAE model used to encode the optional starting image into the latent space. | VAE | Yes | N/A |
| `width` | The width of the output video in pixels (default: 768). | INT | Yes | 16 to 8192 (step 16) |
| `height` | The height of the output video in pixels (default: 512). | INT | Yes | 16 to 8192 (step 16) |
| `length` | The number of frames in the video (default: 121). | INT | Yes | 1 to 8192 (step 4) |
| `batch_size` | The number of video sequences to generate simultaneously (default: 1). | INT | Yes | 1 to 4096 |
| `start_image` | An optional starting image. If provided, it is encoded and used to replace the noisy start of the model's output latents. | IMAGE | No | N/A |

**Note:** When a `start_image` is provided, it is resized to match the specified `width` and `height` using bilinear interpolation. Only the first `length` frames of the image are used for encoding. The encoded latent is then injected into both the `positive` and `negative` conditioning, along with a mask that marks the start frames, so the clean encoded image replaces the noisy beginning of the generated video.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `positive` | The modified positive conditioning, potentially updated with the encoded start image data. | CONDITIONING |
| `negative` | The modified negative conditioning, potentially updated with the encoded start image data. | CONDITIONING |
| `latent` | An empty video latent tensor filled with zeros, shaped according to the specified `batch_size`, `length`, `height`, and `width`. | LATENT |
| `cond_latent` | The clean, encoded latent representation of the provided start images. Used to replace the noisy start of the model's output latents. Empty when no `start_image` is provided. | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/en.md)

---
**Source fingerprint (SHA-256):** `7212f0ea912578d3b72dddf1333a20054a881e3f22c2b8abd9645fc21e75a08b`
