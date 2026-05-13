> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/zh.md)

此节点通过处理最多四张展示物体不同视角的图像，使用 Tripo API 同步生成 3D 模型。它需要一张正面图像以及至少一个额外视角（左、后或右），以创建带有纹理和材质选项的完整 3D 模型。

## 输入

| 参数 | 数据类型 | 是否必填 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 物体的正面视角图像（必填） |
| `image_left` | IMAGE | 否 | - | 物体的左侧视角图像 |
| `image_back` | IMAGE | 否 | - | 物体的背面视角图像 |
| `image_right` | IMAGE | 否 | - | 物体的右侧视角图像 |
| `model_version` | COMBO | 否 | 提供多个选项 | 用于生成的模型版本 |
| `orientation` | COMBO | 否 | 提供多个选项 | 3D 模型的方向设置（默认值："default"） |
| `texture` | BOOLEAN | 否 | - | 是否为模型生成纹理（默认值：True） |
| `pbr` | BOOLEAN | 否 | - | 是否生成 PBR（基于物理的渲染）材质（默认值：True） |
| `model_seed` | INT | 否 | - | 模型生成的随机种子（默认值：42） |
| `texture_seed` | INT | 否 | - | 纹理生成的随机种子（默认值：42） |
| `texture_quality` | COMBO | 否 | `"standard"`<br>`"detailed"` | 纹理生成的质量级别（默认值："standard"） |
| `texture_alignment` | COMBO | 否 | `"original_image"`<br>`"geometry"` | 纹理与模型对齐的方法（默认值："original_image"） |
| `face_limit` | INT | 否 | -1 到 500000 | 生成模型的最大面数。设置为 -1 表示无限制（默认值：-1） |
| `quad` | BOOLEAN | 否 | - | 此参数已弃用，不执行任何操作（默认值：False） |
| `geometry_quality` | COMBO | 否 | `"standard"`<br>`"detailed"` | 几何体生成的质量级别（默认值："standard"） |

**注意：** 正面图像（`image`）始终为必填项。必须至少提供一张额外视角图像（`image_left`、`image_back` 或 `image_right`）以进行多视角处理。

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `model_file` | STRING | 生成的 3D 模型的文件路径或标识符（仅用于向后兼容） |
| `model task_id` | MODEL_TASK_ID | 用于跟踪模型生成过程的任务标识符 |
| `GLB` | FILE3DGLB | 以 GLB 格式生成的 3D 模型文件 |

---
**Source fingerprint (SHA-256):** `4ad433f4a0060d0ac2ce14463497db3168a1bf3348f17b98e958409e9a63baaf`
