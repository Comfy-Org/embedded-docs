# ModelSamplingStableCascade

The ModelSamplingStableCascade node applies stable cascade sampling to a model by adjusting the sampling parameters with a shift value. It creates a modified clone of the input model with a custom sampling configuration for stable cascade generation.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | The input model to apply stable cascade sampling to | MODEL | Yes | - |
| `shift` | The shift value to apply to the sampling parameters (default: 2.0) | FLOAT | Yes | 0.0 - 100.0 (step: 0.01) |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `model` | The modified model with stable cascade sampling applied | MODEL |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/en.md)

---
**Source fingerprint (SHA-256):** `358681a7c698d4335cde60780d5a8b134b75df4ea40102bf51544c53bbb08c42`
