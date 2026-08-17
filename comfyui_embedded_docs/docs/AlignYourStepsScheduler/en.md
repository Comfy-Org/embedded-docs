# AlignYourStepsScheduler

The AlignYourStepsScheduler node creates the sigma values used during the denoising process for different diffusion model types. It picks the base noise levels for the selected model, adjusts the number of steps based on the `denoise` setting, and returns a tensor of sigma values that ends at 0.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model_type` | The model type used to select the base noise levels (default: "SD1") | COMBO | Yes | `"SD1"`<br>`"SDXL"`<br>`"SVD"` |
| `steps` | The total number of sampling steps to generate (default: 10) | INT | Yes | 1 to 10000 |
| `denoise` | Controls how much of the sampling process is used: 1.0 uses all steps, lower values use fewer steps, and 0.0 returns an empty sigma tensor (default: 1.0) | FLOAT | Yes | 0.0 to 1.0 |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `sigmas` | The calculated sigma values for the denoising process. If `denoise` is 0.0, an empty tensor is returned. | SIGMAS |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/en.md)

---
**Source fingerprint (SHA-256):** `3adbe1016c1ff4b9b7ad3737f50b168f54444d4ca355488e60537d1136f85d3f`
