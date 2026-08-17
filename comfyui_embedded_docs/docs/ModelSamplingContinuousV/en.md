# ModelSamplingContinuousV

The ModelSamplingContinuousV node modifies a model's sampling behavior by applying continuous V-prediction sampling parameters. It creates a clone of the input model and configures it with custom sigma range settings for advanced sampling control. This allows users to fine-tune the sampling process with specific minimum and maximum sigma values.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | The input model to be modified with continuous V-prediction sampling | MODEL | Yes | - |
| `sampling` | The sampling method to apply. Only V-prediction is currently supported. | COMBO | Yes | `"v_prediction"` |
| `sigma_max` | The maximum sigma value for sampling (default: 500.0) | FLOAT | Yes | 0.0 – 1000.0 (step 0.001) |
| `sigma_min` | The minimum sigma value for sampling (default: 0.03) | FLOAT | Yes | 0.0 – 1000.0 (step 0.001) |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `model` | The modified model with continuous V-prediction sampling applied | MODEL |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/en.md)

---
**Source fingerprint (SHA-256):** `8549be9dd2375374c20da7c74a756a90285716db0e52fed8a1a2b753cd6d75fe`
