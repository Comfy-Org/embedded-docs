# ER_SDE采样器

SamplerER_SDE 节点为扩散模型提供专门的采样方法，支持三种求解器类型：ER-SDE、反向时间 SDE 和 ODE。它允许控制采样过程的随机行为和计算阶段数量。当选择 ODE 求解器或确定性配置（`eta`=0）时，节点会自动调整噪声设置。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `solver_type` | 用于采样的求解器类型。决定扩散过程的噪声缩放行为（默认值："ER-SDE"）。 | COMBO | 是 | "ER-SDE"<br>"Reverse-time SDE"<br>"ODE" |
| `max_stage` | 采样过程的最大阶段数（默认值：3）。控制计算复杂度和质量。高级参数。 | INT | 是 | 1-3 |
| `eta` | SDE 的随机强度。<br>当 `eta`=0 时，它们退化为确定性 ODE。<br>较大的 `eta` 可能导致无效输出。如果发生这种情况，请尝试减小此值。（默认值：1.0）。高级参数。 | FLOAT | 是 | 0.0-10.0 |
| `s_noise` | 采样过程的噪声缩放因子（默认值：1.0）。控制采样过程中应用的噪声量。高级参数。 | FLOAT | 是 | 0.0-100.0 |

**参数约束：**

- 当 `solver_type` 为 "ODE" 或 `eta` 为 0 时，节点将 `s_noise` 强制设为 0.0，并将求解器切换为 "ODE"。
- `eta` 同时影响 "ER-SDE" 和 "Reverse-time SDE" 求解器类型。较大的值可能导致无效输出。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `sampler` | 一个配置好的采样器对象，可在采样流程中与指定的求解器设置一起使用。 | SAMPLER |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerER_SDE/zh.md)

---
**Source fingerprint (SHA-256):** `5299ae9b45444cdc7c36bcb3c5e5a0600f9f904e57ae614554033434afdffd30`
