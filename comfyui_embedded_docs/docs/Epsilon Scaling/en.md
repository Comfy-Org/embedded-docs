# Epsilon Scaling

This node implements the Epsilon Scaling method from the research paper "Elucidating the Exposure Bias in Diffusion Models" (arxiv.org/abs/2308.15321v6). It works by scaling the predicted noise during the sampling process to help reduce exposure bias, which can lead to improved quality in the generated images. This implementation uses the "uniform schedule" recommended by the paper for its practicality and effectiveness.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | The model to which the epsilon scaling patch will be applied. | MODEL | Yes | - |
| `scaling_factor` | The factor by which the predicted noise is scaled. A value greater than 1.0 reduces the predicted noise, while a value less than 1.0 increases it (default: 1.005). | FLOAT | Yes | 0.5 - 1.5 (step: 0.001) |

Note: The `scaling_factor` is guarded against a value of zero to prevent division by zero. The UI enforces a minimum of 0.5, so this cannot occur through normal use.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `model` | A patched copy of the input model with the epsilon scaling function applied to its sampling process. The original model is left unmodified. | MODEL |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon Scaling/en.md)

---
**Source fingerprint (SHA-256):** `8d258c7bb853940922402f1009d777bfc71e88704fd2f615f569c214ddbeac64`
