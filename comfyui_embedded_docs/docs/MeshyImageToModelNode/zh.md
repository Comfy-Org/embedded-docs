# Meshy：图像转模型

Meshy: Image to Model 节点使用 Meshy API 从单个输入图像生成 3D 模型。它会上传您的图像，提交处理任务，并返回生成的 3D 模型文件（GLB 和 FBX）以及任务 ID 以供参考。

## 输入
| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 指定用于生成的 AI 模型版本。 | COMBO | 是 | `"latest"` |
| `image` | 要转换为 3D 模型的输入图像。 | IMAGE | 是 | - |
| `should_remesh` | 当设置为 `"false"` 时，返回未经处理的三角网格。 | DYNAMIC_COMBO | 是 | `"true"`<br>`"false"` |
| `topology` | 重新网格化后的目标多边形拓扑。此输入仅在 `should_remesh` 设置为 `"true"` 时可用。 | COMBO | 否* | `"triangle"`<br>`"quad"` |
| `target_polycount` | 重新网格化后的目标多边形数量。此输入仅在 `should_remesh` 设置为 `"true"` 时可用。默认值：300000。 | INT | 否* | 100 - 300000 |
| `symmetry_mode` | 控制应用于生成的 3D 模型的对称性。 | COMBO | 是 | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | 决定是否生成纹理。设置为 `"false"` 时跳过纹理阶段并返回无纹理的网格。 | DYNAMIC_COMBO | 是 | `"true"`<br>`"false"` |
| `enable_pbr` | 除基础颜色外，还生成 PBR 贴图（金属度、粗糙度、法线）。此输入仅在 `should_texture` 设置为 `"true"` 时可用。默认值：`False`。 | BOOLEAN | 否* | - |
| `texture_prompt` | 提供文本提示以指导纹理生成过程。最多 600 个字符。不能与 `texture_image` 同时使用。此输入仅在 `should_texture` 设置为 `"true"` 时可用。默认值：空字符串。 | STRING | 否* | - |
| `texture_image` | 同一时间只能使用 `texture_image` 或 `texture_prompt` 中的一个。此输入仅在 `should_texture` 设置为 `"true"` 时可用。 | IMAGE | 否* | - |
| `pose_mode` | 指定生成模型的姿势模式。这是一个高级参数。 | COMBO | 是 | `""` (空)<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | 种子控制节点是否应重新运行；无论种子如何，结果都是非确定性的。默认值：0。 | INT | 是 | 0 - 2147483647 |

**参数约束说明：**

* `topology` 和 `target_polycount` 输入仅在 `should_remesh` 设置为 `"true"` 时可用。
* `enable_pbr`、`texture_prompt` 和 `texture_image` 输入仅在 `should_texture` 设置为 `"true"` 时可用。
* 当 `should_texture` 设置为 `"true"` 时，`texture_prompt` 和 `texture_image` 不能同时使用。如果同时提供，节点将引发错误。
* `texture_prompt` 的最大长度为 600 个字符。

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `模型文件` | 生成的 GLB 模型的文件名。仅为向后兼容而保留。 | STRING |
| `meshy_task_id` | Meshy API 任务的唯一标识符，可用于参考或故障排除。 | MESHY_TASK_ID |
| `GLB` | 以 GLB 文件格式生成的 3D 模型。 | FILE3DGLB |
| `FBX` | 以 FBX 文件格式生成的 3D 模型。 | FILE3DFBX |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/zh.md)

---
**Source fingerprint (SHA-256):** `9f7abcb0db3c78715e4ba7370efe294caf186590f7ab62da8568778848fc838c`
