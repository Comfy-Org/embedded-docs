# BetaSamplingScheduler

The BetaSamplingScheduler node creates a sequence of noise levels (sigmas) that control how noise is removed during the sampling process in image generation. It uses a beta scheduling algorithm, and the `alpha` and `beta` settings adjust the shape of the noise schedule. The generated sigmas are passed to a sampler to guide the denoising process.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | The model used for sampling, which provides the model sampling object. | MODEL | Yes | - |
| `steps` | The number of sampling steps to generate sigmas for (default: 20). | INT | Yes | 1 to 10000 |
| `alpha` | Alpha parameter for the beta scheduler, controlling the scheduling curve (default: 0.6). Advanced parameter. | FLOAT | Yes | 0.0 to 50.0 |
| `beta` | Beta parameter for the beta scheduler, controlling the scheduling curve (default: 0.6). Advanced parameter. | FLOAT | Yes | 0.0 to 50.0 |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `SIGMAS` | A sequence of noise levels (sigmas) used for the sampling process. | SIGMAS |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BetaSamplingScheduler/en.md)

---
**Source fingerprint (SHA-256):** `80adae3cbedff7fe544a1fbcf638af7965f1216e422931063ecf67da53ddff95`
