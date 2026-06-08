CLIPAdd 节点通过合并两个 CLIP 模型的关键补丁来组合它们。它会创建第一个 CLIP 模型的副本，然后添加第二个模型的大部分关键补丁（不包括位置 ID 和 logit 尺度参数）。这使您能够在保留第一个模型结构的同时，融合不同 CLIP 模型的特征。

## 输入

| 参数 | 描述 | 数据类型 | 输入类型 | 默认值 | 范围 |
| --- | --- | --- | --- | --- | --- |
| `clip1` | 作为合并基础的原始 CLIP 模型 | CLIP | 必需 | - | - |
| `clip2` | 提供额外补丁的次要 CLIP 模型 | CLIP | 必需 | - | - |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `CLIP` | 返回一个合并后的 CLIP 模型，融合了两个输入模型的特征 | CLIP |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAdd/zh.md)

---
**Source fingerprint (SHA-256):** `935d450d25d90dc623e3f2b39b251359a9066c9e1fdd2a70384982fb26a21864`
