# Recraft 矢量化图像

从输入图像生成 SVG 矢量图形。此节点通过将每张图像发送到 Recraft API，并在单个 SVG 输出中返回结果，将栅格图像转换为可缩放矢量格式。该输出会为每张已处理图像保存一个单独的 SVG 文档；这些文档不会合并为一个。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `图像` | 要转换为 SVG 格式的输入图像。支持多张图像的批处理。 | IMAGE | 是 | - |
| `version` | 矢量化器版本：`v1` 是标准版本，`v1_pro`（Vectorizer Pro）可生成更干净的 SVG，具有平滑曲线、直线和锐角，最适合文字和复杂形状（默认："v1"）。 | COMBO | 否 | "v1"<br>"v1_pro" |
| `shape_stacking` | 形状在 SVG 中的堆叠方式：`hierarchical` 将形状逐层堆叠到彼此之上；`cut_out` 生成永不重叠的形状，适用于绘图仪、乙烯基切割机和丝网印刷（默认："hierarchical"）。 | COMBO | 否 | "hierarchical"<br>"cut_out" |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `SVG` | 生成的矢量图形。单个 SVG 输出会为每张已处理图像保存一个单独的 SVG 文档。 | SVG |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftVectorizeImageNode/zh.md)

---
**Source fingerprint (SHA-256):** `b7f8245de0597e8d3ceeef5a15b378e0903965a7e15c1825cacdf2387b278c7e`
