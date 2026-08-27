# RenderMesh

此节点通过光线投射单个视图，将 3D 网格渲染为 2D 图像。它可以输出带纹理的网格、顶点颜色、实体着色表面、表面法线或深度。相机和可选的模型变换可来自 Load3D / Preview3D 查看器；如果未连接相机，则将自动取景为默认的前视图。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `mesh` | 要渲染的 3D 网格。 | MESH | 是 | — |
| `mode` | 要渲染的内容。auto：如果存在纹理则渲染纹理，否则渲染顶点颜色，再否则渲染着色黏土。（默认值："auto"） | COMBO | 是 | `"auto"`<br>`"texture"`<br>`"vertex colors"`<br>`"solid"`<br>`"normal"`<br>`"depth"` |
| `width` | 渲染图像的宽度（像素）。（默认值：1024） | INT | 是 | 64 to 4096 (step 8) |
| `height` | 渲染图像的高度（像素）。（默认值：1024） | INT | 是 | 64 to 4096 (step 8) |
| `background` | 网格未覆盖的像素所使用的背景颜色。（默认值："#000000"） | COLOR | 是 | — |
| `model_3d_info` | 来自同一 Load3D / Preview3D 查看器的模型变换。将其与 `camera_info` 连接以匹配查看器的取景。 | LOAD3D_MODEL_INFO | 否 | — |
| `camera_info` | 来自 Load3D / Preview3D 查看器或 Create Camera Info 节点的相机。如果未连接任何相机，将自动取景为默认的前视图。 | LOAD3D_CAMERA | 否 | — |

注意：仅渲染批处理网格中的第一个项目——如果网格批次包含多个项目，节点会记录警告并使用第一个项目。`texture` 模式要求网格同时具有纹理和 UV，`vertex colors` 模式要求网格具有顶点颜色；如果所选模式所需的数据不可用，节点将回退到实体着色渲染。`model_3d_info` 和 `camera_info` 应同时连接自同一 Load3D / Preview3D 查看器，以使渲染结果与查看器的取景一致。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `image` | 网格的渲染图像。 | IMAGE |
| `mask` | 一个遮罩，在网格被渲染的位置为 1.0，在其他位置为 0.0。 | MASK |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderMesh/zh.md)

---
**Source fingerprint (SHA-256):** `d23e85a904520eb2dfed899eb3e6a9cf45c980df00c034503687ac4eccc66ac4`
