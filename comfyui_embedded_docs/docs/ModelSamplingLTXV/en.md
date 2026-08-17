# ModelSamplingLTXV

The ModelSamplingLTXV node applies advanced sampling parameters to a model based on token count. It calculates a shift value using a linear interpolation between base and maximum shift values, with the calculation depending on the number of tokens in the input latent. The node then creates a specialized model sampling configuration and applies it to the input model.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | The input model to apply sampling parameters to | MODEL | Yes | - |
| `max_shift` | The maximum shift value used in the linear interpolation calculation. The shift value equals this maximum at 4096 tokens (default: 2.05) | FLOAT | Yes | 0.0 to 100.0 |
| `base_shift` | The base shift value used in the linear interpolation calculation. The shift value equals this base at 1024 tokens (default: 0.95) | FLOAT | Yes | 0.0 to 100.0 |
| `latent` | Optional latent input used to determine the token count for the shift calculation. The token count is the product of the spatial dimensions of the latent samples. If not provided, a default token count of 4096 is used | LATENT | No | - |

Note: The shift value is calculated by linear interpolation between `base_shift` at 1024 tokens and `max_shift` at 4096 tokens. When no `latent` is provided, the default token count of 4096 makes the shift equal to `max_shift`.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `model` | The modified model with the applied sampling parameters | MODEL |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/en.md)

---
**Source fingerprint (SHA-256):** `aba596c5478e9d6ee821eec1eca15506935bcc765a368087ccc442fc2ed6671b`
