# Save LoRA Weights

The SaveLoRA node saves a LoRA (Low-Rank Adaptation) model to a file. It writes the LoRA model as a `.safetensors` file in the output directory. You can specify a filename prefix and an optional step count; when provided, the step count is included in the saved file name.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `lora` | The LoRA model to save. Do not use the model with LoRA layers. | LORA_MODEL | Yes | N/A |
| `prefix` | The prefix to use for the saved LoRA file (default: "loras/ComfyUI_trained_lora"). | STRING | Yes | N/A |
| `steps` | Optional: The number of steps the LoRA has been trained for, used to name the saved file. | INT | No | N/A |

**Note:** The `lora` input must be a pure LoRA model. Do not provide a base model that has LoRA layers applied to it.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| *None* | This node does not output any data to the workflow. It is an output node that saves a file to disk. | N/A |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/en.md)

---
**Source fingerprint (SHA-256):** `02f1d15dd7a5181666f2dbf06c45c07b12c4a178985464e07b5f613bd628f906`
