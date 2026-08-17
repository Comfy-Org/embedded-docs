# AutogrowNamesTestNode

此节点用于测试 Autogrow 输入功能。它接受动态数量的浮点输入，每个输入都带有特定名称，并将其值合并为单个以逗号分隔的字符串。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `autogrow` | 一个动态输入组。您可以添加多个浮点输入，每个输入的名称从列表 "a"、"b" 或 "c" 中预定义。该节点接受这些命名输入的任意组合。 | FLOAT | 是 | N/A |

**注意：** `autogrow` 输入是动态的。您可以根据工作流需要添加或删除单个浮点输入（命名为 "a"、"b" 或 "c"）。节点会处理所有提供的值。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `output` | 一个字符串，包含所有提供的浮点输入的值，并以逗号连接。 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/zh.md)

---
**Source fingerprint (SHA-256):** `dac384c9486ac645d0d292fc891603cbfa6d362baa0a1e939c43257bbc0b06a0`
