# Meshy：文本生成模型

Meshy: Text to Model 节点使用 Meshy API 根据文本描述生成 3D 模型。它会在发送请求时将你的提示词和设置传给 API，然后等待生成完成并下载结果模型文件。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 指定要使用的 AI 模型版本。目前仅提供 "latest" 版本。 | COMBO | 是 | `"latest"` |
| `prompt` | 你想要生成的 3D 模型的文本描述。长度必须在 1 到 600 个字符之间。 | STRING | 是 | - |
| `style` | 生成 3D 模型的艺术风格。 | COMBO | 是 | `"realistic"`<br>`"sculpture"` |
| `should_remesh` | 控制是否处理生成后的网格。设为 "false" 时，节点返回未处理的三角网格；选择 "true" 会显示拓扑和多边形数量相关的额外参数。 | DYNAMIC_COMBO | 是 | `"true"`<br>`"false"` |
| `topology` | 重新网格化后的目标多边形类型。仅当 `should_remesh` 设为 "true" 时可用。 | COMBO | 否* | `"triangle"`<br>`"quad"` |
| `target_polycount` | 重新网格化后的目标多边形数量。默认值为 300000。仅当 `should_remesh` 设为 "true" 时可用。 | INT | 否* | 100 - 300000 |
| `symmetry_mode` | 控制生成模型中的对称性。这是一个高级参数。 | COMBO | 是 | `"auto"`<br>`"on"`<br>`"off"` |
| `pose_mode` | 指定生成模型的姿态模式。空字符串表示不请求特定姿态。这是一个高级参数。 | COMBO | 是 | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Seed 控制节点是否应重新运行；无论 seed 为何，结果都是非确定性的。默认值为 0。 | INT | 是 | 0 - 2147483647 |

*注意：`topology` 和 `target_polycount` 参数是条件性可用的。它们仅在 `should_remesh` 设为 "true" 时出现。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `模型文件` | 生成的 GLB 模型文件名。此输出用于向后兼容。 | STRING |
| `meshy_task_id` | Meshy API 任务的唯一标识符。 | MESHY_TASK_ID |
| `GLB` | 以 GLB 格式生成的 3D 模型文件。 | FILE3DGLB |
| `FBX` | 以 FBX 格式生成的 3D 模型文件。 | FILE3DFBX |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelNode/zh.md)

---
**Source fingerprint (SHA-256):** `1860b2d760aa81d611d4f44114591b4d98ccb85075bd1e06beabf462fb58bd53`
