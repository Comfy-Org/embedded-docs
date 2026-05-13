> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/en.md)

## Overview

This node converts a LATENT (such as the output from the VOIDWarpedNoise node) into a NOISE source. This allows you to use the warped noise with the SamplerCustomAdvanced node for more controlled image generation.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `warped_noise` | LATENT | Yes | N/A | Warped noise latent from VOIDWarpedNoise |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `NOISE` | NOISE | A noise source that can be used with SamplerCustomAdvanced |

---
**Source fingerprint (SHA-256):** `ff798d223da5cf705a40ad1f36cc403030105331d0cc4173e9553cd3718c5d93`
