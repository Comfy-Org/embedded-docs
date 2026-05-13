> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByShorterEdge/en.md)

This node resizes images so that the shorter edge matches a specified length while preserving the original aspect ratio. It calculates new dimensions based on the target length for the shorter side and returns the resized image.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Yes | - | The input image to be resized. |
| `shorter_edge` | INT | No | 1 to 8192 | Target length for the shorter edge. (default: 512) |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | The resized image with the shorter edge matching the specified target length. |

---
**Source fingerprint (SHA-256):** `011949390faa9032587aec210d9e38d55b79e474c7a6dcd5d3c0e75594a1fc29`
