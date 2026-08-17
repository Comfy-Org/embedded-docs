# 3D 预览（高级）

此节点提供高级 3D 模型预览，并输出相机与模型信息。它可预览 3D 模型文件，而无需将其保存到 ComfyUI 输出目录，而是将模型写入临时文件以在 UI 中显示。模型数据、模型信息、相机信息和视口尺寸也会被传递，以供下游进一步处理。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 来自上游 3D 节点的 3D 模型文件。 | FILE3D | 是 | GLB、GLTF、FBX、OBJ、STL、USDZ 或任何受支持的 3D 格式 |
| `model_3d_info` | 可选的模型信息元数据。 | LOAD3DMODELINFO | 否 | - |
| `viewport_state` | 包含相机和模型信息的当前视口状态。 | LOAD3D | 是 | - |
| `camera_info` | 用于 3D 视图的可选相机配置。 | LOAD3DCAMERA | 否 | - |
| `width` | 预览宽度（像素）。 | INT | 是 | 1 至 4096（默认值：1024） |
| `height` | 预览高度（像素）。 | INT | 是 | 1 至 4096（默认值：1024） |

注意：当 `camera_info` 未连接时，节点将使用 `viewport_state` 中的 `camera_info` 值。当 `model_3d_info` 未连接时，节点将使用 `viewport_state` 中的 `model_3d_info` 值；如果视口状态中不包含该值，则使用空列表。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `model_3d` | 从输入传递的 3D 模型文件。 | FILE3D |
| `model_3d_info` | 模型信息元数据，来自输入或视口状态。 | LOAD3DMODELINFO |
| `camera_info` | 相机配置，来自输入或视口状态。 | LOAD3DCAMERA |
| `width` | 预览宽度（像素）。 | INT |
| `height` | 预览高度（像素）。 | INT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/zh.md)

---
**Source fingerprint (SHA-256):** `eda8c8fdd6ce7c39caf00c3054fc58e6dcab124fc3774d17af2deae651fbbf2e`
