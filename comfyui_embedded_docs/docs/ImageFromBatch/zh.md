`ImageFromBatch`节点设计用于根据提供的索引和长度从一批图像中提取特定段。它允许对批处理图像进行更细粒度的控制，使得可以对较大批次中的单个或子集图像执行操作。

## 输入

| 参数名称     | 数据类型 | 作用描述                                   |
| ------------ | -------- | ------------------------------------------ |
| `image`      | IMAGE    | 需要从中提取段的图像批次。此参数对于指定源批次至关重要。 |
| `batch_index`| INT      | 从批次中开始提取的起始索引。它决定了从批次中提取段的初始位置。 |
| `length`     | INT      | 从`batch_index`开始从批次中提取的图像数量。此参数定义了要提取的段的大小。 |

## 输出

| 参数名称 | 数据类型 | 作用描述                                     |
| -------- | -------- | -------------------------------------------- |
| `image`  | IMAGE    | 从指定批次中提取的图像段。此输出表示原始批次的一个子集，由`batch_index`和`length`参数确定。 |
