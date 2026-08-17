# FreeU_V2

The FreeU_V2 node enhances image generation quality by applying frequency-based modifications to a diffusion model's U-Net architecture. It uses configurable scaling factors to adjust feature channels in different blocks, improving output without requiring additional training.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | The diffusion model to apply FreeU enhancement to | MODEL | Yes | - |
| `b1` | Backbone feature scaling factor for the first block (default: 1.3) | FLOAT | Yes | 0.0 - 10.0 |
| `b2` | Backbone feature scaling factor for the second block (default: 1.4) | FLOAT | Yes | 0.0 - 10.0 |
| `s1` | Skip feature scaling factor for the first block (default: 0.9) | FLOAT | Yes | 0.0 - 10.0 |
| `s2` | Skip feature scaling factor for the second block (default: 0.2) | FLOAT | Yes | 0.0 - 10.0 |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `model` | The enhanced diffusion model with FreeU modifications applied | MODEL |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU_V2/en.md)

---
**Source fingerprint (SHA-256):** `4cef2af9b04164a8ead25bea9c9bb3311be9224f2539a5cc6edbe97ad8465d65`
