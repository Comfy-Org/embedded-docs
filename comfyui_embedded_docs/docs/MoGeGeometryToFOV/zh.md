# MoGeGeometryToFOV

此节点从 MoGe 几何对象中存储的相机内参推导视场角和焦距。它可以返回垂直、水平或对角视场角，单位为度或弧度。例如，垂直视场角输出可用于为 SAM3DBody_Predict 节点提供输入。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `moge_geometry` | MoGe 几何对象。它必须包含内参矩阵以及图像、点或深度数据中的至少一项，用于读取像素高度以进行焦距转换。 | MOGE_GEOMETRY | 是 | — |
| `axis` | 计算视场角所沿的轴："vertical"（fov_y）、"horizontal"（fov_x）或 "diagonal"（默认："vertical"）。 | COMBO | 是 | "vertical"<br>"horizontal"<br>"diagonal" |
| `unit` | 视场角的输出单位（默认："degrees"）。 | COMBO | 是 | "degrees"<br>"radians" |

注意：如果 `moge_geometry` 不包含内参（全景几何没有内参），或者既不包含图像、点也不包含深度数据，则节点会引发错误。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `fov` | 沿所选轴的视场角，单位为所选单位（度或弧度）。 | FLOAT |
| `focal_pixels` | 以像素为单位的镜头焦距，由垂直内参和像素高度推导得出。 | FLOAT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeGeometryToFOV/zh.md)

---
**Source fingerprint (SHA-256):** `983dc984847f93a8e002c73982571ecb38b7bae9c3dc4c201d9be17f785dcaed`
