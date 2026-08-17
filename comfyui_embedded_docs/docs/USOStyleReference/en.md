# Apply USO Style Reference

The USOStyleReference node applies style information from a reference image to a Flux model. It builds a style embedding from the CLIP vision output, then patches a clone of the model so that, during generation, the style embedding is inserted in front of the text prompt conditioning.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | The base model to apply the style reference patch to | MODEL | Yes | - |
| `model_patch` | The model patch containing style reference information | MODEL_PATCH | Yes | - |
| `clip_vision_output` | The encoded visual features extracted from CLIP vision processing. The node combines the hidden states from layers -20 and -11 together with the penultimate hidden states to build the style embedding | CLIP_VISION_OUTPUT | Yes | - |

Note: All three inputs are required. This node is marked as experimental.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `model` | The modified model with the applied style reference patch | MODEL |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/en.md)

---
**Source fingerprint (SHA-256):** `9033dddb76fafb388c67dcd09d96102a7ab3e5bc416cec61bf18d088da37a0f0`
