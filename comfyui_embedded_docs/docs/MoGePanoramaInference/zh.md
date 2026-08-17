# MoGe 全景推理

此节点对等距柱状投影全景图像执行深度估计。其工作原理是将全景图分割为 12 个透视视图，在每个视图上运行 MoGe 深度估计模型，然后将结果合并回原始全景图的单一完整深度图。

## 输入
| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `moge_model` | 用于推理的 MoGe 模型。 | MOGE_MODEL | Yes |  |
| `image` | 等距柱状投影全景图（任意宽高比）。仅接受单张图像。 | IMAGE | Yes |  |
| `resolution_level` | 每个视图的细节（0 = 最快，9 = 最详细）。默认值：9。 | INT | Yes | 0 to 9 |
| `split_resolution` | 每个透视分割的分辨率。默认值：512。 | INT | Yes | 256 to 1024 |
| `merge_resolution` | 合并后的等距柱状投影距离图的长边分辨率。默认值：1920。 | INT | Yes | 256 to 8192 |
| `batch_size` | 每次推理批次处理的视图数（共 12 个分割）。默认值：4。 | INT | Yes | 1 to 12 |

注意：此节点仅接受单张图像。传入一批图像会引发错误。全景图始终被分割为 12 个透视视图；`batch_size` 仅控制每次推理批次处理其中多少个视图。

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `moge_geometry` | 一个包含估计几何信息的字典：`points`（3D 点云）、`depth`（深度图）、`mask`（有效区域掩码）和 `image`（输入图像）。 | MOGE_GEOMETRY |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/zh.md)

---
**Source fingerprint (SHA-256):** `d35b6d42a5bb17c184bc56fe3867d3a183017084dc81649c0663a9fba2362770`
