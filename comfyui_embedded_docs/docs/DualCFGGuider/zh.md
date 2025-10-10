> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/zh.md)

DualCFGGuider 节点为双分类器自由引导采样创建了一个引导系统。它将两个正向条件输入与一个负向条件输入相结合，对每个条件对应用不同的引导尺度，以控制每个提示词对生成输出的影响程度。

## 输入参数

| 参数名 | 数据类型 | 必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 用于引导的模型 |
| `cond1` | CONDITIONING | 是 | - | 第一个正向条件输入 |
| `cond2` | CONDITIONING | 是 | - | 第二个正向条件输入 |
| `negative` | CONDITIONING | 是 | - | 负向条件输入 |
| `cfg_conds` | FLOAT | 是 | 0.0 - 100.0 | 第一个正向条件的引导尺度（默认值：8.0） |
| `cfg_cond2_negative` | FLOAT | 是 | 0.0 - 100.0 | 第二个正向和负向条件的引导尺度（默认值：8.0） |
| `style` | COMBO | 是 | "regular"<br>"nested" | 要应用的引导样式（默认值："regular"） |

## 输出结果

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `GUIDER` | GUIDER | 已配置的引导系统，准备用于采样 |