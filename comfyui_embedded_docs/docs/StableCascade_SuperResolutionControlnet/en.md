> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/en.md)

The StableCascade_SuperResolutionControlnet node prepares inputs for Stable Cascade super-resolution processing. It takes an input image and encodes it using a VAE to create controlnet input, while also generating placeholder latent representations for stage C and stage B of the Stable Cascade pipeline.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Yes | - | The input image to be processed for super-resolution |
| `vae` | VAE | Yes | - | The VAE model used to encode the input image |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `controlnet_input` | IMAGE | The encoded image representation suitable for controlnet input |
| `stage_c` | LATENT | Placeholder latent representation for stage C of Stable Cascade processing |
| `stage_b` | LATENT | Placeholder latent representation for stage B of Stable Cascade processing |

---
**Source fingerprint (SHA-256):** `78b6e5a02c48ac37a205ef9d8532a3aca19134de4ec7be98b2ee55969dab7b53`
