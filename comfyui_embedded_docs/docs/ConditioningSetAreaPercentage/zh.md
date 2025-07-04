条件采样区域百分比设置节点专门用于根据百分比值调整条件元素的影响区域。它允许指定区域的尺寸和位置作为总图像尺寸的百分比，以及一个强度参数来调节条件效果的强度。

## 输入

| 参数名称 | 数据类型 | 作用 |
| --- | --- | --- |
| `CONDITIONING` | CONDITIONING | 表示要修改的条件元素，作为应用区域和强度调整的基础。 |
| `width` | `FLOAT` | 指定区域的宽度，作为总图像宽度的百分比，影响条件水平上影响图像的程度。 |
| `height` | `FLOAT` | 确定区域的高度，作为总图像高度的百分比，影响条件影响的垂直范围。 |
| `x` | `FLOAT` | 表示区域的水平起始点，作为总图像宽度的百分比，定位条件效果。 |
| `y` | `FLOAT` | 指定区域的垂直起始点，作为总图像高度的百分比，定位条件效果。 |
| `strength` | `FLOAT` | 控制指定区域内条件效果的强度，允许微调其影响。 |

## 输出

| 参数名称 | 数据类型 | 作用 |
| --- | --- | --- |
| `CONDITIONING` | CONDITIONING | 返回具有更新的区域和强度参数的修改后条件元素，准备进行进一步处理或应用。 |
