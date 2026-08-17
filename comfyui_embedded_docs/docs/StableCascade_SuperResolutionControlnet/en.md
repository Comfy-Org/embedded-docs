# StableCascade_SuperResolutionControlnet

The StableCascade_SuperResolutionControlnet node prepares inputs for Stable Cascade super-resolution processing. It takes an input image and encodes it using a VAE to create controlnet input, while also generating placeholder latent representations for stage C and stage B of the Stable Cascade pipeline.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `image` | The input image to be processed for super-resolution | IMAGE | Yes | - |
| `vae` | The VAE model used to encode the input image | VAE | Yes | - |

Note: Only the first three color channels of the input image are used when encoding with the VAE.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `controlnet_input` | The encoded image representation suitable for controlnet input | IMAGE |
| `stage_c` | Placeholder latent representation for stage C of Stable Cascade processing, with dimensions based on the input image size divided by 16 | LATENT |
| `stage_b` | Placeholder latent representation for stage B of Stable Cascade processing, with dimensions based on the input image size divided by 2 | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/en.md)

---
**Source fingerprint (SHA-256):** `d9eff373ac7736f2e2f9788d1b43c04bb3212422aa1703d1d58ac512ce476925`
