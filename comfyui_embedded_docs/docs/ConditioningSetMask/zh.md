此节点设计通过应用具有指定强度的遮罩来修改生成模型的条件，允许对条件内的特定区域进行有针对性的调整，从而实现对生成过程更精确的控制。

## 输入

| 参数名称 | 数据类型 | 作用 |
| --- | --- | --- |
| `CONDITIONING` | CONDITIONING | 要修改的条件数据。它作为应用遮罩和强度调整的基础。 |
| `mask` | `MASK` | 一个遮罩张量，指定要在其中修改的条件区域。 |
| `strength` | `FLOAT` | 遮罩对条件的影响强度，允许对应用的修改进行微调。 |
| `set_cond_area` | COMBO[STRING] | 确定遮罩的效果是应用于默认区域还是由遮罩本身限定，提供在定位特定区域方面的灵活性。 |

## 输出

| 参数名称 | 数据类型 | 作用 |
| --- | --- | --- |
| `CONDITIONING` | CONDITIONING | 应用了遮罩和强度调整的修改后条件数据。 |
