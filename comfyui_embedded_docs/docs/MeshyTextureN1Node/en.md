# Meshy: Texture Model (N1)

This node textures a previously created 3D model with the Meshy N1 texture model, using 1 to 4 reference views of the same object. Connect the task ID of the original model plus the views; the node sends them to Meshy, waits for the job to finish and returns the textured model as GLB and FBX files together with the new task ID.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | The AI model used for the texturing job. Only `"meshy-n1"` is currently available. | COMBO | Yes | `"meshy-n1"` |
| `meshy_task_id` | Task ID of the previously created 3D model that should be textured. | MESHY_TASK_ID | Yes | N/A |
| `front_view` | The view Meshy treats as the front. One image textures the front and leaves the back plain; add back and side views in `extra_views` for a faithful back. | IMAGE | Yes | Single image |
| `extra_views` | Further views of the same object, in any order. Growable slot: connect 0 to 3 images (`view_1` ... `view_3`). Together with `front_view` at most 4 images. | IMAGE | No | 0 to 3 images |
| `enable_original_uv` | Use the original UV of the model instead of generating new UVs. When enabled, Meshy preserves existing textures from the uploaded model. If the model has no original UV, the quality of the output might not be as good. (default: True; advanced option) | BOOLEAN | No | True / False |

**Note:** `front_view` and `extra_views` may hold at most 4 images together; the node raises an error when more are connected. If a connected image carries a batch, each image in the batch counts toward that limit. The texture resolution is fixed at 2K and no PBR maps are generated.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `meshy_task_id` | Task ID of the texturing job, usable by later Meshy nodes. | MESHY_TASK_ID |
| `GLB` | The textured 3D model downloaded in GLB format. | FILE3DGLB |
| `FBX` | The textured 3D model downloaded in FBX format. | FILE3DFBX |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureN1Node/en.md)

---
**Source fingerprint (SHA-256):** `808df4f5a32b2d9ca6e74668051409836f2fcbc078d4ee3e85c07121d7a81f76`
