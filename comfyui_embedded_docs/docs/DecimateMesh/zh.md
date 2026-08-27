# DecimateMesh

DecimateMesh 使用二次误差度量（QEM）简化方法将 3D 网格简化为目标面数，并在当前计算设备上执行计算。`"midpoint"` 放置模式是 cumesh-faithful 预设，在保留头发等细小特征的同时提供最佳质量；而 `"qem"` 模式则将顶点放置在 QEM 最优位置，并提供可选的线条和特征边缘控制。输出网格保持焊接状态。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `mesh` | 要简化的 3D 网格。 | MESH | 是 | - |
| `target_face_count` | 目标最大面数。0 表示禁用。（默认：200000） | INT | 是 | 0 到 50000000 |
| `placement_mode` | midpoint：cumesh-faithful（推荐）。qem：QEM 最优放置。（默认：`"midpoint"`） | DYNAMIC_COMBO | 是 | `"midpoint"`<br>`"qem"` |

### Midpoint 输入

`"midpoint"` 放置模式不暴露额外的子参数；它使用默认的 midpoint 放置预设。

### QEM 输入

仅当 `placement_mode` 设置为 `"qem"` 时，以下子参数才会出现在界面中。

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `line_quadric_weight` | 每条边的线二次误差加权值；保留清晰的锐利边缘/谷线。0 表示关闭。（默认：0.0） | FLOAT | 否 | 0.0 到 100.0 |
| `feature_edge_quadric_weight` | 二面角特征边缘（折痕）上的额外二次误差加权值。0 表示关闭。（默认：0.0） | FLOAT | 否 | 0.0 到 1000.0 |
| `feature_edge_min_dihedral_deg` | 将一条边视为特征边缘的最小二面角（度）。（默认：30.0） | FLOAT | 否 | 0.0 到 180.0 |
| `clamp_v_to_edge` | 将 QEM 最优位置投影到折叠后的边段上。（默认：true） | BOOLEAN | 否 | `true`<br>`false` |

注意：当 `target_face_count` 为 0 或网格的面数已经少于目标时，将跳过简化。节点会显示面数减少摘要，例如 `faces: 1.23M → 200K (-84%)`。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `mesh` | 面数减少后的简化网格；连接性保持焊接状态。 | MESH |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DecimateMesh/zh.md)

---
**Source fingerprint (SHA-256):** `55336e5b52e27d940e5402ecd74fd0ac847a1c6acd35955eccf72aab8ed940f9`
