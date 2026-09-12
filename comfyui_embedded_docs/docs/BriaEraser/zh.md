# Bria 擦除

Bria Eraser 使用 Bria API 从图像中移除对象或区域。你提供一张图像和一个掩码，该掩码勾勒出要移除的区域；节点会将两者上传到 Bria，运行擦除任务，等待其完成，并返回已编辑的图像，其中被掩码的区域已被擦除。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `image` | 包含要移除的对象或区域的输入图像。 | IMAGE | 是 | - |
| `mask` | 白色区域会被擦除，黑色区域会被保留。掩码在发送前会进行二值化，因此部分绘制的区域会被视为白色。必须与图像具有相同的宽高比。 | MASK | 是 | - |
| `mask_type` | 掩码来源类型。"manual" 用于手绘或画笔掩码；"automatic" 用于由分割模型（如 SAM）生成的掩码。 | COMBO | 是 | "manual"<br>"automatic" |
| `moderation` | 审核设置。设为 "true" 可对输入和/或输出图像启用视觉内容审核。 | DYNAMIC_COMBO | 是 | "false"<br>"true" |

当 `moderation` 设置为 "true" 时，两个额外的布尔设置可用：

- `visual_input_moderation` — 对输入图像应用视觉内容审核（默认：false）
- `visual_output_moderation` — 对输出图像应用视觉内容审核（默认：false）

注意：掩码必须与图像的宽高比匹配，否则请求会失败。掩码在发送到 API 之前会转换为二值（黑白）掩码：不透明度低于一半的绘制区域会被忽略，部分绘制的区域会被视为白色并会被擦除。掩码必须包含至少一些白色区域；空掩码会导致请求失败，因为没有可擦除的内容。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `image` | 已编辑的图像，其中被掩码的对象或区域已移除。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraser/zh.md)

---
**Source fingerprint (SHA-256):** `5528b7a3cb4d0a7b1b28acbc642a8bd21e2eacf5aa225403d6344c29f0cdba80`
