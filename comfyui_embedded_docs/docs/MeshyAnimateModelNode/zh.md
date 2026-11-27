# Meshy：动画模型

此节点使用 Meshy 服务对先前已绑定的 3D 角色应用特定的动画动作。它接收来自先前绑定操作的任务 ID 和一个动作 ID，以从库中选择所需的动画，然后以 GLB 和 FBX 两种文件格式返回带动画的模型。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `rig_task_id` | 来自先前完成的 Meshy 角色绑定操作的唯一任务 ID。 | MESHY_RIGGED_TASK_ID, STRING | 是 | N/A |
| `action_id` | 要应用的动画动作的 ID 编号。访问 https://docs.meshy.ai/en/api/animation-library 查看可用值列表。（默认值：0） | INT | 是 | 0 到 696 |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `model_file` | 带动画模型的字符串标识符。此输出仅为向后兼容而提供。 | STRING |
| `GLB` | GLB 格式的带动画 3D 模型文件。 | FILE3DGLB |
| `FBX` | FBX 格式的带动画 3D 模型文件。 | FILE3DFBX |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyAnimateModelNode/zh.md)

---
**Source fingerprint (SHA-256):** `d2fe5e62d8261880fe55cf305bc8bac4cb85367914d9ddfe2308ad1b43c85a16`
