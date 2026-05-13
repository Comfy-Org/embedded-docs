> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhanceV2/en.md)

# Topaz Video Enhance V2

The **Topaz Video Enhance V2** node allows you to upscale and enhance video using Topaz Labs' AI models. It can increase resolution, adjust frame rate through interpolation, and apply creative or realistic enhancements to breathe new life into your video footage.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Yes | - | The input video to be processed. Must be in MP4 container format. |
| `upscaler_model` | COMBO | Yes | `"Astra 2"`<br>`"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"`<br>`"Disabled"` | The AI model used for upscaling the video. Selecting "Disabled" means no upscaling will be applied. |
| `upscaler_model.upscaler_resolution` | COMBO | Conditional | `"FullHD (1080p)"`<br>`"4K (2160p)"` | The target output resolution for the upscaler. This parameter is required when an upscaler model is selected (not "Disabled"). |
| `upscaler_model.creativity` | FLOAT / COMBO | Conditional | Astra 2: 0.0 to 1.0 (step 0.1)<br>Starlight Creative: `"low"`<br>`"middle"`<br>`"high"` | Creative strength of the upscale. Available only for "Astra 2" and "Starlight (Astra) Creative" models. For Astra 2, it's a slider (default: 0.5). For Starlight Creative, it's a combo (default: "low"). |
| `upscaler_model.prompt` | STRING | No | - | Optional descriptive (not instructive) scene prompt. Only available for the "Astra 2" model. Capped at 500 input frames (~15s @ 30fps) when set. Default: empty. |
| `upscaler_model.sharp` | FLOAT | No | 0.0 to 1.0 (step 0.01) | Pre-enhance sharpness: 0.0=Gaussian blur, 0.5=passthrough (default), 1.0=USM sharpening. Only available for the "Astra 2" model. Default: 0.5. |
| `upscaler_model.realism` | FLOAT | No | 0.0 to 1.0 (step 0.01) | Pulls output toward photographic realism. Leave at 0 for the model default. Only available for the "Astra 2" model. Default: 0.0. |
| `interpolation_model` | COMBO | Yes | `"Disabled"`<br>`"apo-8"` | The AI model used for frame interpolation. Selecting "Disabled" means no interpolation will be applied. |
| `interpolation_model.interpolation_frame_rate` | INT | Conditional | 15 to 240 | Output frame rate. Required when interpolation model is "apo-8". Default: 60. |
| `interpolation_model.interpolation_slowmo` | INT | No | 1 to 16 | Slow-motion factor applied to the input video. For example, 2 makes the output twice as slow and doubles the duration. Default: 1. |
| `interpolation_model.interpolation_duplicate` | BOOLEAN | No | True/False | Analyze the input for duplicate frames and remove them. Default: False. |
| `interpolation_model.interpolation_duplicate_threshold` | FLOAT | No | 0.001 to 0.1 (step 0.001) | Detection sensitivity for duplicate frames. Default: 0.01. |
| `dynamic_compression_level` | COMBO | No | `"Low"`<br>`"Mid"`<br>`"High"` | CQP level for video compression. Default: "Low". |

**Important Constraints:**
- At least one of `upscaler_model` or `interpolation_model` must be enabled (not "Disabled"), otherwise an error is raised.
- The input video must be in MP4 container format.
- The "Astra 2" model with a prompt is limited to 500 input frames (~15 seconds at 30fps). Without a prompt, it is limited to a higher number of frames.
- When `upscaler_model` is not "Disabled", the `upscaler_resolution` sub-parameter is required.
- When `interpolation_model` is not "Disabled", the `interpolation_frame_rate` sub-parameter is required.

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `video` | VIDEO | The enhanced video output after applying the selected upscaling and/or interpolation filters. |

---
**Source fingerprint (SHA-256):** `29b7538206327c35866126c1862c1d1ccea872ba84fbb9c84126114a06e2b00f`
