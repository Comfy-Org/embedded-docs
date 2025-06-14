
此节点旨在为 DPMPP_2M_SDE 模型生成采样器，允许根据指定的求解器类型、噪声水平和计算设备偏好创建样本。它抽象了采样器配置的复杂性，提供了一个简化的接口，用于生成具有定制设置的样本。

## 输入

| 参数名称       | 数据类型 | 作用                                                         |
|----------------|----------|--------------------------------------------------------------|
| `solver_type`  | COMBO[STRING] | 在采样过程中使用的求解器类型，提供 'midpoint' 和 'heun' 两种选择。此选择影响采样期间应用的数值积分方法。 |
| `eta`          | `FLOAT`  | 确定数值积分中的步长，影响采样过程的粒度。较高的值表示较大的步长。                     |
| `s_noise`      | `FLOAT`  | 控制采样过程中引入的噪声水平，影响生成样本的可变性。                           |
| `noise_device` | COMBO[STRING] | 指示噪声生成过程执行的计算设备（'gpu' 或 'cpu'），影响性能和效率。             |

## 输出

| 参数名称   | 数据类型 | 作用                                       |
|------------|----------|--------------------------------------------|
| `sampler`  | `SAMPLER` | 根据指定参数配置的采样器，准备就绪，可用于生成样本。 |
