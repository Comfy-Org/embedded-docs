# Reve 图像编辑

Reve Image Edit 节点允许您基于文本描述修改现有图像。它使用 Reve API 解析您的指令，并对您提供的图像应用请求的更改。

## 输入
### 通用输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要编辑的图像。 | IMAGE | 是 | - |
| `edit_instruction` | 如何编辑图像的文本描述。最多 2560 个字符。（默认值：""） | STRING | 是 | 1 到 2560 字符 |
| `model` | 用于编辑的模型版本。 | DYNAMIC_COMBO | 是 | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"` |
| `upscale` | 放大生成的图像。可能会产生额外费用。（默认值："disabled"） | DYNAMIC_COMBO | 否 | `"disabled"`<br>`"enabled"` |
| `remove_background` | 从生成的图像中移除背景。可能会产生额外费用。（默认值：false） | BOOLEAN | 否 | `true`<br>`false` |
| `seed` | 种子控制节点是否应重新运行；无论种子如何，结果都是非确定性的。（默认值：0） | INT | 否 | 0 到 2147483647 |

### 模型输入

由 `reve-edit@20250915` 和 `reve-edit-fast@20251030` 模型共享。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model.aspect_ratio` | 输出图像的宽高比。设置为 `"auto"` 时，将自动确定宽高比。（默认值："auto"） | COMBO | 否 | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `model.test_time_scaling` | 数值越高，生成的图像越好，但消耗的积分越多。（默认值：1） | INT | 否 | 1 到 5 |

### 放大输入

当 `upscale` 设置为 `"enabled"` 时显示。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `upscale.upscale_factor` | 放大倍数（2x、3x 或 4x）。（默认值：2） | INT | 否 | 2 到 4 |

**注意：** 仅当 `upscale` 设置为 `"enabled"` 时，`upscale.upscale_factor` 参数才会出现。

## 输出
| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `image` | 根据指令生成的已编辑图像。 | IMAGE |

**注意：** 此节点已标记为已弃用。

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/zh.md)

---
**Source fingerprint (SHA-256):** `4001f3ab4cc4e705c235f578e90e497bb30d22110ef69b16fb072a91a65d15df`
