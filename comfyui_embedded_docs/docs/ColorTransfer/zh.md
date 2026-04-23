> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorTransfer/zh.md)

ColorTransfer 节点通过调整目标图像的色彩调色板，使其与参考图像的色彩相匹配。它采用不同的数学算法来分析和传递参考图像到目标图像的颜色特征，例如亮度、对比度和色调分布。这对于在多张图像之间创建视觉一致性或应用特定的色彩分级非常有用。

## 输入参数

| 参数名 | 数据类型 | 必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image_target` | IMAGE | 是 | - | 要应用色彩变换的目标图像。 |
| `image_ref` | IMAGE | 否 | - | 用于匹配色彩的参考图像。如果未提供，则跳过处理并返回未更改的目标图像。 |
| `method` | COMBO | 是 | `"reinhard_lab"`<br>`"mkl_lab"`<br>`"histogram"` | 要使用的色彩传递算法。 |
| `source_stats` | DYNAMICCOMBO | 是 | `"per_frame"`<br>`"uniform"`<br>`"target_frame"` | 确定如何从源（目标）图像计算色彩统计信息。 |
| `strength` | FLOAT | 是 | 0.0 到 10.0 | 色彩传递效果的强度。值为 1.0 时应用完整的变换，值为 0.0 时返回原始图像。默认值：1.0 |

**参数详情：**
*   **`source_stats` 选项：**
    *   **`per_frame`**：批次中的每一帧都单独与 `image_ref` 进行匹配。
    *   **`uniform`**：汇集所有源帧的色彩统计信息以创建单一基准，然后与 `image_ref` 进行匹配。
    *   **`target_frame`**：使用目标批次中选择的一帧作为计算到 `image_ref` 变换的基准。然后，此变换将统一应用于所有帧，从而保留它们之间的相对色彩差异。选择此选项时，会额外出现一个 `target_index` 参数。
*   **`target_index`**（当 `source_stats` 为 `"target_frame"` 时出现）：用作计算变换的源基准的帧索引（从 0 开始）。默认值：0。必须在 0 到 10000 之间。

**约束条件：**
*   如果未提供 `image_ref` 或将 `strength` 设置为 0.0，节点将返回未经处理的原始 `image_target`。
*   当 `source_stats` 设置为 `"target_frame"` 时，`target_index` 必须是 `image_target` 批次中的有效索引。如果超出帧数，则使用最后一帧。
*   对于 `source_stats` 设置为 `"per_frame"` 的 `histogram` 方法，如果 `image_ref` 的批次大小大于 1，则每个目标帧将按索引与相应的参考帧匹配。如果参考批次只有一帧，则该帧将用于所有目标帧。

## 输出参数

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `image` | IMAGE | 应用色彩传递后得到的图像。 |