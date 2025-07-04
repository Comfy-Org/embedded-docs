
`KSampler AdvancedK采样器（高级）`节点是`KSampler`节点的高级版本。`KSampler`在使用中总会向潜像中添加噪声，然后完全去除加噪后的潜像中的罩上，但`KSampler AdvancedK采样器（高级）`节点可以更细致地控制这个过程。可以通过**add_noise添加噪波**设置告诉`KSampler AdvancedK采样器（高级）`节点要不要向潜像中添加噪声。它还可以通过**return_with_leftover_noise返回噪波**设置返回部分去噪后的潜像。与`KSampler`节点不同，此节点没有**denoise降噪**设置，但这个过程是由**start_at_step开始降噪步数**和**end_at_step结束降噪步数**设置控制的。所以通过这个节点你可以将部分去除噪声的潜像输入到下一个`KSampler AdvancedK采样器（高级）`，从而在不同降噪过程中采用不同的方法。

## 输入

| 参数名称             | 数据类型 | 作用                                                         |
|---------------------|----------|--------------------------------------------------------------|
| `model`             | MODEL    | 指定用于生成样本的模型，对采样过程至关重要。               |
| `add_noise`         | COMBO[STRING] | 确定是否向采样过程添加噪声，影响生成样本的多样性和质量。   |
| `noise_seed`        | INT      | 设置噪声生成的种子，确保采样过程的可重复性。               |
| `steps`             | INT      | 定义采样过程中要执行的步骤数，影响输出的细节和质量。       |
| `cfg`               | FLOAT    | 控制条件因子，影响采样过程的方向和空间。                   |
| `sampler_name`      | COMBO[STRING] | 选择要使用的特定采样器，允许定制采样技术。               |
| `scheduler`         | COMBO[STRING] | 选择调度器以控制采样过程，影响样本的进展和质量。       |
| `positive`          | CONDITIONING | 指定正向条件以引导采样朝向期望的属性。                 |
| `negative`          | CONDITIONING | 指定负向条件以使采样远离某些属性。                       |
| `latent_image`      | LATENT   | 提供采样过程中使用的初始潜在图像，作为起点。               |
| `start_at_step`     | INT      | 确定采样过程的起始步骤，允许控制采样进展。               |
| `end_at_step`       | INT      | 设置采样过程的结束步骤，定义采样的范围。                   |
| `return_with_leftover_noise` | COMBO[STRING] | 指示是否返回带有剩余噪声的样本，影响最终输出的外观。 |

## 输出

| 参数名称 | 数据类型 | 作用                                                         |
|----------|----------|--------------------------------------------------------------|
| `latent` | LATENT   | 输出代表从模型生成的潜在图像，反映了应用的配置和技术。   |
