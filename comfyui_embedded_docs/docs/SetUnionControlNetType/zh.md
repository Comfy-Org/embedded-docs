# 设置UnionControlNet类型

SetUnionControlNetType 节点允许您设置用于条件控制的控制网络的控制类型。它接收一个现有的控制网络，创建其修改副本，并将选定的控制类型存储在该副本中，从而保持原始网络不变。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `control_net` | 要复制并使用选定控制类型进行修改的控制网络 | CONTROL_NET | 是 | - |
| `type` | 要应用于复制后的控制网络的控制类型。选择 "auto" 表示不设置控制类型，或从可用的联合控制网络类型中选择一个特定类型（默认值："auto"） | COMBO | 是 | `"auto"`<br>`"openpose"`<br>`"depth"`<br>`"hed/pidi/scribble/ted"`<br>`"canny/softedge"`<br>`"normal/bms"`<br>`"seg"`<br>`"inpaint"`<br>`"lineart"`<br>`"s4"`<br>`"tile/color"`<br>`"blur"`<br>`"identity"` |

注意：当 `type` 为 "auto" 时，复制后的控制网络上的控制类型列表将被清除。当选择了特定类型时，复制后的控制网络将存储相应的类型编号。

## 输出

| 输出名 | 描述 | 数据类型 |
| --- | --- | --- |
| `control_net` | 应用了选定控制类型的控制网络的修改副本 | CONTROL_NET |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/zh.md)

---
**Source fingerprint (SHA-256):** `db4b1a3cebafcff2be3172faa09cecbd5e19331376491c491cbe359013ed3da3`
