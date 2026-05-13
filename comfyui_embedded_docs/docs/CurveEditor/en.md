> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CurveEditor/en.md)

The Curve Editor node provides a visual interface for adjusting and fine-tuning a curve. It allows you to modify the shape of an input curve and optionally visualize its distribution with a histogram. The node outputs the modified curve for use in other parts of your workflow.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `curve` | CURVE | Yes | N/A | The input curve to be edited. |
| `histogram` | HISTOGRAM | No | N/A | An optional histogram to display alongside the curve for visual reference. |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `curve` | CURVE | The edited curve after adjustments have been made in the node's interface. |

---
**Source fingerprint (SHA-256):** `34cf36a5b934c44ebfce0b81e7c515f1b31fb17f3b7e1ad52255d1d72f68240b`
