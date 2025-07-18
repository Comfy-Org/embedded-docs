该节点主要用于单独加载 CLIP 文本编码器模型。
支持检测以下路径的模型文件检测：

- “ComfyUI/models/text_encoders/”
- “ComfyUI/models/clip/”

> 如果你是在 ComfyUI 启动后才保存的模型则需要刷新 ComfyUI 前端来获取最新的模型文件路径列表

支持的模型格式有:

- `.ckpt`
- `.pt`
- `.pt2`
- `.bin`
- `.pth`
- `.safetensors`
- `.pkl`
- `.sft`

更多最新模型文件加载详情请查阅[folder_paths](https://github.com/comfyanonymous/ComfyUI/blob/master/folder_paths.py)

## 输入

| 参数名称     | 数据类型 | 作用                                                         |
| ------------ | -------- | ------------------------------------------------------------ |
| `CLIP名称`  | COMBO[STRING] | 指定要加载的 CLIP 模型的名称。此名称用于在预定义的目录结构内定位模型文件。 |
| `类型`       | COMBO[STRING] | 确定要加载的 CLIP 模型类型，随着 ComfyUI 支持的模型数量增加这里的类型也会新增对应的类型，请查看[node.py](https://github.com/comfyanonymous/ComfyUI/blob/master/nodes.py)中源码里关于`CLIPLoader` 类的相关定义|
| `设备`       | COMBO[STRING] |选择加载 CLIP 模型的设备，`default` 将会将对应的模型在 GPU 上运行，如果选择`CPU` 将强制在 CPU上进行加载|

### 不同`设备`选项的说明

**选择 "default" 的情况**：

- 有足够的 GPU 内存
- 希望获得最佳性能
- 让系统自动优化内存使用

**选择 "cpu" 的情况**：

- GPU 内存不足
- 需要为其他模型（如 UNet）保留 GPU 内存
- 在低 VRAM 环境下运行
- 调试或特殊用途需要

**性能影响**

CPU 运行会比 GPU 运行慢很多，但可以节省宝贵的 GPU 内存供其他更重要的模型组件使用。在内存受限的环境中，将 CLIP 模型放在 CPU 上是一个常见的优化策略。

### 支持的搭配

| 模型类型 | 对应编码器 |
|----------|------------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl/ clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cosmos | old t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |

未来随着 ComfyUI 的更新，这个更新搭配可能会新增，详情请参考 [node.py](https://github.com/comfyanonymous/ComfyUI/blob/master/nodes.py)中源码里关于`CLIPLoader` 类的相关定义说明

## 输出

| 参数名称 | 数据类型 | 作用                                       |
| -------- | -------- | ------------------------------------------ |
| `clip`   | CLIP     | 加载的 CLIP 模型，准备用于下游任务或进一步处理。 |

## 其它扩展

CLIP 模型在 ComfyUI 中扮演着文本编码器的核心角色，负责将文本提示转换为可供扩散模型理解的数值表示，你可以把它理解成翻译官，负责讲你的文本翻译成大模型可以理解语言，当然不同模型也存在着 “方言” ，所以在不同架构的模型之间需要不同的 CLIP 编码器来完成文本编码的这一过程。
