# TripoSplat Conditioning

This node encodes an input image using the DINOv3 vision encoder and the Flux2 VAE to create positive and negative conditioning data for the TripoSplat model. It also generates a fixed-size noise target (a latent sequence plus camera token) that serves as the starting point for the KSampler.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `clip_vision` | DINOv3 ViT-H/16+ image encoder | CLIP_VISION | Yes | - |
| `vae` | Flux2 VAE | VAE | Yes | - |
| `image` | The input image to encode | IMAGE | Yes | - |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `positive` | Positive conditioning data containing DINOv3 image features and the Flux2 VAE latent of the input image | CONDITIONING |
| `negative` | Negative conditioning data containing zero-filled DINOv3 features and zero-filled Flux2 VAE latent | CONDITIONING |
| `latent` | The fixed size noise target (latent + camera) for the KSampler | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatConditioning/en.md)

---
**Source fingerprint (SHA-256):** `59ebeef272d125a2cc2045f4ff54f99268b1273d0a1fd46f7462e6d312f3a805`
