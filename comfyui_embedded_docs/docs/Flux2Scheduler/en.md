# Flux2Scheduler

The Flux2Scheduler node generates a sequence of noise levels (sigmas) for the denoising process, specifically tailored for the Flux2 model. It calculates a schedule based on the number of denoising steps and the dimensions of the target image, which influences the progression of noise removal during image generation.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `steps` | The number of denoising steps to perform. A higher value typically leads to more detailed results but takes longer to process (default: 20). | INT | Yes | 1 to 4096 |
| `width` | The width of the image to be generated, in pixels. This value influences the noise schedule calculation (default: 1024). | INT | Yes | 16 to 16384 (MAX_RESOLUTION) |
| `height` | The height of the image to be generated, in pixels. This value influences the noise schedule calculation (default: 1024). | INT | Yes | 16 to 16384 (MAX_RESOLUTION) |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `sigmas` | A sequence of noise level values (sigmas) that define the denoising schedule for the sampler. The output contains one more value than the number of steps (`steps + 1`). | SIGMAS |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2Scheduler/en.md)

---
**Source fingerprint (SHA-256):** `9606177f37f7bc03aef524623f03b7f24bcdc3d9327dcdf74863fe2befeb2b65`
