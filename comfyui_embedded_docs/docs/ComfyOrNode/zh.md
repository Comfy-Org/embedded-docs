# 或

ComfyOrNode 对一组输入值执行逻辑或运算。如果根据 Python 标准真值判定规则，所提供的任意一个值被视为真（truthy），则返回 `true`。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `value` | 用于进行真值判定的值。您可以通过添加更多输入来提供多个值。如果这些值中的任意一个为真（truthy），节点将返回 `true`。 | ANY | 是 | 最少 1 个值；可接受多个值 |

**注意：** 该节点至少接受 1 个输入值。您可以根据需要使用自动扩展（autogrow）功能添加更多输入。

## 输出

| 输出名 | 描述 | 数据类型 |
| --- | --- | --- |
| `BOOLEAN` | 如果任意输入值为真（truthy），则返回 `true`；如果所有输入值均为假（falsy），则返回 `false`。 | BOOLEAN |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyOrNode/zh.md)

---
**Source fingerprint (SHA-256):** `f673aa2b0d754f55c51ba9c9ceea7d9de9a21d2e7308bd1281b4d4461243e4ad`
