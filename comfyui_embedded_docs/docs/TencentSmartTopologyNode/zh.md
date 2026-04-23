> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentSmartTopologyNode/zh.md)

此节点对 3D 模型执行智能重拓扑，这是一个自动创建新的、更简洁且多边形数量更少的网格的过程。它连接到腾讯混元 3D API 来处理模型，支持 GLB 和 OBJ 文件格式。该节点将处理后的模型以 OBJ 文件格式返回。

## 输入参数

| 参数名 | 数据类型 | 必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model_3d` | FILE3D | 是 | - | 输入的 3D 模型（GLB 或 OBJ）。文件必须是 GLB 或 OBJ 格式，且大小不能超过 200MB。 |
| `polygon_type` | STRING | 是 | `"triangle"`<br>`"quadrilateral"` | 表面构成类型。 |
| `face_level` | STRING | 是 | `"medium"`<br>`"high"`<br>`"low"` | 多边形简化级别。 |
| `seed` | INT | 否 | 0 到 2147483647 | 种子控制节点是否应重新运行；无论种子值如何，结果都是非确定性的。（默认值：0） |

**注意：** `seed` 参数用于触发节点的重新运行，但不能保证相同种子值会产生完全相同的最终输出。

## 输出结果

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `OBJ` | FILE3D | 经过拓扑优化的 3D 模型，以 OBJ 格式返回。 |