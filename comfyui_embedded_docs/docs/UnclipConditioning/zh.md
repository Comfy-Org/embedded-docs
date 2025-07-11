此节点设计用于将CLIP视觉输出整合到条件过程中，根据指定的强度和噪声增强参数调整这些输出的影响。它通过视觉上下文丰富了条件，增强了生成过程。

## 输入

| 参数名称 | 数据类型 | 作用 |
| --- | --- | --- |
| `CONDITIONING` | CONDITIONING | 基础条件数据，将向其添加CLIP视觉输出，作为进一步修改的基础。 |
| `clip_vision_output` | `CLIP_VISION_OUTPUT` | 来自CLIP视觉模型的输出，提供被整合进条件的视觉上下文。 |
| `strength` | `FLOAT` | 确定CLIP视觉输出对条件影响的强度。 |
| `noise_augmentation` | `FLOAT` | 指定在将CLIP视觉输出整合进条件之前应用的噪声增强水平。 |

## 输出

| 参数名称 | 数据类型 | 作用 |
| --- | --- | --- |
| `CONDITIONING` | CONDITIONING | 丰富的条件数据，现在包含已应用强度和噪声增强的整合CLIP视觉输出。 |

---
