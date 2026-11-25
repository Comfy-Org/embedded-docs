# Recraft Vectorize Image Node

Generates SVG vector graphics from an input image. This node converts raster images into scalable vector format by sending each image to the Recraft API and combining the results into a single SVG output.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `image` | The input image to convert to SVG format. Supports batch processing of multiple images. | IMAGE | Yes | - |
| `version` | The vectorizer version: `v1` is the standard version, and `v1_pro` (Vectorizer Pro) gives cleaner SVGs with smooth curves, straight lines and sharp corners, best for lettering and intricate shapes (default: "v1"). | COMBO | No | "v1"<br>"v1_pro" |
| `shape_stacking` | How shapes are stacked in the SVG: `hierarchical` layers shapes on top of each other; `cut_out` makes shapes that never overlap, for plotters, vinyl cutters and screen printing (default: "hierarchical"). | COMBO | No | "hierarchical"<br>"cut_out" |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `SVG` | The generated vector graphics output combining all processed images into a single SVG document. | SVG |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftVectorizeImageNode/en.md)

---
**Source fingerprint (SHA-256):** `b7f8245de0597e8d3ceeef5a15b378e0903965a7e15c1825cacdf2387b278c7e`
