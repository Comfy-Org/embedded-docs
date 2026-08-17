# 双CFG引导器

DualCFGGuider 节点创建了一个用于双分类器自由引导采样的引导系统。它将两个正向条件输入与一个负向条件输入相结合，对每一对条件输入应用不同的引导缩放系数，以控制每个提示词对生成输出的影响强度。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 用于引导的模型。 | MODEL | 是 | - |
| `cond1` | 第一个正向条件输入。 | CONDITIONING | 是 | - |
| `cond2` | 第二个正向条件输入，视为中间条件。 | CONDITIONING | 是 | - |
| `negative` | 负向条件输入。 | CONDITIONING | 是 | - |
| `cfg_conds` | 应用于 `cond1` 和 `cond2` 之间的引导缩放系数（默认值：8.0）。 | FLOAT | 是 | 0.0 - 100.0 |
| `cfg_cond2_negative` | 应用于 `cond2` 与负向条件之间的引导缩放系数（默认值：8.0）。 | FLOAT | 是 | 0.0 - 100.0 |
| `style` | 要应用的引导样式（默认值："regular"）。"regular" 在一步中组合两个引导缩放系数；"nested" 先应用 `cfg_conds`，然后使用相对于负向条件的 `cfg_cond2_negative` 对结果进行缩放。 | COMBO | 是 | "regular"<br>"nested" |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `GUIDER` | 一个已配置的引导系统，可用于采样。 | GUIDER |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/zh.md)

---
**Source fingerprint (SHA-256):** `ef28d109149cb545bcd76215fd99535905c1d395222149a029c1c210e2912e97`
