SplitImageWithAlpha 节点旨在分离图像的颜色和 alpha（透明度）组件。它处理输入的图像张量，提取 RGB 通道作为颜色组件，以及 alpha 通道作为透明度组件，从而便于对这些不同的图像方面进行操作。

## 输入

| 参数名称 | 数据类型 | 作用                                                         |
|----------|----------|--------------------------------------------------------------|
| `image`  | `IMAGE`  | 'image' 参数代表要从中分离出 RGB 和 alpha 通道的输入图像张量。它对操作至关重要，因为它提供了拆分的源数据。 |

## 输出

| 参数名称 | 数据类型 | 作用                                                         |
|----------|----------|--------------------------------------------------------------|
| `image`  | `IMAGE`  | 'image' 输出代表输入图像分离出的 RGB 通道，提供了不包含透明度信息的颜色组件。 |
| `mask`   | `MASK`   | 'mask' 输出代表输入图像分离出的 alpha 通道，提供了透明度信息。   |
