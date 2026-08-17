# AutogrowPrefixTestNode

AutogrowPrefixTestNode 是一个逻辑节点，用于测试自动扩展输入功能。它接受动态数量的浮点数输入，将其值组合成逗号分隔的字符串，并输出该字符串。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `autogrow` | 一个接受浮点数值的动态输入组。该组可包含 1 到 10 个浮点数输入，节点会处理所有提供的值。 | FLOAT | 是 | 1 to 10 inputs |

**注意：** `autogrow` 输入是一种特殊的动态输入，可以扩展以添加更多浮点数输入，最多 10 个。最少为 1 个输入。此节点中的 `min` 和 `max` 值定义的是该输入组允许的输入数量范围，而不是每个浮点数值的范围。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `output` | 一个字符串，包含所有输入的浮点数值，以逗号分隔。 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/zh.md)

---
**Source fingerprint (SHA-256):** `9b815f59961a4c661815f44b9c78e15e9084db1e4be89d502b9d92438f18e70b`
