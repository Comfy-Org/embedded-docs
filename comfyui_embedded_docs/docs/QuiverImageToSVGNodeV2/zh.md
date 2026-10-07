# Quiver Image to SVG

使用 Quiver AI 将栅格图像矢量化为可缩放矢量图形（SVG）。图像会发送至 Quiver AI 的 API，由该 API 返回矢量化结果。

选择 `model` 后，会显示下列模型特定参数。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 是否必需 | 取值范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用于 SVG 矢量化的模型。 | DYNAMIC_COMBO | 是 | `"arrow-2"`<br>`"arrow-2-telos"`<br>`"arrow-1.1"`<br>`"arrow-1.1-max"`<br>`"arrow-preview"` |
| `image` | 要矢量化的输入图像。 | IMAGE | 是 | N/A |
| `auto_crop` | 自动裁剪至主体对象。高级参数（默认值：False）。 | BOOLEAN | 是 | `True`<br>`False` |
| `target_size` | 在矢量化之前对输入图像应用的方形缩放尺寸，单位为像素，范围 128 到 4096。设为 0 则保持源尺寸，这比强制缩放能获得更干净的矢量化结果。此参数不会设置输出画布，如需设置请使用 `width` 和 `height`。高级参数（默认值：0）。 | INT | 是 | 0 到 4096 |
| `width` | 输出 SVG 画布（viewBox）的宽度，单位为用户单位。同时设置 `width` 和 `height` 可控制输出尺寸与宽高比；将任一参数留为 0 则由模型自行选择，通常会得到方形画布。高级参数（默认值：0）。 | INT | 是 | 0 到 8192 |
| `height` | 输出 SVG 画布（viewBox）的高度，单位为用户单位。同时设置 `width` 和 `height` 可控制输出尺寸与宽高比；将任一参数留为 0 则由模型自行选择，通常会得到方形画布。高级参数（默认值：0）。 | INT | 是 | 0 到 8192 |
| `seed` | 用于决定该节点是否重新运行的种子；无论种子值为何，实际结果都是不确定的。此参数具有 "control after generate" 功能（默认值：42）。 | INT | 是 | 0 到 2147483647 |

### 模型特定输入

| 参数 | 描述 | 数据类型 | 是否必需 | 取值范围 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 模型在绘制前投入的推理量。级别越高，细节越精细，但消耗的 token 也越多。仅 `"arrow-2"` 和 `"arrow-2-telos"` 模型使用（默认值：`"high"`）。 | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |
| `temperature` | 随机性控制。值越高，随机性越大。`"arrow-2-telos"` 模型不使用此参数。高级参数（默认值：1.0）。 | FLOAT | 是 | 0.0 到 2.0 （步长：0.1） |
| `top_p` | 核采样（nucleus sampling）参数。`"arrow-2-telos"` 模型不使用此参数。高级参数（默认值：1.0）。 | FLOAT | 是 | 0.05 到 1.0 （步长：0.05） |
| `presence_penalty` | token 存在惩罚。`"arrow-2-telos"` 模型不使用此参数。高级参数（默认值：0.0）。 | FLOAT | 是 | -2.0 到 2.0 （步长：0.1） |

**注意：** `target_size` 在矢量化之前应用，不会改变输出画布。将 `width` 或 `height` 留为 0，可让模型自行选择画布尺寸。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `SVG` | 矢量化后的 SVG 输出。 | SVG |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNodeV2/zh.md)

---
**Source fingerprint (SHA-256):** `186769b09bef2d2dbbfc26102f375ff80f8b324a24cd593da20afcea9cc2095b`
