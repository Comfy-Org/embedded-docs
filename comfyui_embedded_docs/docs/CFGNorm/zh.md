# CFG归一化

CFGNorm 对扩散模型中的分类器自由引导（CFG）过程应用归一化技术。它通过比较条件输出和无条件输出的范数来调整去噪预测的缩放比例，然后应用强度乘数来控制效果。这有助于通过防止引导缩放中出现极端值来稳定生成过程。当启用 `pre_cfg` 时，重缩放改为在采样器的 CFG 组合之前应用于组合噪声。

## 输入
| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要应用 CFG 归一化的扩散模型 | MODEL | 是 | - |
| `strength` | 控制应用于 CFG 缩放的归一化效果强度（默认值：1.0） | FLOAT | 是 | 0.0 至 100.0（步长 0.01） |
| `pre_cfg` | 若为 true，则在采样器进行 CFG 组合之前对组合噪声进行重缩放，不进行钳制（可能放大）。与 Lens 等模型使用的范数缩放 CFG 相匹配。默认 false 保留原始的 post-CFG x0 空间仅衰减行为。（默认值：False） | BOOLEAN | 否 | True<br>False |

注意：在默认的 post-CFG 模式下，重缩放因子被钳制在 0.0 和 1.0 之间，因此只能衰减（减小）预测的尺度。当启用 `pre_cfg` 时，不进行钳制，因此组合噪声可以被放大。在该模式下，`strength` 值若不为 1.0，则会将结果向标准线性 CFG 方向混合回退。

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `patched_model` | 返回修改后的模型，其采样过程已应用 CFG 归一化 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/zh.md)

---
**Source fingerprint (SHA-256):** `427dda498ebda2642489aa2591f063355a77b1e064e0dc7fa8570ed8200c2734`
