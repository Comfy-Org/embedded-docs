> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageMergeTileList/en.md)

This node takes a list of image tiles and merges them back into a single, larger image. It is designed to reconstruct an image that was previously split into a grid of overlapping tiles, using a weighted blending technique to create a seamless final result.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `image_list` | IMAGE | Yes | N/A | A list of image tiles to be merged. The first tile in the list is used to determine the tile dimensions and data type for the entire process. |
| `final_width` | INT | Yes | 64 - 32768 | The width of the final merged image in pixels (default: 1024). |
| `final_height` | INT | Yes | 64 - 32768 | The height of the final merged image in pixels (default: 1024). |
| `overlap` | INT | Yes | 0 - 4096 | The amount of overlap between adjacent tiles in pixels. A value greater than 0 enables a smooth blending effect at the tile seams (default: 128). |

**Note:** The `image_list` is a dynamic input list. The node will process tiles in the order they are provided, up to the number required to fill the grid defined by the `final_width`, `final_height`, and the dimensions of the first tile. If the list contains more tiles than needed, the extra tiles are ignored.

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | The final merged image, reconstructed from the input tiles. |

---
**Source fingerprint (SHA-256):** `f8f770ca2e9806d2feb55bb1dfe2c26b09d7a3506caf664990d8536ec5660c92`
