> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/zh.md)

TripoConversionNode 使用 Tripo API 在不同文件格式之间转换 3D 模型。它接收来自先前 Tripo 操作（模型生成、骨骼绑定或重定向）的任务 ID，并将生成的模型转换为所需格式，并提供多种导出选项。

## 输入

| 参数 | 数据类型 | 是否必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID,RIG_TASK_ID,RETARGET_TASK_ID | 是 | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID | 来自先前 Tripo 操作（模型生成、骨骼绑定或重定向）的任务 ID |
| `format` | COMBO | 是 | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF | 转换后 3D 模型的目标文件格式 |
| `quad` | BOOLEAN | 否 | True/False | 是否将三角形转换为四边形（默认值：False） |
| `face_limit` | INT | 否 | -1 至 2000000 | 输出模型的最大面数，使用 -1 表示无限制（默认值：-1） |
| `texture_size` | INT | 否 | 128 至 4096 | 输出纹理的像素大小（默认值：4096） |
| `texture_format` | COMBO | 否 | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP | 导出纹理的格式（默认值：JPEG） |
| `force_symmetry` | BOOLEAN | 否 | True/False | 是否强制模型对称（默认值：False） |
| `flatten_bottom` | BOOLEAN | 否 | True/False | 是否展平模型底部（默认值：False） |
| `flatten_bottom_threshold` | FLOAT | 否 | 0.0 至 1.0 | 底部展平的阈值（默认值：0.0） |
| `pivot_to_center_bottom` | BOOLEAN | 否 | True/False | 是否将枢轴点移动到模型的底部中心（默认值：False） |
| `scale_factor` | FLOAT | 否 | 0.0 及以上 | 应用于模型的缩放因子（默认值：1.0） |
| `with_animation` | BOOLEAN | 否 | True/False | 导出时是否包含动画数据（默认值：False） |
| `pack_uv` | BOOLEAN | 否 | True/False | 是否打包 UV 坐标（默认值：False） |
| `bake` | BOOLEAN | 否 | True/False | 是否烘焙纹理（默认值：False） |
| `part_names` | STRING | 否 | 逗号分隔列表 | 要包含在导出中的部件名称列表，以逗号分隔（默认值：""） |
| `fbx_preset` | COMBO | 否 | blender<br>mixamo<br>3dsmax | 要使用的 FBX 导出预设（默认值：blender） |
| `export_vertex_colors` | BOOLEAN | 否 | True/False | 是否导出顶点颜色（默认值：False） |
| `export_orientation` | COMBO | 否 | align_image<br>default | 导出方向模式（默认值：default） |
| `animate_in_place` | BOOLEAN | 否 | True/False | 是否在原地对模型进行动画处理（默认值：False） |

**注意：** `original_model_task_id` 必须是来自先前 Tripo 操作（模型生成、骨骼绑定或重定向）的有效任务 ID。标记为“高级”的参数为可选参数，仅需根据特定的导出要求进行配置。

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| *无命名输出* | - | 此节点异步处理转换，并通过 Tripo API 系统返回结果 |

---
**Source fingerprint (SHA-256):** `b11ecab98701b7153a350f5e4980ddc2f446c0a12be3402ca98a5e6de60bd7ce`
