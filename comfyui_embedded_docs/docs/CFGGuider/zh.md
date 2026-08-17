# CFG引导器

CFGGuider 节点创建了一个用于控制图像生成过程中采样过程的引导系统。它接收一个模型以及正向和负向条件输入，然后应用无分类器引导缩放（classifier-free guidance scale），将生成过程导向期望的内容，同时避免不需要的元素。此节点输出一个引导器（guider）对象，供采样节点用于控制图像生成方向。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 用于引导的模型 | MODEL | 是 | - |
| `positive` | 引导生成过程朝向期望内容的正向条件 | CONDITIONING | 是 | - |
| `negative` | 引导生成过程远离不需要内容的负向条件 | CONDITIONING | 是 | - |
| `cfg` | 无分类器引导缩放，用于控制条件对生成过程的影响强度（默认值：8.0） | FLOAT | 是 | 0.0 至 100.0 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `GUIDER` | 可传递给采样节点以控制生成过程的引导器对象 | GUIDER |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGGuider/zh.md)

---
**Source fingerprint (SHA-256):** `73b57bfbb6d4fc083a8089bc0f786f82d03e0d7b2faeeb7a42b3d87e38047b9e`
