> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentSmartTopologyNode/en.md)

This node performs smart retopology on a 3D model, which is the process of automatically creating a new, cleaner mesh with a lower polygon count. It connects to a Tencent Hunyuan 3D API to process the model, supporting GLB and OBJ file formats. The node returns the processed model as an OBJ file.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `model_3d` | FILE3D | Yes | - | Input 3D model (GLB or OBJ). The file must be in GLB or OBJ format and cannot exceed 200MB. |
| `polygon_type` | STRING | Yes | `"triangle"`<br>`"quadrilateral"` | Surface composition type. |
| `face_level` | STRING | Yes | `"medium"`<br>`"high"`<br>`"low"` | Polygon reduction level. |
| `seed` | INT | No | 0 to 2147483647 | Seed controls whether the node should re-run; results are non-deterministic regardless of seed. (default: 0) |

**Note:** The `seed` parameter is used to trigger a re-run of the node, but the final output is not guaranteed to be the same for the same seed value.

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `OBJ` | FILE3D | The processed 3D model with optimized topology, returned in OBJ format. |