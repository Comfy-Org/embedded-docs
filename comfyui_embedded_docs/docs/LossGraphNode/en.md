> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/en.md)

The LossGraphNode creates a visual graph of training loss values over time and displays it as a preview image. It takes loss data from training processes and generates a line chart showing how the loss changes across training steps. The resulting graph includes axis labels and min/max loss values.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `loss` | LOSS_MAP | Yes | - | Loss map from training node. |
| `filename_prefix` | STRING | Yes | - | Prefix for the saved loss graph image. (default: "loss_graph") |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `ui.images` | IMAGE | The generated loss graph image displayed as a preview. |

---
**Source fingerprint (SHA-256):** `9b1c844cb4babafc61102ee7bfd1039c325c6665abff1721d92a6da7d18029f9`
