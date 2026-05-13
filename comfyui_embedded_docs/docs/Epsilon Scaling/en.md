> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon Scaling/en.md)

This node implements the Epsilon Scaling method from the research paper "Elucidating the Exposure Bias in Diffusion Models" (arxiv.org/abs/2308.15321v6). It works by scaling the predicted noise during the sampling process to help reduce exposure bias, which can lead to improved quality in the generated images. This implementation uses the "uniform schedule" recommended by the paper for its practicality and effectiveness.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Yes | - | The model to which the epsilon scaling patch will be applied. |
| `scaling_factor` | FLOAT | No | 0.5 - 1.5 | The factor by which the predicted noise is scaled. A value greater than 1.0 reduces the noise, while a value less than 1.0 increases it (default: 1.005). |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `model` | MODEL | A patched version of the input model with the epsilon scaling function applied to its sampling process. |

---
**Source fingerprint (SHA-256):** `85c464ce0b2ec2a031a01d9eef5d50fd300be3012499cc061705fb7964110882`
