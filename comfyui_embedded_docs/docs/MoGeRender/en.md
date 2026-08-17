# Render MoGe Geometry

## Overview

This node takes a MOGE_GEOMETRY packet (produced by a MoGe depth/normal estimation node) and renders it into a standard image format. You can choose to output a depth map, a colored depth map, a normal map, or a mask.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `moge_geometry` | The geometry data packet from a MoGe estimation node. | MOGE_GEOMETRY | Yes | N/A |
| `output` | The type of image to render from the geometry data. DirectX vs OpenGL controls the normal-map green-channel convention. DirectX: green = -Y down (Unreal). OpenGL: green = +Y up (Blender, Substance, Unity, glTF). (default: "depth") | COMBO | Yes | `"depth"`<br>`"depth_colored"`<br>`"normal_opengl"`<br>`"normal_directx"`<br>`"mask"` |

**Note:** The selected `output` mode determines which data must be present in `moge_geometry`:
- `depth` and `depth_colored` require depth data. The depth is converted to a normalized disparity (1/depth) map using 0.1/99.9 percentile clipping.
- `normal_opengl` and `normal_directx` require normal data, or point data from which normals can be derived. The node raises an error if neither is present.
- `mask` requires mask data.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `IMAGE` | The rendered image as a batch of RGB tensors. The content depends on the `output` mode: a grayscale depth map, a colored depth map, a normal map, or a mask. | IMAGE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/en.md)

---
**Source fingerprint (SHA-256):** `ca602f7a7d6eb1b1d00986459621d94ecf9331266ff1d3ce7bb759d24448a346`
