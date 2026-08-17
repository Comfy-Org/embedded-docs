# ModelSave

The ModelSave node saves trained or modified models to your computer's storage. It takes a model as input and writes it to a safetensors checkpoint file in the output folder, using the filename prefix you specify. Workflow prompt and metadata information are embedded in the saved file when available.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | The model to be saved to disk | MODEL | Yes | - |
| `filename_prefix` | The filename and path prefix for the saved model file (default: "diffusion_models/ComfyUI"). A counter is appended to the name when saving (for example, `ComfyUI_00000_.safetensors`). | STRING | Yes | - |
| `prompt` | Workflow prompt information (automatically provided) | PROMPT | No | - |
| `extra_pnginfo` | Additional workflow metadata (automatically provided) | EXTRA_PNGINFO | No | - |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| *None* | This node does not return any output values | - |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/en.md)

---
**Source fingerprint (SHA-256):** `943e60f2c596d9cbcaabe95029fd9d443df5b61c6137736a8b1b81ab78f200ea`
