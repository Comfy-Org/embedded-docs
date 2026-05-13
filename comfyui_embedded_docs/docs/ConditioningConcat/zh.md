> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningConcat/zh.md)

ConditioningConcat 节点用于拼接条件向量，具体操作是将 'conditioning_from' 向量合并到 'conditioning_to' 向量中。当需要将来自两个来源的条件信息合并为统一的表示时，此操作至关重要。

## 输入

| 参数 | Comfy 数据类型 | 描述 |
|------|----------------|------|
| `conditioning_to` | `CONDITIONING` | 表示主要条件向量集，'conditioning_from' 向量将拼接至此。它作为拼接过程的基础。 |
| `conditioning_from` | `CONDITIONING` | 包含待拼接至 'conditioning_to' 向量的条件向量。此参数允许将额外的条件信息集成到现有集合中。 |

## 输出

| 参数 | Comfy 数据类型 | 描述 |
|------|----------------|------|
| `conditioning` | `CONDITIONING` | 输出为统一的条件向量集，由 'conditioning_from' 向量拼接至 'conditioning_to' 向量后得到。 |