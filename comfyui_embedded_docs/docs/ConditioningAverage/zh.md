`条件平均` 节点用于将两组不同的条件（如文本提示/Prompt）按照指定权重进行加权平均，生成介于两者之间的新条件。通过调整权重参数，可以灵活控制不同条件对最终结果的影响，非常适合于提示词插值、风格融合等高级用例。

如下图，通过调节`条件到` 的强度，可以输出介于两个条件之间的结果

![example](./asset/example.webp)

**示例说明**
`conditioning_to` 为 `条件到`
`conditioning_fro` 为 `条件从`
`Strength` 为 `条件到强度`

## 输入

| 参数名称 | 数据类型 | 说明 |
| --- | --- | --- |
| `条件到` | `CONDITIONING` | 目标条件向量，作为加权平均的主要基础。 |
| `条件从` | `CONDITIONING` | 源条件向量，将以一定权重混合到目标条件中。 |
| `条件到强度` | `FLOAT` | 目标条件的强度权重，范围 0.0-1.0，默认 1.0，步长 0.01。|

## 输出

| 参数名称 | 数据类型 | 说明 |
| --- | --- | --- |
| `条件` | `CONDITIONING` | 返回混合后的条件向量，反映加权平均结果。 |

## 典型应用场景

- **Prompt 插值**：在两个不同文本提示之间平滑过渡，生成中间风格或语义的内容。
- **风格融合**：结合不同艺术风格或语义条件，创造新颖效果。
- **强度调节**：通过调整权重，精确控制某一条件对结果的影响程度。
- **创意探索**：探索不同提示组合带来的多样化生成效果。
