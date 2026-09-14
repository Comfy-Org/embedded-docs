# StartLoop

Start Loop 节点在工作流中启动循环结构。它每次迭代运行一次连接的循环体，并可以通过三种方式对迭代进行计数：固定重复次数（simple）、数值索引范围（For）或对列表中的每一项执行一次（List）。每一轮都会公开当前索引、首/末标志，以及可选的可传递值，该值可以从一次迭代传递到下一次迭代。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `mode` | 循环迭代模式（默认："simple"）。所选的模式决定显示哪些附加参数。 | DYNAMIC_COMBO | 是 | `"simple"`<br>`"For"`<br>`"List"` |
| `cache_iterations` | 复用之前执行中未更改的迭代结果。禁用后，每次迭代都会重新执行。默认：false。 | BOOLEAN | 否 | true<br>false |
| `parent_iteration` | 连接外部 Start Loop 的 iteration_index 以嵌套此循环。此输入仅强制输入（需要链接）。 | INT | 否 | Any integer |
| `initial_iteration_value` | 在第一次迭代时作为 current_iteration_value 公开的值。 | ANY (type-matched) | 否 | Any value |

### Simple 模式输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `num_iterations` | 执行循环体的次数。默认：4。 | INT | 是 | Minimum 0 |

### For 模式输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `start_iteration_index` | 使用 For 循环模式时第一次迭代的索引。默认：0。 | INT | 是 | Any integer |
| `max_iteration` | For 模式下 iteration_index 的排他停止值。默认：4。 | INT | 是 | Maximum 0xffffffffffffffff |
| `step` | 使用 For 循环模式时每次迭代之间的索引步长。默认：1。 | INT | 是 | Minimum 1 |

### List 模式输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `list` | 循环迭代的项目列表。循环体对每个项目执行一次。 | ANY (type-matched list item) | 是 | Any list |

注意：

- 仅显示并使用属于当前所选 `mode` 的参数。
- 在 Simple 模式下，迭代索引从 0 运行到 `num_iterations` 减 1。在 For 模式下，索引从 `start_iteration_index` 运行到（但不包括）`max_iteration`，按 `step` 递增。在 List 模式下，`list` 中的每个项目运行一次迭代。
- `step` 不得为 0；值为 0 会引发错误。不允许低于 1 的值。
- 如果计算出的迭代次数为零，`is_last` 输出报告为 true，并且循环体不会运行。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `iteration_index` | 当前循环迭代的索引。 | INT |
| `is_first` | 在循环的第一次迭代期间为 true。 | BOOLEAN |
| `is_last` | 在循环的最后一次迭代期间为 true。 | BOOLEAN |
| `list_item` | 使用 List 模式时列表中的当前项目。在 Simple 和 For 模式下为 None。 | ANY (type-matched) |
| `current_iteration_value` | 当前迭代的循环传递值：第一次迭代时为 initial_iteration_value，之后每次迭代时为来自 End Loop 的 next_iteration_value。 | ANY (type-matched) |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StartLoop/zh.md)

---
**Source fingerprint (SHA-256):** `2584af9fd623f4762f440a043679e47aeef25ad0d571cfac11506cb513dd1b98`
