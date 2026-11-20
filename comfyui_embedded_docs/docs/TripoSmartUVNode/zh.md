# Tripo: Smart UV

Tripo: Smart UV 会重新展开模型的 UV，并将其贴图、绑定和动画重新映射到新的布局上。当模型的原始 UV 布局不可用时使用此节点，例如在重拓扑之后，或者需要重做贴图接缝时。输入模型不能超过 80,000 个三角面（一个四边形计为两个三角面），因此对于更大的模型，请先使用 Tripo: Retopology 或 `face_limit` 进行减面。

> **注意：** Tripo 在其服务器上保留任务记录 7 天（自 2026 年 12 月 1 日起生效）。超过该期限的任务 ID 将无法再解析，因此在窗口期之后重新运行已保存的工作流会在此节点失败。请重新运行前面的 Tripo 节点以创建新的任务 ID，或使用 **Tripo: Import Model** 重新导入已下载的模型。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | 要重新展开 UV 的模型的任务 ID。接受来自 Tripo 生成节点的模型任务 ID，或绑定、重定向或分割任务 ID。 | MODEL_TASK_ID | 是 | Tripo 任务 ID |
| `bake` | 将现有贴图烘焙到新的 UV 布局上。关闭时将跳过烘焙，返回不带颜色贴图的模型（默认：True）。 | BOOLEAN | 是 | `True`<br>`False` |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `model task_id` | 完成的 UV 任务的任务 ID。可传递给其他 Tripo 节点，例如 Tripo: Texture。 | MODEL_TASK_ID |
| `GLB` | 重新展开 UV 后的模型，GLB 格式。当源模型为 FBX 时为空。 | FILE_3D_GLB |
| `FBX` | 重新展开 UV 后的模型，FBX 格式。仅当源模型为 FBX 时才填充，例如四边形网格。 | FILE_3D_FBX |
| `UV atlas` | 模型渲染后的 UV 布局图像。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSmartUVNode/zh.md)

---
**Source fingerprint (SHA-256):** `55c9352c7c8129fa7a4f99f803bdc6db112830454e7d9566fa734063cb283532`
