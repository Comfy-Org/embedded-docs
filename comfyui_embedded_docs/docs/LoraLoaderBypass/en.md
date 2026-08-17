# Load LoRA (Bypass) (For debugging)

The LoraLoaderBypass node applies a LoRA (Low-Rank Adaptation) to a diffusion model and a CLIP model in a special bypass mode. Unlike a standard LoRA loader, it does not permanently modify the base model weights. Instead, it adds the LoRA's effect to the model's normal forward pass, which is useful for training or when working with models that have their weights offloaded.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | The diffusion model the LoRA will be applied to. | MODEL | Yes | N/A |
| `clip` | The CLIP model the LoRA will be applied to. | CLIP | Yes | N/A |
| `lora_name` | The name of the LoRA file to apply. The options are loaded from the `loras` folder. | COMBO | Yes | List of available LoRA files |
| `strength_model` | How strongly to modify the diffusion model. This value can be negative (default: 1.0). | FLOAT | Yes | -100.0 to 100.0 |
| `strength_clip` | How strongly to modify the CLIP model. This value can be negative (default: 1.0). | FLOAT | Yes | -100.0 to 100.0 |

**Note:** If both `strength_model` and `strength_clip` are set to 0, the node returns the original, unmodified `model` and `clip` inputs without processing.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `MODEL` | The diffusion model with the LoRA applied in bypass mode. | MODEL |
| `CLIP` | The CLIP model with the LoRA applied in bypass mode. | CLIP |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/en.md)

---
**Source fingerprint (SHA-256):** `025f0638a6690a53b1a6c4548dac24fb7e7f26e04ff4b1c88d29b061430037a8`
