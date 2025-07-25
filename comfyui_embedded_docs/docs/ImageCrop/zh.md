此节点设计用于根据指定的宽度和高度以及给定的 x 和 y 坐标对图像进行裁剪。这一功能对于聚焦于图像的特定区域或调整图像大小以满足某些要求至关重要。

## 输入

| 参数名称 | 数据类型 | 作用 |
| --- | --- | --- |
| `image` | `IMAGE` | 要裁剪的输入图像。此参数至关重要，因为它定义了将根据指定的尺寸和坐标提取区域的源图像。 |
| `width` | `INT` | 指定裁剪图像的宽度。此参数决定了结果裁剪图像的宽度。 |
| `height` | `INT` | 指定裁剪图像的高度。此参数决定了结果裁剪图像的高度。 |
| `x` | `INT` | 裁剪区域左上角的 x 坐标。此参数为裁剪的宽度维度设置了起始点。 |
| `y` | `INT` | 裁剪区域左上角的 y 坐标。此参数为裁剪的高度维度设置了起始点。 |

## 输出

| 参数名称 | 数据类型 | 作用 |
| --- | --- | --- |
| `image` | `IMAGE` | 裁剪操作的结果图像。此输出对于进一步处理或分析指定的图像区域非常重要。 |
