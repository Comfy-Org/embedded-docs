# Apply SeedVR2 Conditioning

This node builds positive and negative conditioning from a VAE latent for use with the SeedVR2 model. It adds a mask channel to the latent, then pairs it with the model's built-in positive and negative conditioning embeddings to produce the conditioning values needed for sampling.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | The SeedVR2 model. | MODEL | Yes | - |
| `vae_conditioning` | The VAE latent to build conditioning from. Display name: latent. | LATENT | Yes | - |

The `vae_conditioning` latent must be a 5-D tensor in Comfy channel-first layout (B, C, T, H, W) with the number of channels expected by the SeedVR2 VAE. Channel-last latents are rejected with an error. The `model` input must be a valid SeedVR2 model with the expected internal structure.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `positive` | The positive conditioning for sampling. | CONDITIONING |
| `negative` | The negative conditioning for sampling. | CONDITIONING |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/en.md)

---
**Source fingerprint (SHA-256):** `28e508bdd776e2e3f5f2f93bfc29a1a1d1c34a11dbdc7f421d197ddbfa85f0f5`
