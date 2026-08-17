# ModelSamplingSD3

The ModelSamplingSD3 node applies Stable Diffusion 3 sampling parameters to a model. It modifies the model's sampling behavior by adjusting the shift parameter, which controls the sampling distribution characteristics. The node creates a modified copy of the input model with the specified sampling configuration applied.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | The input model to apply SD3 sampling parameters to | MODEL | Yes | - |
| `shift` | Controls the sampling shift parameter (default: 3.0) | FLOAT | Yes | 0.0 - 100.0 |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `model` | The modified model with SD3 sampling parameters applied | MODEL |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/en.md)

---
**Source fingerprint (SHA-256):** `46d44786422c2efea78c1fe7e1183cebc9bf51d4f13861da04d5a974b5b6da7d`
