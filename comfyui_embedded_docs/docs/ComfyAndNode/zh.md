# 与

## 概述

And 节点对一组输入值执行逻辑与运算。仅当所有提供的值都根据 Python 的真值规则判断为真（truthy）时，它才返回 `true`。此节点用于在继续操作之前检查多个条件是否同时满足。

## 输入

| 参数 | 说明 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `values` | 可扩展的值列表，用于求值。节点至少需要一个值，可以通过点击节点上的“+”按钮添加更多输入槽。每个输入槽可接受任何数据类型。 | ANY | 是 | 1 个或多个 |

**注意：** 节点使用 Python 的真值规则来判断值为 `true` 还是 `false`。例如，空字符串、数字 0、空列表和 `None` 均被视为 `false`。其他所有值均被视为 `true`。

## 输出

| 输出名称 | 说明 | 数据类型 |
| --- | --- | --- |
| `BOOLEAN` | 如果所有输入值均为真（truthy），则返回 `true`，否则返回 `false`。 | BOOLEAN |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyAndNode/zh.md)

---
**Source fingerprint (SHA-256):** `e7359c46da62f9859ea4f4a239cf20c565b5f7de22d280afc00c7ca321f1c89d`
