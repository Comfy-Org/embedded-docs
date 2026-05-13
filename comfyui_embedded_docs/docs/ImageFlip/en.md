> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFlip/en.md)

The ImageFlip node flips images along different axes. It can flip images vertically along the x-axis or horizontally along the y-axis. The node uses torch.flip operations to perform the flipping based on the selected method.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Yes | - | The input image to be flipped |
| `flip_method` | STRING | Yes | "x-axis: vertically"<br>"y-axis: horizontally" | The flipping direction to apply (default: "x-axis: vertically") |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | The flipped output image |

---
**Source fingerprint (SHA-256):** `5cb9949c53653192b1a696179351976c3a87e2e7afc4634624b4d827ad75b527`
