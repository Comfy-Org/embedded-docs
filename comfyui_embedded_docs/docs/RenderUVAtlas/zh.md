# RenderUVAtlas

将网格的 UV 布局渲染为图像。每个连通的 UV 区域（chart）以不同的颜色填充，chart 边界在深灰色背景上用黑色勾勒。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `mesh` | 要渲染其 UV 布局的 3D 网格。网格必须具有 UV 坐标，否则将引发错误。 | MESH | 是 | - |
| `resolution` | 渲染图像的宽度和高度（以像素为单位，默认值：1024）。 | INT | 是 | 64 到 4096（步长 64） |

注意：如果网格没有 UV 坐标，节点将引发错误 "mesh has no UVs to render. Run UnwrapMesh first."。如果网格包含批次维度（3D UV 或面数组），则仅渲染批次中的第一个项目。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `image` | 渲染后的 UV 图集图像，每个 chart 已着色，chart 边界边缘以黑色勾勒。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderUVAtlas/zh.md)

---
**Source fingerprint (SHA-256):** `b462101036418350390ffed621e583c6de14d5ea34d1e427342dc44ec3fd1922`
