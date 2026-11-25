# Meshy: Texture Model (N1)

此节点使用 Meshy N1 纹理模型，通过同一物体的 1 到 4 张参考视图，为先前创建的 3D 模型添加纹理。连接原始模型的任务 ID 以及这些视图；节点会将它们发送至 Meshy，等待任务完成，然后返回带纹理的模型（GLB 和 FBX 文件）以及新的任务 ID。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用于纹理生成任务的 AI 模型。目前仅提供 `"meshy-n1"`。 | COMBO | 是 | `"meshy-n1"` |
| `meshy_task_id` | 先前创建的、需要添加纹理的 3D 模型的任务 ID。 | MESHY_TASK_ID, STRING | 是 | N/A |
| `front_view` | Meshy 视为正面的视图。仅提供一张图像时，只会为正面添加纹理，背面保持空白；可在 `额外视图` 中添加背面和侧面视图，以获得真实的背面效果。 | IMAGE | 是 | 单张图像 |
| `额外视图` | 同一物体的更多视图，顺序不限。可增长的槽位：连接 0 到 3 张图像（`view_1` ... `view_3`）。与 `front_view` 合计最多 4 张图像。 | IMAGE | 否 | 0 到 3 张图像 |
| `enable_original_uv` | 使用模型的原始 UV，而不是生成新的 UV。启用后，Meshy 会保留所上传模型中已有的纹理。如果模型没有原始 UV，输出质量可能不够理想。（默认：True；高级选项） | BOOLEAN | 否 | True / False |

**注意：** `front_view` 和 `额外视图` 合计最多可包含 4 张图像；连接更多图像时节点会报错。如果所连接的图像带有批次（batch），则该批次中的每张图像都会计入此限制。纹理分辨率固定为 2K，且不会生成 PBR 贴图。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `meshy_task_id` | 纹理生成任务的任务 ID，可供后续 Meshy 节点使用。 | MESHY_TASK_ID, STRING |
| `GLB` | 以 GLB 格式下载的带纹理 3D 模型。 | FILE3DGLB |
| `FBX` | 以 FBX 格式下载的带纹理 3D 模型。 | FILE3DFBX |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureN1Node/zh.md)

---
**Source fingerprint (SHA-256):** `be4191fd091839cfdce82b4f41fc6ae9e70f7b5b5504eb14a3c0d741d25ac8fd`
