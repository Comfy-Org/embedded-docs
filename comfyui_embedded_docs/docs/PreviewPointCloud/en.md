# Preview Point Cloud

The Preview Point Cloud node lets you view a 3D point cloud file (such as a .ply file) directly in the ComfyUI interface without saving it to the output directory. The node writes the point cloud to a temporary file, displays it in a 3D preview window, and passes the model data, model information, camera information, width, and height through for further processing.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Point cloud file (.ply) | FILE3D | Yes | - |
| `model_3d_info` | Information about the 3D model. Advanced input. When not connected, the value stored in `viewport_state` is used. | LOAD3DMODELINFO | No | - |
| `viewport_state` | The current viewport state, which can contain camera information and model information used for the preview. | LOAD3D | Yes | - |
| `camera_info` | Camera information for the 3D view. Advanced input. When not connected, the value stored in `viewport_state` is used. | LOAD3DCAMERA | No | - |
| `width` | Width of the preview window in pixels (default: 1024). | INT | Yes | 1 to 4096 |
| `height` | Height of the preview window in pixels (default: 1024). | INT | Yes | 1 to 4096 |

Note: When `camera_info` or `model_3d_info` are not connected, the node uses the values stored in `viewport_state`.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `model_3d` | The point cloud model data, passed through unchanged. | FILE3D |
| `model_3d_info` | Information about the 3D model used for the preview. | LOAD3DMODELINFO |
| `camera_info` | Camera information used for the 3D view. | LOAD3DCAMERA |
| `width` | Width of the preview window. | INT |
| `height` | Height of the preview window. | INT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/en.md)

---
**Source fingerprint (SHA-256):** `a192096df29c4d7029f6e7f4f32e0a2f48de5b3d0cd437bd5b03d79e15eb0987`
