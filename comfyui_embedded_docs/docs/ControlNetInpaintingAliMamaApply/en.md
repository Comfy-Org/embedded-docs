# Apply ControlNet Inpainting (AliMama)

This node applies ControlNet conditioning for inpainting tasks by combining positive and negative conditioning with a control image and a mask. It processes the image and mask to create modified conditioning that guides the generation process, allowing precise control over which areas are inpainted. The node also supports strength and timing controls to adjust the ControlNet's influence during generation.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `positive` | The positive conditioning that guides the generation toward desired content. | CONDITIONING | Yes | - |
| `negative` | The negative conditioning that guides the generation away from unwanted content. | CONDITIONING | Yes | - |
| `control_net` | The ControlNet model that provides additional control over the generation. | CONTROL_NET | Yes | - |
| `vae` | The VAE used for encoding and decoding images. | VAE | Yes | - |
| `image` | The input image used as control guidance for the ControlNet. | IMAGE | Yes | - |
| `mask` | The mask that defines which areas of the image should be inpainted. | MASK | Yes | - |
| `strength` | The strength of the ControlNet effect (default: 1.0). | FLOAT | Yes | 0.0 to 10.0 |
| `start_percent` | Advanced option. The fraction of the generation process at which ControlNet influence begins (default: 0.0). | FLOAT | Yes | 0.0 to 1.0 |
| `end_percent` | Advanced option. The fraction of the generation process at which ControlNet influence stops (default: 1.0). | FLOAT | Yes | 0.0 to 1.0 |

**Note:** When the selected ControlNet has `concat_mask` enabled, the mask values are inverted (1 - mask), a resized version of the inverted mask is applied to the image, and the inverted mask is included in the extra concatenation data passed to the ControlNet. If `concat_mask` is disabled, the `mask` input is not used.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `positive` | The modified positive conditioning with ControlNet applied for inpainting. | CONDITIONING |
| `negative` | The modified negative conditioning with ControlNet applied for inpainting. | CONDITIONING |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/en.md)

---
**Source fingerprint (SHA-256):** `307b55c7b4936826b9e4424c172248fa4b41921c2362de724e5cfa2f1c25de68`
