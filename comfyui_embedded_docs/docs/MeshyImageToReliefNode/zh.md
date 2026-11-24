# Meshy: Image to Relief

此节点可将照片转换为浅浮雕模型，并生成用于 3D 打印、激光雕刻和 CNC 雕刻的 16 位深度图。浅色背景上的深色图案会被凸起，而浅色区域保持低凹。只有你连接的输出才会被生成和下载，因此在未连接任何模型输出的情况下，任务只返回深度图。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要转换为浮雕的照片。浅色背景上的深色图案会被凸起。上传前会丢弃透明通道，因此请先将透明标志平铺到白色背景上。 | IMAGE | 是 | 单张图像 |
| `relief_type` | 雕刻预设。`"low"` 为浅雕刻，适用于激光雕刻、CNC 加工和铭牌；`"high"` 则更深，适用于 3D 打印件。该预设决定 `carving_depth_mm` 的取值。 | DYNAMIC_COMBO | 是 | `"low"`<br>`"high"` |
| `carving_depth_mm` | 雕刻深度，单位为毫米。在设置 `relief_type` 后可用（默认值：`"low"` 为 3.0，`"high"` 为 6.0）。 | FLOAT | 是 | 0.1 到 60.0（步长 0.1） |
| `size_mm` | 模型上照片较长边的长度，单位为毫米，按未弯折时的平展状态测量（默认值：60.0）。 | FLOAT | 是 | 20.0 到 250.0（步长 1.0） |
| `carving_mode` | `"emboss"` 将照片中较近的部分凸起，`"engrave"` 则将其刻入。 | COMBO | 是 | `"emboss"`<br>`"engrave"` |
| `base` | `"plate"` 在浮雕下方保留底板，`"none"` 切除背景且不构建底板。选择某个选项后会显示其对应参数。 | DYNAMIC_COMBO | 是 | `"plate"`<br>`"none"` |
| `base_thickness_mm` | 底板的厚度，单位为毫米。当 `base` 为 `"plate"` 时可用（默认值：1.0）。 | FLOAT | 是 | 0.1 到 10.0（步长 0.1） |
| `removal_threshold` | 在 0 到 1 的深度图上，低于该深度值的背景会被切除。0.3 可保持半身像完整，0.8 会将其打散成碎片。当 `base` 为 `"none"` 时可用（默认值：0.01）。 | FLOAT | 是 | 0.01 到 1.0（步长 0.01） |
| `bend` | `"convex"` 使正面向外凸起，`"concave"` 使其向内弯曲，`"off"` 保持浮雕平整。选择弯折方式后会显示 `bend_axis` 和 `bend_angle`。 | DYNAMIC_COMBO | 是 | `"off"`<br>`"convex"`<br>`"concave"` |
| `bend_axis` | `"xz"` 卷曲左右边缘，`"yz"` 卷曲上下边缘。当 `bend` 为 `"convex"` 或 `"concave"` 时可用。 | COMBO | 是 | `"xz"`<br>`"yz"` |
| `bend_angle` | 弯折所跨越的圆弧角度，单位为度；360 会将浮雕闭合为圆柱。当 `bend` 为 `"convex"` 或 `"concave"` 时可用（默认值：60.0）。 | FLOAT | 是 | 1.0 到 360.0（步长 1.0） |
| `seed` | 控制节点是否重新运行的种子；无论种子为何，结果都是非确定性的。修改它可请求由上次运行之后才连接的输出所产生的结果（默认值：42）。 | INT | 是 | 0 到 2147483647 |
| `mesh_resolution` | 沿照片较长边的网格点数。为 1024 时 GLB 约 50 MB、STL 约 105 MB；为 2048 时分别约 200 MB 和 420 MB；启用弯折会使其翻倍。（默认值：1024；高级选项） | INT | 是 | 512 到 2048 |
| `color_mapping` | 用照片为 GLB、OBJ、FBX 和 USDZ 文件着色。STL 和 3MF 保持白色。（默认值：False；高级选项） | BOOLEAN | 是 | True / False |

**注意：** 只有当某个模型格式的输出被连接时，该格式才会被生成和下载。未连接任何模型输出时，任务只返回深度图；仅连接 `preview` 时，仍会为缩略图生成模型，但不返回模型文件。`depth_map` 保留完整的 16 位范围；Save Image (Advanced) 会将其写为 16 位 PNG。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `GLB` | 以 GLB 格式下载的浮雕模型。 | FILE3DGLB |
| `STL` | 以 STL 格式下载的浮雕模型。 | FILE3DSTL |
| `OBJ` | 以 OBJ 格式下载的浮雕模型。 | FILE3DOBJ |
| `FBX` | 以 FBX 格式下载的浮雕模型。 | FILE3DFBX |
| `USDZ` | 以 USDZ 格式下载的浮雕模型。 | FILE3DUSDZ |
| `3MF` | 以 3MF 格式下载的浮雕模型。 | FILE3D |
| `depth_map` | 具有完整 16 位范围的深度图；Save Image (Advanced) 会将其写为 16 位 PNG。 | IMAGE |
| `preview` | Meshy 为完成的浮雕渲染的缩略图。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToReliefNode/zh.md)

---
**Source fingerprint (SHA-256):** `6f2f0eb49074281b99d7ee10daf3bcc5616c6596c1c4d8491c72739550395f52`
