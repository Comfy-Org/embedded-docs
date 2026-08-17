# Save Audio (Opus) (DEPRECATED)

The SaveAudioOpus node saves audio data to an Opus format file. It takes an audio input and exports it as a compressed Opus file with configurable quality settings. This node is deprecated and may be removed in future versions.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `audio` | The audio data to be saved as an Opus file. The node raises an error if no audio is provided (for example, when the source video has no audio track). | AUDIO | Yes | - |
| `filename_prefix` | The prefix for the output filename (default: "audio/ComfyUI") | STRING | No | - |
| `quality` | The audio quality (bitrate) setting for the Opus file (default: "128k") | COMBO | No | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `audio` | The input audio data, returned after the Opus file is saved to disk. | AUDIO |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/en.md)

---
**Source fingerprint (SHA-256):** `a2f585f45299759738fa85f6b73f51680d4e86da57d3fc9c2236e66114fa3d6c`
