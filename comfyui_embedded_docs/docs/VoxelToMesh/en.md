> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMesh/en.md)

The VoxelToMeshBasic node converts 3D voxel data into a mesh geometry by extracting a surface at a specified threshold value. It processes each voxel grid in the input and generates vertices and faces that form a 3D mesh representation.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `voxel` | VOXEL | Yes | - | The input voxel data to convert to mesh geometry |
| `threshold` | FLOAT | Yes | -1.0 to 1.0 | The threshold value for surface extraction (default: 0.6) |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `MESH` | MESH | The generated 3D mesh containing stacked vertices and faces from all input voxel grids |

---
**Source fingerprint (SHA-256):** `36df962c84c99a83f243a59b6387874e42e7d05323bd84079dbab112d2f1b67c`
