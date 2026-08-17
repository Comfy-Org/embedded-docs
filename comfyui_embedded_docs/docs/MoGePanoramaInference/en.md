# Run MoGe Panorama Inference

This node performs depth estimation on equirectangular panorama images. It works by splitting the panorama into 12 perspective views, running the MoGe depth estimation model on each view, and then merging the results back into a single, complete depth map for the original panorama.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `moge_model` | The MoGe model to use for inference. | MOGE_MODEL | Yes |  |
| `image` | Equirectangular panorama (any aspect). Accepts a single image only. | IMAGE | Yes |  |
| `resolution_level` | Per-view detail (0 = fastest, 9 = most detailed). Default: 9. | INT | Yes | 0 to 9 |
| `split_resolution` | Resolution of each perspective split. Default: 512. | INT | Yes | 256 to 1024 |
| `merge_resolution` | Long-side resolution of the merged equirect distance map. Default: 1920. | INT | Yes | 256 to 8192 |
| `batch_size` | Views per inference batch (12 splits total). Default: 4. | INT | Yes | 1 to 12 |

Note: This node accepts a single image only. Passing a batch of images raises an error. The panorama is always split into 12 perspective views; `batch_size` only controls how many of those views are processed per inference batch.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `moge_geometry` | A dictionary containing the estimated geometry: `points` (3D point cloud), `depth` (depth map), `mask` (valid area mask), and `image` (the input image). | MOGE_GEOMETRY |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/en.md)

---
**Source fingerprint (SHA-256):** `d35b6d42a5bb17c184bc56fe3867d3a183017084dc81649c0663a9fba2362770`
