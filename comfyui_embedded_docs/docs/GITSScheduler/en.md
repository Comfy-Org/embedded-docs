# GITSScheduler

The GITSScheduler node generates the sigma (noise level) schedule used by the GITS sampling method. It selects a pre-defined noise level table based on the `coeff` parameter and the number of `steps`, optionally trimming the schedule when a `denoise` value below 1.0 is used.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `coeff` | The coefficient that selects which pre-defined noise level table is used to build the schedule. The value is rounded to 2 decimal places (default: 1.20) | FLOAT | Yes | 0.80 - 1.50 |
| `steps` | The total number of sampling steps to generate sigmas for (default: 10) | INT | Yes | 2 - 1000 |
| `denoise` | Denoising factor that reduces the number of steps used (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |

**Note:** When `denoise` is set to 0.0, the node returns an empty tensor. When `denoise` is less than 1.0, the actual number of steps used is calculated as `round(steps * denoise)`. For steps up to 20, the node uses pre-defined noise levels directly; for steps greater than 20, it uses log-linear interpolation to extend the pre-defined noise levels to the desired number of steps.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `sigmas` | The generated sigma values for the noise schedule | SIGMAS |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/en.md)

---
**Source fingerprint (SHA-256):** `f46681970fece985f6a4b62d0817d1ea306f1ca9a20189f937512dd5717f458b`
