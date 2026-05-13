> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAttentionMultiply/en.md)

The CLIPAttentionMultiply node allows you to adjust the attention mechanism in CLIP models by applying multiplication factors to different components of the self-attention layers. It works by modifying the query, key, value, and output projection weights and biases in the CLIP model's attention mechanism. This experimental node creates a modified copy of the input CLIP model with the specified scaling factors applied.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Yes | - | The CLIP model to modify |
| `q` | FLOAT | Yes | 0.0 - 10.0 | Multiplication factor for query projection weights and biases (default: 1.0) |
| `k` | FLOAT | Yes | 0.0 - 10.0 | Multiplication factor for key projection weights and biases (default: 1.0) |
| `v` | FLOAT | Yes | 0.0 - 10.0 | Multiplication factor for value projection weights and biases (default: 1.0) |
| `out` | FLOAT | Yes | 0.0 - 10.0 | Multiplication factor for output projection weights and biases (default: 1.0) |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `CLIP` | CLIP | Returns a modified CLIP model with the specified attention scaling factors applied |

---
**Source fingerprint (SHA-256):** `43dab83ecfc928f3359eb7560658f43235bf3faa62c81084a2b4f482e3a4638f`
