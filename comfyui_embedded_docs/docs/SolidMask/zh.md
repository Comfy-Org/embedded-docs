
纯块遮罩节点用于生成一个具有指定值的均匀纯色的遮罩，覆盖其整个区域。它旨在创建具有特定尺寸和强度的遮罩，在各种图像处理和遮罩任务中非常有用。

## 输入

| 参数名称 | 数据类型 | 作用 |
| --- | --- | --- |
| `value` | FLOAT | 指定遮罩的强度值，影响其整体外观以及在后续操作中的实用性。 |
| `width` | INT | 确定生成遮罩的宽度，直接影响其大小和宽高比。 |
| `height` | INT | 设置生成遮罩的高度，影响其大小和宽高比。 |

## 输出

| 参数名称 | 数据类型 | 作用 |
| --- | --- | --- |
| `mask` | MASK | 输出一个具有指定尺寸和值的均匀遮罩。 |
