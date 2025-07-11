
该节点旨在通过集成连续 EDM（基于能量的扩散模型）采样技术来增强模型的采样能力。它允许动态调整模型采样过程中的噪声水平，提供对生成质量和多样性的更精细控制。

## 输入

### 必填

| 参数名称 | 数据类型 | 作用                                                         |
| -------- | -------- | ------------------------------------------------------------ |
| `model`  | MODEL    | 需要增强连续 EDM 采样能力的模型。它作为应用高级采样技术的基石。 |
| `sampling` | COMBO[STRING] | 指定要应用的采样类型，可以是 'eps' 表示欧拉采样，或 'v_prediction' 表示速度预测，这将影响采样过程中模型的行为。 |
| `sigma_max` | `FLOAT` | 噪声水平的最大 sigma 值，允许在采样过程中控制噪声注入的上限。 |
| `sigma_min` | `FLOAT` | 噪声水平的最小 sigma 值，设置噪声注入的下限，从而影响模型的采样精度。 |

## 输出

| 参数名称 | 数据类型 | 作用                                       |
| -------- | -------- | ------------------------------------------ |
| `model`  | MODEL    | 增强后的模型，集成了连续 EDM 采样能力，准备用于生成任务。 |
