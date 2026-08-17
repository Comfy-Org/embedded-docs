# Hunyuan3Dv2ConditioningMultiView

The Hunyuan3Dv2ConditioningMultiView node processes multi-view CLIP vision embeddings for 3D video generation. It takes optional front, left, back, and right view embeddings and adds positional encoding to each provided view before combining them into a single conditioning sequence. The node outputs both positive conditioning from the combined embeddings and negative conditioning with zero values.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `front` | CLIP vision output for the front view | CLIP_VISION_OUTPUT | No | - |
| `left` | CLIP vision output for the left view | CLIP_VISION_OUTPUT | No | - |
| `back` | CLIP vision output for the back view | CLIP_VISION_OUTPUT | No | - |
| `right` | CLIP vision output for the right view | CLIP_VISION_OUTPUT | No | - |

**Note:** At least one view input must be provided for the node to function. The node only processes views that contain valid CLIP vision output data. Each provided view receives a positional encoding based on its view position (front, left, back, right), and the encoded views are concatenated in that same order.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `positive` | Positive conditioning containing the combined multi-view embeddings with positional encoding | CONDITIONING |
| `negative` | Negative conditioning containing zero values with the same shape as the positive conditioning | CONDITIONING |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/en.md)

---
**Source fingerprint (SHA-256):** `1492b51661d0bb8f2c142c1b1e8ef104beed1b9dae532a970e2928e27ad71d69`
