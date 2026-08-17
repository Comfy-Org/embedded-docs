# Preview Splat

The PreviewGaussianSplat node lets you preview a 3D gaussian splat file directly in the ComfyUI interface without saving it to the output directory. It temporarily stores the file in a temp folder, displays it in a 3D preview window, and passes the model data, camera information, and preview size through to other nodes.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | A gaussian splat 3D file. | FILE3D | Yes | splat, ply, spz, ksplat |
| `model_3d_info` | Optional metadata information about the 3D model. | LOAD3DMODELINFO | No | - |
| `viewport_state` | The current state of the 3D viewport, including camera and model information. | LOAD3D | Yes | - |
| `camera_info` | Optional camera information for the preview. | LOAD3DCAMERA | No | - |
| `width` | The width of the preview render in pixels (default: 1024). | INT | Yes | 1 to 4096 |
| `height` | The height of the preview render in pixels (default: 1024). | INT | Yes | 1 to 4096 |

Note: When `camera_info` or `model_3d_info` are not provided, the node uses the corresponding values from `viewport_state` instead.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `model_3d` | The input 3D gaussian splat file, passed through unchanged. | FILE3D |
| `model_3d_info` | Metadata information about the 3D model, either from the input or from the viewport state. | LOAD3DMODELINFO |
| `camera_info` | Camera information for the preview, either from the input or from the viewport state. | LOAD3DCAMERA |
| `width` | The width of the preview render. | INT |
| `height` | The height of the preview render. | INT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/en.md)

---
**Source fingerprint (SHA-256):** `7157a0b34d7bda3e7ec86cb2ac09e0e10ff96ea7037bb6c9d6ad2c879fdedbb2`
