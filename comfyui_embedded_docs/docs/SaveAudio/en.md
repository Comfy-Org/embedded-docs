# Save Audio (FLAC) (DEPRECATED)

The SaveAudio node saves audio data to a file in FLAC format. It takes an audio input, writes it to the output directory using the specified filename prefix, and passes the same audio through as its output. This node is deprecated and should be replaced with the current Save Audio node.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `audio` | The audio data to be saved | AUDIO | Yes | - |
| `filename_prefix` | The prefix for the output filename (default: "audio/ComfyUI") | STRING | No | - |

The node raises an error if `audio` is None, which can happen when the source video has no audio track.

The `prompt` and `extra_pnginfo` parameters are hidden and automatically handled by the system.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `audio` | The same audio data that was saved to the file | AUDIO |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/en.md)

---
**Source fingerprint (SHA-256):** `6ac62d315f14213091cd179a05f0bbd51f1b1a5056bb5c06ca137d2b574d6017`
