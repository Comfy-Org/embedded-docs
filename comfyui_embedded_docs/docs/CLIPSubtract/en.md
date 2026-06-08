The CLIPSubtract node performs a subtraction operation between two CLIP models. It takes the first CLIP model as a base and subtracts the key patches from the second CLIP model, with an optional multiplier to control the subtraction strength. This allows for fine-tuned model blending by removing specific characteristics from one model using another.

## Inputs

| Parameter | Description | Data Type | Input Type | Default | Range |
| --- | --- | --- | --- | --- | --- |
| `clip1` | The base CLIP model that will be modified | CLIP | Required | - | - |
| `clip2` | The CLIP model whose key patches will be subtracted from the base model | CLIP | Required | - | - |
| `multiplier` | Controls the strength of the subtraction operation. Positive values subtract features from clip2, negative values add features instead. | FLOAT | Required | 1.0 | -10.0 to 10.0, step 0.01 |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `CLIP` | The resulting CLIP model after the subtraction operation | CLIP |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSubtract/en.md)

---
**Source fingerprint (SHA-256):** `ea7b6f838d6eb083d2d9bc07891b6ef2f3e625861ab1de9279df351e58f2a2a8`
