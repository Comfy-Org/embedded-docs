# SamplerDPMPP_SDE

The SamplerDPMPP_SDE node creates a DPM++ SDE (Stochastic Differential Equation) sampler for use in the sampling process. This sampler provides a stochastic sampling method with configurable noise parameters and device selection. It returns a sampler object that can be used in the sampling pipeline.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `eta` | Controls the stochasticity of the sampling process (default: 1.0) | FLOAT | Yes | 0.0 - 100.0 |
| `s_noise` | Controls the amount of noise added during sampling (default: 1.0) | FLOAT | Yes | 0.0 - 100.0 |
| `r` | A parameter that influences the sampling behavior (default: 0.5) | FLOAT | Yes | 0.0 - 100.0 |
| `noise_device` | Selects the device where noise calculations are performed (default: "gpu"). When set to "cpu", the standard `dpmpp_sde` sampler is used; when set to "gpu", the `dpmpp_sde_gpu` sampler is used. | COMBO | Yes | "gpu"<br>"cpu" |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `sampler` | Returns a configured DPM++ SDE sampler object for use in sampling pipelines | SAMPLER |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/en.md)

---
**Source fingerprint (SHA-256):** `56949712f245abfcc48c09d7d14a1a7778e80ba58535e538484c382d7e0d02c6`
