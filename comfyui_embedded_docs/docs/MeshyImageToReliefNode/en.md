# Meshy: Image to Relief

This node turns a photo into a bas-relief model plus a 16-bit depth map for 3D printing, laser engraving and CNC carving. Dark artwork on a light background is raised and light areas stay low. Only the outputs you connect are generated and downloaded, so with no model output connected the task returns just the depth map.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `image` | Photo to convert into a relief. Dark artwork on a light background is raised. Transparency is dropped before upload, so flatten a transparent logo onto a white background first. | IMAGE | Yes | Single image |
| `relief_type` | Carving preset. `"low"` is a shallow carving for laser engraving, CNC work and plaques; `"high"` is deeper for 3D-printed pieces. The preset selects the `carving_depth_mm` value. | DYNAMIC_COMBO | Yes | `"low"`<br>`"high"` |
| `carving_depth_mm` | Depth of the carve in millimetres. Available when `relief_type` is set (default: 3.0 for `"low"`, 6.0 for `"high"`). | FLOAT | Yes | 0.1 to 60.0 (step 0.1) |
| `size_mm` | Length of the photo's longer side on the model in millimetres, measured flat before any bend (default: 60.0). | FLOAT | Yes | 20.0 to 250.0 (step 1.0) |
| `carving_mode` | `"emboss"` raises the nearer parts of the photo, `"engrave"` cuts them in. | COMBO | Yes | `"emboss"`<br>`"engrave"` |
| `base` | `"plate"` keeps a base plate under the relief, `"none"` cuts the background away and builds no plate. Selecting an option reveals its parameter. | DYNAMIC_COMBO | Yes | `"plate"`<br>`"none"` |
| `base_thickness_mm` | Thickness of the base plate in millimetres. Available when `base` is `"plate"` (default: 1.0). | FLOAT | Yes | 0.1 to 10.0 (step 0.1) |
| `removal_threshold` | Depth below which the background is cut away, on the 0 to 1 depth map. 0.3 keeps a bust whole, 0.8 breaks it into fragments. Available when `base` is `"none"` (default: 0.01). | FLOAT | Yes | 0.01 to 1.0 (step 0.01) |
| `bend` | `"convex"` bulges the front outward, `"concave"` curves it inward, `"off"` keeps the relief flat. Selecting a bend reveals `bend_axis` and `bend_angle`. | DYNAMIC_COMBO | Yes | `"off"`<br>`"convex"`<br>`"concave"` |
| `bend_axis` | `"xz"` curls the left and right edges, `"yz"` the top and bottom edges. Available when `bend` is `"convex"` or `"concave"`. | COMBO | Yes | `"xz"`<br>`"yz"` |
| `bend_angle` | Arc the bend spans in degrees; 360 closes the relief into a cylinder. Available when `bend` is `"convex"` or `"concave"` (default: 60.0). | FLOAT | Yes | 1.0 to 360.0 (step 1.0) |
| `seed` | Seed that controls whether the node re-runs; the result is non-deterministic regardless of the seed. Change it to request an output that was connected after the last run (default: 42). | INT | Yes | 0 to 2147483647 |
| `mesh_resolution` | Mesh points along the photo's longer side. At 1024 the GLB is about 50 MB and the STL about 105 MB, at 2048 about 200 MB and 420 MB; a bend doubles them. (default: 1024; advanced option) | INT | Yes | 512 to 2048 |
| `color_mapping` | Color the GLB, OBJ, FBX and USDZ files with the photo. STL and 3MF stay white. (default: False; advanced option) | BOOLEAN | Yes | True / False |

**Note:** A model format is only generated and downloaded when its output is connected. With no model output connected the task returns just the depth map, and `preview` alone still has the model generated for the thumbnail but returns no model file. `depth_map` keeps the full 16-bit range; Save Image (Advanced) writes it as a 16-bit PNG.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `GLB` | The relief model downloaded in GLB format. | FILE3DGLB |
| `STL` | The relief model downloaded in STL format. | FILE3DSTL |
| `OBJ` | The relief model downloaded in OBJ format. | FILE3DOBJ |
| `FBX` | The relief model downloaded in FBX format. | FILE3DFBX |
| `USDZ` | The relief model downloaded in USDZ format. | FILE3DUSDZ |
| `3MF` | The relief model downloaded in 3MF format. | FILE3D |
| `depth_map` | Depth map with the full 16-bit range; Save Image (Advanced) writes it as a 16-bit PNG. | IMAGE |
| `preview` | Thumbnail rendered by Meshy for the finished relief. | IMAGE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToReliefNode/en.md)

---
**Source fingerprint (SHA-256):** `6f2f0eb49074281b99d7ee10daf3bcc5616c6596c1c4d8491c72739550395f52`
