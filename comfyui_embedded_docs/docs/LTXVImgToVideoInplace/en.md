# LTXVImgToVideoInplace

The LTXVImgToVideoInplace node conditions a video latent representation by encoding an input image into its initial frames. It works by using a VAE to encode the image into the latent space and then replacing the first frames of the latent video samples with this encoded image. A noise mask is applied so the conditioning strength controls how strongly the image influences those initial frames during generation.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `vae` | The VAE model used to encode the input image into the latent space. | VAE | Yes | - |
| `image` | The input image to be encoded and used to condition the video latent. | IMAGE | Yes | - |
| `latent` | The target latent video representation to be modified. | LATENT | Yes | - |
| `strength` | Controls the conditioning strength of the encoded image on the initial latent frames. A value of 1.0 fully conditions the initial frames, while lower values apply weaker conditioning. (default: 1.0) | FLOAT | No | 0.0 - 1.0 |
| `bypass` | Bypass the conditioning. When enabled, the node returns the input latent unchanged. (default: False) | BOOLEAN | No | - |

**Note:** The `image` will be automatically resized (bilinear interpolation) to match the spatial dimensions required by the `vae` for encoding, based on the `latent` input's width and height. Only the first 3 color channels (RGB) of the image are used; any alpha channel is ignored.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `latent` | The modified latent video representation. It contains the updated samples and a `noise_mask` that applies the conditioning strength to the initial frames. | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/en.md)

---
**Source fingerprint (SHA-256):** `69faa4b2e7b0fedeee531dc5a8809e23a79c9ce03e9760afb865160594fef30d`
