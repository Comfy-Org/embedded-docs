# Hunyuan Video 1.5 Super Resolution

The HunyuanVideo15SuperResolution node prepares conditioning data for a video super-resolution process. It takes a latent representation of a video and, optionally, a starting image, and packages them together with a noise augmentation value and optional CLIP vision data into a format that a model can use to generate a higher-resolution output.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `positive` | The positive conditioning input to be modified with the concatenated latent and noise augmentation data. | CONDITIONING | Yes | N/A |
| `negative` | The negative conditioning input to be modified with the concatenated latent and noise augmentation data. | CONDITIONING | Yes | N/A |
| `vae` | The VAE used to encode the optional `start_image`. Required if `start_image` is provided. | VAE | No | N/A |
| `start_image` | An optional starting image that guides the super-resolution process. If provided, it is upscaled, encoded with the `vae`, and placed at the beginning of the conditioning latent. | IMAGE | No | N/A |
| `clip_vision_output` | Optional CLIP vision embeddings. When provided, they are added to both the positive and negative conditioning. | CLIP_VISION_OUTPUT | No | N/A |
| `latent` | The latent video representation to be incorporated into the conditioning. | LATENT | Yes | N/A |
| `noise_augmentation` | The strength of noise augmentation to apply to the conditioning (default: 0.70). This is an advanced parameter. | FLOAT | Yes | 0.0 - 1.0 (step 0.01) |

**Note:** If you provide a `start_image`, you must also connect a `vae` for it to be encoded. The `start_image` is automatically upscaled to match the dimensions implied by the input `latent`, and only its first three color channels (RGB) are used by the VAE.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `positive` | The modified positive conditioning, now containing the concatenated latent, noise augmentation, and optional CLIP vision data. | CONDITIONING |
| `negative` | The modified negative conditioning, now containing the concatenated latent, noise augmentation, and optional CLIP vision data. | CONDITIONING |
| `latent` | The input latent, passed through unchanged. | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/en.md)

---
**Source fingerprint (SHA-256):** `c9e64092e78423f5e0dc43446a77240e09100242c25e4fccc91491049fe76be5`
