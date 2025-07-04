此节点对图像应用高斯模糊，允许软化边缘并减少细节和噪声。它通过参数提供对模糊强度和扩散的控制。

## 输入

| 参数名称 | 数据类型 | 作用 |
| --- | --- | --- |
| `image` | `IMAGE` | 要模糊的输入图像。这是模糊效果的主要目标。 |
| `blur_radius` | `INT` | 确定模糊效果的半径。更大的半径会导致更明显的模糊。 |
| `sigma` | `FLOAT` | 控制模糊的扩散。更高的sigma值意味着模糊将影响每个像素周围的更广泛区域。 |

## 输出

| 参数名称 | 数据类型 | 作用 |
| --- | --- | --- |
| `image` | `IMAGE` | 输出是输入图像的模糊版本，模糊程度由输入参数决定。 |
