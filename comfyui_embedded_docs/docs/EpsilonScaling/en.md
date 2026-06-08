Implements the Epsilon Scaling method from the research paper "Elucidating the Exposure Bias in Diffusion Models." This method improves sample quality by scaling the predicted noise during the sampling process. It uses a uniform schedule to mitigate exposure bias in diffusion models.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | The model to apply epsilon scaling to | MODEL | Yes | - |
| `scaling_factor` | The factor used to scale the predicted noise (default: 1.005) | FLOAT | No | 0.5 - 1.5 |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `model` | The model with epsilon scaling applied | MODEL |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EpsilonScaling/en.md)
