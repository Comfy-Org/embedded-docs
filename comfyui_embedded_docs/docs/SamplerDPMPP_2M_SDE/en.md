# SamplerDPMPP_2M_SDE

The SamplerDPMPP_2M_SDE node creates a DPM++ 2M SDE sampler for diffusion models. This sampler combines a second-order multistep solver with stochastic differential equation (SDE) noise to generate samples. It provides different solver types and noise handling options to control the sampling process.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `solver_type` | The type of differential equation solver to use during sampling: "midpoint" or "heun" (default: "midpoint") | COMBO | Yes | "midpoint"<br>"heun" |
| `eta` | Controls the amount of stochasticity (randomness) in the sampling process (default: 1.0) | FLOAT | Yes | 0.0 - 100.0 |
| `s_noise` | Controls the amount of noise added during sampling (default: 1.0) | FLOAT | Yes | 0.0 - 100.0 |
| `noise_device` | The device used for noise calculations. "gpu" performs noise generation on the GPU for potentially faster performance; "cpu" uses the CPU (default: "gpu") | COMBO | Yes | "gpu"<br>"cpu" |

Note: When `noise_device` is set to "cpu", the node creates the `dpmpp_2m_sde` sampler. When set to "gpu", it creates the `dpmpp_2m_sde_gpu` variant, which performs the noise-related calculations on the GPU.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `sampler` | A configured sampler object ready for use in the sampling pipeline | SAMPLER |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/en.md)

---
**Source fingerprint (SHA-256):** `42f5f098fa7573ca8a1a6085b72675ee6cb0ae8e7865c5793a815a6ef2495f82`
