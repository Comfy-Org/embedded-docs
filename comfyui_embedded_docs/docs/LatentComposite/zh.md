
此节点设计用于将两个潜在表示混合或合并为单个输出。这一过程对于通过控制方式结合输入潜在特征来创建组合图像或特征至关重要。

## 输入

| 参数名称 | 数据类型 | 作用 |
| --- | --- | --- |
| `samples_to` | `LATENT` | 'samples_to'的潜在表示，是'samples_from'组合的基础。 |
| `samples_from` | `LATENT` | 要组合到'samples_to'上的'samples_from'潜在表示。它为最终组合输出贡献其特征或特性。 |
| `x` | `INT` | 'samples_from'潜在将放置在'samples_to'上的x坐标（水平位置）。它决定了组合的水平对齐方式。 |
| `y` | `INT` | 'samples_from'潜在将放置在'samples_to'上的y坐标（垂直位置）。它决定了组合的垂直对齐方式。 |
| `feather` | `INT` | 一个布尔值，指示在组合之前是否应将'samples_from'潜在调整大小以匹配'samples_to'。这可能影响组合结果的规模和比例。 |

## 输出

| 参数名称 | 数据类型 | 作用 |
| --- | --- | --- |
| `latent` | `LATENT` | 输出是一个组合的潜在表示，根据指定的坐标和调整大小选项，混合了'samples_to'和'samples_from'潜在的特征。 |
