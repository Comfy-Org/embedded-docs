# ModelSamplingAuraFlow

The ModelSamplingAuraFlow node applies a specialized sampling configuration to diffusion models, specifically designed for AuraFlow model architectures. It modifies the model's sampling behavior by applying a `shift` parameter that adjusts the sampling distribution. This node inherits from the SD3 model sampling framework and provides fine control over the sampling process.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | The diffusion model to apply the AuraFlow sampling configuration to. | MODEL | Yes | - |
| `shift` | The shift value to apply to the sampling distribution. Default: 1.73. Step: 0.01. | FLOAT | Yes | 0.0 - 100.0 |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `model` | The modified model with the AuraFlow sampling configuration applied. | MODEL |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/en.md)

---
**Source fingerprint (SHA-256):** `7ca35632ae73517c78aa31a528492427c9af37862322ff7335f895c597ee1709`
