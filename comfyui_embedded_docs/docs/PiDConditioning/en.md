# PiD Conditioning

Attaches a latent image and a degrade sigma value to a CONDITIONING data. This is used for PiD (Pixel-in-Detail) decoding or upscaling, allowing you to control how much the latent is degraded before processing.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `positive` | The conditioning data to attach the latent and degrade sigma to. | CONDITIONING | Yes | - |
| `latent` | The latent image (from VAEEncode or a KSampler) to attach to the conditioning. | LATENT | Yes | - |
| `latent_format` | The format of the latent. Flux1 (16-ch) and Flux2 (128-ch) latents are auto-detected from the channel dimension under "flux". For SD3 (16-ch), SDXL (4-ch), or QwenImage (16-ch), select manually (default: "flux"). | COMBO | Yes | `"flux"`<br>`"sd3"`<br>`"sdxl"`<br>`"qwenimage"` |
| `degrade_sigma` | 0 = clean latent. Increase to denoise corrupted latent outputs (default: 0.0). | FLOAT | Yes | 0.0 to 1.0 (step: 0.01) |

Note: When `latent_format` is "flux", the node automatically detects whether the latent is Flux1 (16 channels) or Flux2 (128 channels) based on its channel dimension. If the processed latent has 5 dimensions, only the first slice along the last dimension is used.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `CONDITIONING` | The original conditioning data with the latent and degrade sigma values attached. | CONDITIONING |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/en.md)

---
**Source fingerprint (SHA-256):** `24f613b33e7872cb35f458aa5794a3cc4d37ceaecd43725039edef75f4a512bc`
