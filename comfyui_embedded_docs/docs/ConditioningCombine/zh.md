此节点将两个条件输入组合成单个输出，有效地合并它们的信息。

## 输入

| 参数名称 | 数据类型 | 作用 |
| --- | --- | --- |
| `conditioning_1` | `CONDITIONING` | 要组合的第一个条件输入。在组合过程中与conditioning_2扮演同等重要角色。 |
| `conditioning_2` | `CONDITIONING` | 要组合的第二个条件输入。在合并过程中与conditioning_1同等重要。 |

## 输出

| 参数名称 | 数据类型 | 作用 |
| --- | --- | --- |
| `CONDITIONING` | CONDITIONING | 组合conditioning_1和conditioning_2的结果，封装了合并后的信息。 |
