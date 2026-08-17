# 预览 Splat

PreviewGaussianSplat 节点允许您直接在 ComfyUI 界面中预览 3D 高斯溅射文件，而无需将其保存到输出目录。它会将文件临时存储在临时文件夹中，在 3D 预览窗口中显示，并将模型数据、相机信息和预览尺寸传递给其他节点。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 高斯溅射 3D 文件。 | FILE3D | 是 | splat, ply, spz, ksplat |
| `model_3d_info` | 关于 3D 模型的可选元数据信息。 | LOAD3DMODELINFO | 否 | - |
| `viewport_state` | 3D 视口的当前状态，包括相机和模型信息。 | LOAD3D | 是 | - |
| `camera_info` | 用于预览的可选相机信息。 | LOAD3DCAMERA | 否 | - |
| `width` | 预览渲染的宽度（像素），默认值：1024。 | INT | 是 | 1 to 4096 |
| `height` | 预览渲染的高度（像素），默认值：1024。 | INT | 是 | 1 to 4096 |

注意：当未提供 `camera_info` 或 `model_3d_info` 时，节点将改用 `viewport_state` 中的相应值。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `model_3d` | 输入的 3D 高斯溅射文件，原样传递。 | FILE3D |
| `model_3d_info` | 有关 3D 模型的元数据信息，来自输入或视口状态。 | LOAD3DMODELINFO |
| `camera_info` | 用于预览的相机信息，来自输入或视口状态。 | LOAD3DCAMERA |
| `width` | 预览渲染的宽度。 | INT |
| `height` | 预览渲染的高度。 | INT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/zh.md)

---
**Source fingerprint (SHA-256):** `7157a0b34d7bda3e7ec86cb2ac09e0e10ff96ea7037bb6c9d6ad2c879fdedbb2`
