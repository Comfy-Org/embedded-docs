> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/en.md)

The PrimitiveBoundingBox node creates a simple rectangular area defined by its position and size. It takes X and Y coordinates for the top-left corner, along with width and height values, and outputs a bounding box data structure that can be used by other nodes in a workflow.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `x` | INT | Yes | 0 to 8192 | The X-coordinate for the top-left corner of the bounding box (default: 0). |
| `y` | INT | Yes | 0 to 8192 | The Y-coordinate for the top-left corner of the bounding box (default: 0). |
| `width` | INT | Yes | 1 to 8192 | The width of the bounding box (default: 512). |
| `height` | INT | Yes | 1 to 8192 | The height of the bounding box (default: 512). |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `bounding_box` | BOUNDING_BOX | A data structure containing the `x`, `y`, `width`, and `height` properties of the defined rectangle. |

---
**Source fingerprint (SHA-256):** `715f1a2bd650ecd6ba2ea3c1d54636bc32dff4fb4aec8f088ee9b0994809412c`
