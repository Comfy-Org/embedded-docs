# ModelSamplingFlux

The ModelSamplingFlux node applies Flux model sampling to a given model by calculating a shift parameter based on image dimensions. It creates a specialized sampling configuration that adjusts the model's behavior according to the specified width, height, and shift parameters, then returns the modified model with the new sampling settings applied.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | The model to apply Flux sampling to | MODEL | Yes | - |
| `max_shift` | Maximum shift value for sampling calculation (default: 1.15) | FLOAT | Yes | 0.0 - 100.0 |
| `base_shift` | Base shift value for sampling calculation (default: 0.5) | FLOAT | Yes | 0.0 - 100.0 |
| `width` | Width of the target image in pixels (default: 1024) | INT | Yes | 16 - MAX_RESOLUTION |
| `height` | Height of the target image in pixels (default: 1024) | INT | Yes | 16 - MAX_RESOLUTION |

The effective shift value is interpolated between `base_shift` and `max_shift` based on the latent size derived from `width` and `height`. The `step` value is 0.01 for `max_shift` and `base_shift`, and 8 for `width` and `height`. The `max_shift` and `base_shift` parameters are marked as advanced options in the user interface.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `model` | The modified model with Flux sampling configuration applied | MODEL |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/en.md)

---
**Source fingerprint (SHA-256):** `04065b54ace30a2b20476ed085df871ea89794650e98ae30c40f750357663834`
