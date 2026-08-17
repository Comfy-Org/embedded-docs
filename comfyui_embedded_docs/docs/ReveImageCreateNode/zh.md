# Reve 图像生成

The Reve Image Create 节点使用 Reve AI 模型根据文本描述生成图像。它将文本提示发送到 Reve API 并返回生成的图像。您可以控制图像的宽高比，并应用可选的后处理效果，如放大和背景移除。此节点已弃用。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用于生成的模型版本。选择此模型将显示 `aspect_ratio` 和 `test_time_scaling` 设置。 | DYNAMIC_COMBO | 是 | `"reve-create@20250915"` |
| `prompt` | 所需图像的文本描述。最多 2560 个字符。默认值：空。 | STRING | 是 | 不适用 |
| `seed` | 种子用于控制节点是否应重新运行；无论种子如何，结果都是非确定性的。默认值：0。 | INT | 否 | 0 到 2147483647 |
| `upscale` | 放大生成的图像。可能会产生额外费用。设置为 `enabled` 时，将显示 `upscale_factor` 设置。默认值：`disabled`。 | DYNAMIC_COMBO | 否 | `"disabled"`<br>`"enabled"` |
| `remove_background` | 从生成的图像中移除背景。可能会产生额外费用。默认值：false。 | BOOLEAN | 否 | true<br>false |

### reve-create@20250915 输入

当 `model` 设置为 `"reve-create@20250915"` 时，将显示这些设置。

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | 输出图像的宽高比。 | COMBO | 是 | `"3:2"`<br>`"16:9"`<br>`"9:16"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | 数值越高，生成的图像质量越好，但消耗的积分也越多。默认值：1。 | INT | 否 | 1 到 5 |

### 放大输入

当 `upscale` 设置为 `"enabled"` 时，将显示这些设置。

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `upscale_factor` | 放大倍数（2 倍、3 倍或 4 倍）。默认值：2。 | INT | 否 | 2 到 4（步长 1） |

**注意：** `seed` 参数不能保证确定性输出。`upscale` 参数控制是否将放大作为后处理步骤应用。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `image` | Reve 模型根据输入提示生成的图像。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/zh.md)

---
**Source fingerprint (SHA-256):** `69178bc7d11e32ca179be5f598fbe60c4d41955b87e1c797e79cf224917a930c`
