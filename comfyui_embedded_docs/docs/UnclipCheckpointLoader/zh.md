该节点会检测位于 `ComfyUI/models/checkpoints` 文件夹下的模型，
同时也会读取你在 extra_model_paths.yaml 文件中配置的额外路径的模型，
有时你可能需要 **刷新 ComfyUI 界面** 才能让它读取到对应文件夹下的模型文件

unCLIP检查点加载节点旨在加载专门为unCLIP模型定制的检查点。它便于检索和初始化模型、CLIP视觉模块和变分自编码器（VAE）从指定的检查点，简化了进一步操作或分析的设置过程。

## 输入

| 参数名称 | 数据类型 | 作用 |
| --- | --- | --- |
| `ckpt_name` | COMBO[STRING] | 'ckpt_name' 参数指定要加载的检查点的名称。它对于从预定义的检查点目录中识别和检索正确的检查点文件至关重要，从而决定了要初始化的模型和配置。 |

## 输出

| 参数名称 | 数据类型 | 作用 |
| --- | --- | --- |
| `model` | MODEL | 表示从检查点加载的主要模型。 |
| `clip` | CLIP | 表示从检查点加载的CLIP模块，如果可用。 |
| `vae` | VAE | 表示从检查点加载的VAE模块，如果可用。 |
| `clip_vision` | CLIP_VISION | 表示从检查点加载的CLIP视觉模块，如果可用。 |

---
