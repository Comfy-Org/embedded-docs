> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioAdjustVolume/en.md)

The AudioAdjustVolume node modifies the loudness of audio by applying volume adjustments in decibels (dB). It takes an audio input and applies a gain factor based on the specified volume level, where positive values increase volume and negative values decrease it. The node returns the modified audio with the same sample rate as the original.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Yes | - | The audio input to be processed |
| `volume` | INT | Yes | -100 to 100 | Volume adjustment in decibels (dB). 0 = no change, +6 = double, -6 = half, etc (default: 1) |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `audio` | AUDIO | The processed audio with adjusted volume level |

---
**Source fingerprint (SHA-256):** `0436765680671551239f7a89b575cdfb22590fbe662bdfe5da01bd1cd5c496ed`
