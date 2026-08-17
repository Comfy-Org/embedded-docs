# SamplerER_SDE

The SamplerER_SDE node provides specialized sampling methods for diffusion models, offering three solver types: ER-SDE, Reverse-time SDE, and ODE. It allows control over the stochastic behavior and the number of computational stages of the sampling process. The node automatically adjusts the noise settings when the ODE solver or a deterministic configuration (`eta`=0) is selected.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `solver_type` | The type of solver to use for sampling. Determines the noise scaling behavior of the diffusion process (default: "ER-SDE"). | COMBO | Yes | "ER-SDE"<br>"Reverse-time SDE"<br>"ODE" |
| `max_stage` | The maximum number of stages for the sampling process (default: 3). Controls the computational complexity and quality. Advanced parameter. | INT | Yes | 1-3 |
| `eta` | Stochastic strength of SDEs.<br>When eta=0, they reduce to deterministic ODE.<br>Large eta may cause invalid outputs. If this occurs, try decreasing this value. (default: 1.0). Advanced parameter. | FLOAT | Yes | 0.0-10.0 |
| `s_noise` | Noise scaling factor for the sampling process (default: 1.0). Controls the amount of noise applied during sampling. Advanced parameter. | FLOAT | Yes | 0.0-100.0 |

**Parameter Constraints:**

- When `solver_type` is "ODE" or `eta` is 0, the node forces `s_noise` to 0.0 and switches the solver to "ODE".
- `eta` affects both "ER-SDE" and "Reverse-time SDE" solver types. Large values may cause invalid outputs.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `sampler` | A configured sampler object that can be used in the sampling pipeline with the specified solver settings. | SAMPLER |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerER_SDE/en.md)

---
**Source fingerprint (SHA-256):** `5299ae9b45444cdc7c36bcb3c5e5a0600f9f904e57ae614554033434afdffd30`
