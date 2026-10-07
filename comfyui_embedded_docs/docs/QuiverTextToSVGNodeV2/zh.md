# Quiver Text to SVG

使用 Quiver AI 从文本提示生成可缩放矢量图形（SVG）。可选的参考图像和风格说明可以指导生成。

选择 `model` 会显示下面列出的模型特定参数，参考图像的最大数量也取决于所选模型。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用于 SVG 生成的模型。 | DYNAMIC_COMBO | 是 | `"arrow-2"`<br>`"arrow-2-telos"`<br>`"arrow-1.1"`<br>`"arrow-1.1-max"`<br>`"arrow-preview"` |
| `prompt` | 所需 SVG 输出的文本描述。必须包含至少一个非空白字符（默认：空）。 | STRING | 是 | 任意文本 |
| `instructions` | 附加的风格或格式指导。可选高级参数（默认：空）。 | STRING | 否 | 任意文本 |
| `reference_images` | 可增长槽位：连接一个或多个可选的参考图像（`ref_1`、`ref_2`、...），用于指导生成。最大图像数量取决于所选模型。 | IMAGE | 否 | 最多 14<br>最多 4 |
| `width` | 输出 SVG 画布（viewBox）的宽度，以用户单位表示。同时设置 `width` 和 `height` 以控制输出尺寸和宽高比；将任一值设为 0 让模型选择，通常会得到方形画布。高级参数（默认：0）。 | INT | 是 | 0 到 8192 |
| `height` | 输出 SVG 画布（viewBox）的高度，以用户单位表示。同时设置 `width` 和 `height` 以控制输出尺寸和宽高比；将任一值设为 0 让模型选择，通常会得到方形画布。高级参数（默认：0）。 | INT | 是 | 0 到 8192 |
| `seed` | 用于确定节点是否应重新运行的种子；无论种子值如何，实际结果都是非确定性的。此参数具有“生成后控制”功能（默认：42）。 | INT | 是 | 0 到 2147483647 |

### 模型特定输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 模型在绘制前花费的推理力度。更高的级别可提高细节，但会消耗更多 token。仅由 `"arrow-2"` 和 `"arrow-2-telos"` 模型使用（默认：`"high"`）。 | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |
| `temperature` | 随机性控制。更高的值会增加随机性。`"arrow-2-telos"` 模型不使用。高级参数（默认：1.0）。 | FLOAT | 是 | 0.0 到 2.0（步长 0.1） |
| `top_p` | 核采样参数。`"arrow-2-telos"` 模型不使用。高级参数（默认：1.0）。 | FLOAT | 是 | 0.05 到 1.0（步长 0.05） |
| `presence_penalty` | Token 存在惩罚。`"arrow-2-telos"` 模型不使用。高级参数（默认：0.0）。 | FLOAT | 是 | -2.0 到 2.0（步长 0.1） |

**注意：** 对于 `"arrow-2"`、`"arrow-2-telos"` 和 `"arrow-1.1-max"`，`reference_images` 的最大数量为 14；对于 `"arrow-1.1"` 和 `"arrow-preview"`，为 4。将 `width` 或 `height` 保留为 0，让模型选择画布尺寸。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `SVG` | 生成的 SVG 输出。 | SVG |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNodeV2/zh.md)

---
**Source fingerprint (SHA-256):** `809d2e5bd62386723e36b7649af2f8dda40b437dc39bac9236529db5b52d32e9`
