# VOIDSampler

## Overview

The VOIDSampler node provides a specialized DDIM sampling method designed specifically for VOID inpainting models. It implements the same denoising process used during VOID model training, without the noise scaling that standard KSamplers apply. This node is intended for use with SamplerCustom or SamplerCustomAdvanced nodes, and should be paired with RandomNoise or VOIDWarpedNoiseSource.

## Inputs

This node has no configurable input parameters. It is a self-contained sampler that applies a fixed DDIM sampling algorithm.

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| *No inputs* | This node does not accept any input parameters. | - | - | - |

Note: VOID models were trained with the diffusers CogVideoXDDIMScheduler, which operates in alpha-space where the input standard deviation is approximately 1. The standard KSampler applies noise scaling that multiplies by about 4500x, which is incompatible with this training. The VOIDSampler skips that scaling and implements the DDIM update rule directly using sigma-to-alpha conversion.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `SAMPLER` | A sampler object implementing the VOID DDIM algorithm, ready to be connected to SamplerCustom or SamplerCustomAdvanced nodes. | SAMPLER |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/en.md)

---
**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`
