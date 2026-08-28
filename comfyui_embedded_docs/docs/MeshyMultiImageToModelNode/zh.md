# Meshy：多图像转模型

该节点使用 Meshy API 从多张输入图像生成 3D 模型。它会上传提供的图像，提交处理任务，并返回生成的 3D 模型文件（GLB 和 FBX）以及用于参考的任务 ID。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 指定要使用的 AI 模型版本。 | COMBO | 是 | `"latest"` |
| `should_remesh` | 决定是否对生成的网格进行处理。设置为 `"false"` 时，节点返回未处理的三角网格；设置为 `"true"` 时，显示下方的重构设置。 | DYNAMIC_COMBO | 是 | `"true"`<br>`"false"` |
| `symmetry_mode` | 控制是否对生成的模型应用对称。 | COMBO | 是 | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | 决定是否生成纹理。设置为 `"false"` 时跳过纹理阶段并返回无纹理的网格；设置为 `"true"` 时，显示下方的纹理设置。 | DYNAMIC_COMBO | 是 | `"true"`<br>`"false"` |
| `pose_mode` | 指定生成模型的姿态模式。 | COMBO | 是 | `""`（空）<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | 种子控制节点是否应重新运行；无论种子如何，结果都是非确定性的。（默认值：0） | INT | 是 | 0 到 2147483647 |

### 重构设置（当 `should_remesh` 设置为 `"true"` 时可见）

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `topology` | 重构输出的目标多边形类型。 | COMBO | 否 | `"triangle"`<br>`"quad"` |
| `target_polycount` | 重构模型的目标多边形数量（默认值：300000）。 | INT | 否 | 100 到 300000 |

### 纹理设置（当 `should_texture` 设置为 `"true"` 时可见）

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `enable_pbr` | 除了基础颜色外，还生成 PBR 贴图（金属度、粗糙度、法线）。（默认值：False） | BOOLEAN | 否 | True / False |
| `texture_prompt` | 提供文本提示以引导纹理生成过程。最多 600 个字符。不能与 `texture_image` 同时使用。（默认值：空） | STRING | 否 | - |
| `texture_image` | `texture_image` 和 `texture_prompt` 只能同时使用其中一个。 | IMAGE | 否 | - |

### 图像输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `images` | 可增长插槽：连接 2 到 4 张输入图像（`image_1`、`image_2`、`image_3`、`image_4`）。这些图像用于生成 3D 模型。 | IMAGE | 是 | 2 到 4 张图像 |

**注意**

* 您必须为 `images` 输入提供 2 到 4 张图像。
* `topology` 和 `target_polycount` 参数仅在 `should_remesh` 设置为 `"true"` 时生效。
* `enable_pbr`、`texture_prompt` 和 `texture_image` 参数仅在 `should_texture` 设置为 `"true"` 时生效。
* `texture_prompt` 和 `texture_image` 互斥；不能同时使用两者。`texture_prompt` 限制为 600 个字符。
* `seed` 值不会使结果变得确定；更改它只会导致节点重新运行生成任务。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `模型文件` | 生成的 GLB 模型的文件名。此输出仅为向后兼容而提供。 | STRING |
| `meshy_task_id` | Meshy API 任务的唯一标识符。 | MESHY_TASK_ID |
| `GLB` | 生成的 GLB 格式 3D 模型。 | FILE3DGLB |
| `FBX` | 生成的 FBX 格式 3D 模型。 | FILE3DFBX |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/zh.md)

---
**Source fingerprint (SHA-256):** `c2282cad611bbbc8c0a618df6a68fcd9f6e3c29c6d08b2c96a117c29765d8a7a`
