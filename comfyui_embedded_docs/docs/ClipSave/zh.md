`CLIP保存` 节点用于将 CLIP 文本编码器模型保存为 SafeTensors 格式文件, 该节点属于高级模型合并工作流的一部分，通常与 `CLIPMergeSimple`、`CLIPMergeAdd` 等节点配合使用。保存的文件采用 SafeTensors 格式，确保安全性和兼容性。

## 输入

| 参数名 | 类型 | 是否必需 | 默认值 | 描述 |
|--------|------|----------|--------|------|
| `clip` | CLIP | 必需 | - | 要保存的 CLIP 模型 |
| `文件名前缀` | STRING | 必需 | `"clip/ComfyUI"` | 保存文件的前缀路径 |
| `prompt` | PROMPT | 隐藏参数 | - | 工作流提示信息（用于元数据） |
| `extra_pnginfo` | EXTRA_PNGINFO | 隐藏参数 | - | 额外的PNG信息（用于元数据） |

## 输出

该节点没有定义输出类型, 会将处理后的文件保存到 `ComfyUI/output/` 文件夹下

### 多文件保存策略

节点会根据 CLIP 模型类型分别保存不同组件：

| 前缀类型 | 文件名后缀 | 说明 |
|----------|------------|------|
| `clip_l.` | `_clip_l` | CLIP-L 文本编码器 |
| `clip_g.` | `_clip_g` | CLIP-G 文本编码器 |
| 空前缀 | 无后缀 | 其他 CLIP 组件 |
