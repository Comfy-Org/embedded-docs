# MoGe 点云映射到网格

此节点将 MoGe 点图转换为 3D 网格。它获取由 MoGe 深度估计节点生成的几何数据，并从中将一张图像三角化为具有 UV 坐标和可选纹理的网格。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `moge_geometry` | 包含点图、深度以及可选源图像的 MoGe 几何数据。 | MOGE_GEOMETRY | 是 | N/A |
| `batch_index` | 要对批处理 MoGe 几何中的哪张图像进行网格化。每张图像的顶点数不同，因此批次无法堆叠到单个 MESH 中（默认值：0）。 | INT | 是 | 0 to 4096 |
| `decimation` | 顶点步幅；1 = 全分辨率（默认值：1）。 | INT | 是 | 1 to 8 |
| `discontinuity_threshold` | 丢弃其 3x3 深度跨度超过此比例的像素。0 = 关闭（默认值：0.04）。 | FLOAT | 是 | 0.0 to 1.0 |
| `texture` | 将源图像作为 baseColor 纹理传递（默认值：True）。 | BOOLEAN | 是 | True/False |

注意：`batch_index` 必须小于所提供的 `moge_geometry` 的批次大小。输入几何必须包含点数据，如果生成的网格为空，则节点返回错误，建议设置 `discontinuity_threshold = 0`。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `MESH` | 具有顶点、面、UV 坐标以及可选源图像纹理的 3D 网格。 | MESH |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/zh.md)

---
**Source fingerprint (SHA-256):** `626925866eed6805d2ce87529909fc76b9484cd2e8118fdd1669a237d44b9b0b`
