# HiDream-O1 补丁缝隙平滑

## 概述
此节点通过在采样过程后期对多个偏移 patch 网格位置上的模型输出进行平均，减少 HiDream-O1 模型生成图像中可见的接缝。其工作原理是多次运行模型，每次使用略有不同的图像对齐方式，然后将结果混合在一起，从而抵消 patch 边界处可能出现的网格状伪影。

## 输入
| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要应用接缝平滑包装器的 HiDream-O1 模型。 | MODEL | 是 | - |
| `start_percent` | 混合开启时的采样进度（0=开始，1=结束）（默认：0.8）。 | FLOAT | 是 | 0.0 to 1.0 (step: 0.01) |
| `end_percent` | 混合关闭时的采样进度（默认：1.0）。 | FLOAT | 是 | 0.0 to 1.0 (step: 0.01) |
| `pattern` | 偏移布局。`single_shift`：在自然 patch 网格上运行一次，其余为偏移运行。`symmetric`：所有运行都在网格外，偏移围绕原点分布（默认：`"single_shift"`）。 | COMBO | 是 | `"single_shift"`<br>`"symmetric"` |
| `passes` | 每个门控步骤的传递次数。`2`/`4` = 固定次数。`ramp_*`：传递次数随采样接近结束而增加（在接缝最明显处进行更多平滑）（默认：`"2"`）。 | COMBO | 是 | `"2"`<br>`"4"`<br>`"ramp_2_4"`<br>`"ramp_2_4_8"` |
| `blend` | `average`：等权平均。`window`：Hann 窗加权，更倾向于远离每个 patch 边界的传递。`median`：逐像素中位数，可排除环绕越界异常传递（默认：`"average"`）。 | COMBO | 是 | `"average"`<br>`"window"`<br>`"median"` |
| `strength` | 自然网格预测（0）与平均结果（1）之间的插值系数（默认：1.0）。 | FLOAT | 是 | 0.0 to 1.0 (step: 0.01) |

**约束说明：**

- 如果 `strength` 小于或等于 0.0，或 `end_percent` 小于或等于 `start_percent`，则不应用平滑效果；在这些情况下，节点返回未修改的模型。
- `passes` 的 ramp 选项（`ramp_2_4`、`ramp_2_4_8`）会在采样过程于门控范围内向 `end_percent` 推进时增加传递次数，因此只有在 `start_percent` 和 `end_percent` 构成非空范围时才有意义。
- 平均结果仅在远离图像边界处混合回模型输出：一个遮罩会在每条边缘的 32 像素条带内保留原始预测（带有 4 像素羽化），从而避免偏移传递导致的环绕污染。

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 已应用 patch 接缝平滑包装器的修改后模型。 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1PatchSeamSmoothing/zh.md)

---
**Source fingerprint (SHA-256):** `02a2256fbf1868cc033a00f15066e9a896a7685ecdca0564ceec5b5b618b6a3c`
