# EndLoop

End Loop 标记循环块的结束。它收集循环体中最后一个节点产生的值，并根据 `accumulate` 设置，仅返回最终一次迭代或返回每一次迭代，同时还会将一个值传回 Start Loop，以便下一次迭代可以开始。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `output_value` | End Loop 返回的值。它会根据 `accumulate` 返回最终一次迭代或所有迭代。 | ANY | 否 | 任意值类型 |
| `next_iteration_value` | 从 End Loop 发送回 Start Loop 以供下一次迭代使用的值。 | ANY | 否 | 任意值类型 |
| `accumulate` | 启用时返回每次迭代的 `output_value`；否则仅返回最终一次迭代。 | BOOLEAN | 否 | `true`<br>`false`（默认：`false`） |
| `terminations` | 连接必须在每次迭代时执行的输出。它们的值不会被返回。可增长槽位，命名为 `termination_1`、`termination_2` 等。 | ANY | 否 | 0 到 50 个槽位 |

注意：`terminations` 是一个可增长的槽位列表，最少 0 个、最多 50 个连接。连接到此处的值会强制在每次迭代时执行，但不属于返回结果的一部分。

注意：此节点是输入列表节点，因此其输入会接收每次循环迭代收集到的值。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `outputs` | 最终一次迭代的 `output_value`；启用 `accumulate` 时，则为跨迭代累计的值。 | ANY (list) |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EndLoop/zh.md)

---
**Source fingerprint (SHA-256):** `473ba61d8e6fecdd1205297e2c602e3fd821044aff87d15a3f4b7646748d9999`
