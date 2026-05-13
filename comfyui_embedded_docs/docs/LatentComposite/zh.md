> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentComposite/zh.md)

LatentComposite 节点旨在将两个潜在表示混合或合并为单个输出。此过程通过以受控方式结合输入潜在特征，对于创建复合图像或特征至关重要。

## 输入

| 参数 | 数据类型 | 描述 |
|--------------|-------------|-------------|
| `samples_to` | `LATENT` | `samples_to` 潜在表示，`samples_from` 将被合成到其上。它作为合成操作的基础。 |
| `samples_from` | `LATENT` | `samples_from` 潜在表示，将被合成到 `samples_to` 上。它将其特征或特性贡献给最终的复合输出。 |
| `x` | `INT` | `samples_from` 潜在将被放置在 `samples_to` 上的 x 坐标（水平位置）。它决定了合成的水平对齐方式。 |
| `y` | `INT` | `samples_from` 潜在将被放置在 `samples_to` 上的 y 坐标（垂直位置）。它决定了合成的垂直对齐方式。 |
| `feather` | `INT` | 一个布尔值，指示在合成前是否应将 `samples_from` 潜在调整为匹配 `samples_to` 的大小。这会影响合成结果的缩放比例和尺寸。 |

## 输出

| 参数 | 数据类型 | 描述 |
|-----------|-------------|-------------|
| `latent` | `LATENT` | 输出是一个复合潜在表示，根据指定的坐标和调整大小选项，融合了 `samples_to` 和 `samples_from` 潜在的特征。 |