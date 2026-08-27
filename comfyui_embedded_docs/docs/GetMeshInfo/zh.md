# GetMeshInfo

Get Mesh Info 节点会报告网格中的顶点数和面数，以及其包含的属性（如 UV、顶点颜色、法线和纹理）。报告显示在节点上，并作为文本输出返回，而网格本身保持不变。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `mesh` | 要检查的网格。该节点对其顶点和面进行计数，检测存在哪些属性，并原样传递该网格。 | MESH | 是 | — |

注意：当输入包含多个网格（一个批次）时，报告会显示整个批次的总顶点数和总面数，以及按网格细分的明细。对于零填充批次，则使用存储在网格数据中的每项计数。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `mesh` | 原始网格，未做任何修改地传递。 | MESH |
| `info` | 包含顶点数、面数和检测到的属性（uvs、vertex_colors、normals、tangents、texture、metallic_roughness、normal_map）的多行文本报告。大数值使用逗号格式化，例如 "1,234,567 (1.23M)"。相同文本也会显示在节点上。 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetMeshInfo/zh.md)

---
**Source fingerprint (SHA-256):** `cd168a5e69131a4a37f1f47014af2bc2ac2c8aa69e146cf33c2072480b35ebb2`
