# 预览点云

预览点云节点允许您直接在 ComfyUI 界面中查看 3D 点云文件（例如 `.ply` 文件），而无需将其保存到输出目录。该节点将点云写入临时文件，在 3D 预览窗口中显示，并将模型数据、模型信息、相机信息、宽度和高度传递给后续处理。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 点云文件 (.ply) | FILE3D | 是 | - |
| `model_3d_info` | 3D 模型的信息。高级输入。未连接时，将使用 `viewport_state` 中存储的值。 | LOAD3DMODELINFO | 否 | - |
| `viewport_state` | 当前视口状态，可包含用于预览的相机信息和模型信息。 | LOAD3D | 是 | - |
| `camera_info` | 3D 视图的相机信息。高级输入。未连接时，将使用 `viewport_state` 中存储的值。 | LOAD3DCAMERA | 否 | - |
| `width` | 预览窗口的宽度（像素）（默认值：1024）。 | INT | 是 | 1 到 4096 |
| `height` | 预览窗口的高度（像素）（默认值：1024）。 | INT | 是 | 1 到 4096 |

注意：当 `camera_info` 或 `model_3d_info` 未连接时，节点将使用 `viewport_state` 中存储的值。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `model_3d` | 点云模型数据，原样传递。 | FILE3D |
| `model_3d_info` | 用于预览的 3D 模型的信息。 | LOAD3DMODELINFO |
| `camera_info` | 用于 3D 视图的相机信息。 | LOAD3DCAMERA |
| `width` | 预览窗口的宽度。 | INT |
| `height` | 预览窗口的高度。 | INT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/zh.md)

---
**Source fingerprint (SHA-256):** `a192096df29c4d7029f6e7f4f32e0a2f48de5b3d0cd437bd5b03d79e15eb0987`
