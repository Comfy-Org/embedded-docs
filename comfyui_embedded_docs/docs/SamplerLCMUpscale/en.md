# SamplerLCMUpscale

The SamplerLCMUpscale node provides a specialized sampling method that combines Latent Consistency Model (LCM) sampling with image upscaling capabilities. It allows you to upscale images during the sampling process using various interpolation methods, making it useful for generating higher resolution outputs while maintaining image quality. The upscaling is applied gradually across the sampling steps until the target `scale_ratio` is reached.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `scale_ratio` | The scaling factor to apply during upscaling (default: 1.0) | FLOAT | No | 0.1 - 20.0 |
| `scale_steps` | The number of steps to use for the upscaling process. Use -1 for automatic calculation (default: -1) | INT | No | -1 - 1000 |
| `upscale_method` | The interpolation method used for upscaling the image (default: bislerp) | COMBO | Yes | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" |

Note: When `scale_steps` is set to a positive value, the effective number of upscaling steps is limited by the sampler's total number of sampling steps.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `sampler` | Returns a configured sampler object that can be used in the sampling pipeline | SAMPLER |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/en.md)

---
**Source fingerprint (SHA-256):** `5d6f6472fbb4d2c66a8a8b9d6dc34dcc52ac8272589fd6c29e4084d6cab3141b`
