> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageToTileList/en.md)

The Split Image into List of Tiles node divides a single input image into a series of smaller, overlapping rectangular sections called tiles. It creates a batched list of these tiles, which can be processed individually by other nodes. The size of each tile and the amount of overlap between them can be specified.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Yes | - | The input image to be split into tiles. |
| `tile_width` | INT | Yes | 64 to 1048576 | The width of each output tile in pixels (default: 1024). |
| `tile_height` | INT | Yes | 64 to 1048576 | The height of each output tile in pixels (default: 1024). |
| `overlap` | INT | Yes | 0 to 4096 | The number of pixels that adjacent tiles will overlap (default: 128). |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | A batched list containing all the individual image tiles. |

---
**Source fingerprint (SHA-256):** `26991a325b7b9358cd7338348e93c57695b1ed1aa1983962794f889c94c34547`
