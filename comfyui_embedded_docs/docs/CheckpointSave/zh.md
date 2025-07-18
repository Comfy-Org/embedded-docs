`保存Checkpoint` 节点的作用是将完整的 Stable Diffusion 模型（包括 UNet、CLIP 和 VAE 组件）保存为 **.safetensors** 格式的检查点文件。

CheckpointSave 主要用于模型合并工作流中，当你通过 `ModelMergeSimple`、`ModelMergeBlocks` 等节点创建了新的合并模型后，可以使用此节点将结果保存为可重复使用的检查点文件。

## 输入

| 参数名称 | 数据类型 | 作用                                                         |
| ------- | -------- | ------------------------------------------------------------ |
| `模型` | MODEL    | 表示要保存状态的主要模型。捕获模型的当前状态以供将来恢复或分析至关重要。 |
| `clip`  | CLIP     | 与主要模型相关联的 CLIP 模型的参数，允许其状态与主模型一起保存。 |
| `vae`   | VAE      | 变分自编码器（VAE）模型的参数，使其状态可以与主模型和 CLIP 一起保存以供将来使用或分析。 |
| `文件名前缀`  | STRING   | 指定保存检查点的文件名前缀。 |

另外节点还存在两个隐藏输入用于元数据：

**prompt (PROMPT)**: 工作流提示信息
**extra_pnginfo (EXTRA_PNGINFO)**: 额外的 PNG 信息

## 输出

这个节点将会输出一个 checkpoint 文件, 对应的输出文件路径为 `output/checkpoints/` 目录

## 架构兼容性

- 目前完全支持: SDXL、SD3、SVD 等主流架构,查看[源码](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L176-L189)
- 基础支持：其它架构认可保存，但不会添加标准化的元数据信息

## 相关链接

相关源码: [nodes_model_merging.py#L227](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L227)
