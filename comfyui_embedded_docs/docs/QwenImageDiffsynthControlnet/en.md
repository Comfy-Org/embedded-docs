# Apply Qwen Image DiffSynth ControlNet

The QwenImageDiffsynthControlnet node applies a diffusion synthesis control network patch to modify a base model's behavior. It uses an image input and optional mask to guide the model's generation process with adjustable strength, creating a patched model that incorporates the control network's influence for more controlled image synthesis.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | The base model to be patched with the control network | MODEL | Yes | - |
| `model_patch` | The control network patch model to apply to the base model | MODEL_PATCH | Yes | - |
| `vae` | The VAE (Variational Autoencoder) used in the diffusion process | VAE | Yes | - |
| `image` | The input image used to guide the control network (only RGB channels are used) | IMAGE | Yes | - |
| `strength` | The strength of the control network influence (default: 1.0) | FLOAT | Yes | -10.0 to 10.0 (step: 0.01) |
| `mask` | Optional mask that defines areas where the control network should be applied (inverted internally) | MASK | No | - |

**Note:** When a mask is provided, it is automatically inverted (1.0 - mask) and reshaped to match the dimensions expected by the control network processing. When the model patch is a ZImage Control type, the patch is applied to both the noise refiner and double blocks; for a standard DiffSynth control network, only the double block patch is applied.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `model` | The modified model with the diffusion synthesis control network patch applied | MODEL |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/en.md)

---
**Source fingerprint (SHA-256):** `56739c098933cb70d3bcb8d6b251da33e7879b464b2e8a7296da085aefc15698`
