# Plot Loss Graph

The LossGraphNode creates a visual graph of training loss values over time and displays it as a preview image. It takes loss data from training processes and generates a line chart showing how the loss changes across training steps. The resulting graph includes axis labels and min/max loss values.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `loss` | Loss map from training node. Must contain a `loss` key with a list of loss values used to plot the graph. | LOSS_MAP | Yes | - |
| `filename_prefix` | Prefix for the saved loss graph image. (default: "loss_graph") | STRING | Yes | - |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `ui.images` | The generated loss graph image displayed as a preview. | IMAGE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/en.md)

---
**Source fingerprint (SHA-256):** `b1f0b72a03d4ce2d9461fc6e312bd1e847455f7dd5227667876a945494ea8cdb`
