# Preview 3D (Advanced)

This node provides an advanced 3D model preview with camera and model information output. It previews a 3D model file without saving it to the ComfyUI output directory, writing the model to a temporary file for display in the UI. The model data, model information, camera information, and viewport dimensions are also passed through for further processing downstream.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 3D model file from an upstream 3D node. | FILE3D | Yes | GLB, GLTF, FBX, OBJ, STL, USDZ, or any supported 3D format |
| `model_3d_info` | Optional model information metadata. | LOAD3DMODELINFO | No | - |
| `viewport_state` | The current viewport state containing camera and model information. | LOAD3D | Yes | - |
| `camera_info` | Optional camera configuration for the 3D view. | LOAD3DCAMERA | No | - |
| `width` | The width of the preview in pixels. | INT | Yes | 1 to 4096 (default: 1024) |
| `height` | The height of the preview in pixels. | INT | Yes | 1 to 4096 (default: 1024) |

Note: When `camera_info` is not connected, the node uses the `camera_info` value from `viewport_state`. When `model_3d_info` is not connected, the node uses the `model_3d_info` value from `viewport_state`, or an empty list if the viewport state does not contain it.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `model_3d` | The 3D model file passed through from the input. | FILE3D |
| `model_3d_info` | Model information metadata, from the input or from the viewport state. | LOAD3DMODELINFO |
| `camera_info` | Camera configuration, from the input or from the viewport state. | LOAD3DCAMERA |
| `width` | The width of the preview in pixels. | INT |
| `height` | The height of the preview in pixels. | INT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/en.md)

---
**Source fingerprint (SHA-256):** `eda8c8fdd6ce7c39caf00c3054fc58e6dcab124fc3774d17af2deae651fbbf2e`
