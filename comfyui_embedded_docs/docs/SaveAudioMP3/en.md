# Save Audio (MP3) (DEPRECATED)

The SaveAudioMP3 node saves audio data as an MP3 file. It takes an audio input and writes it to the output directory with a customizable filename prefix and quality setting. This node is deprecated and may be removed in future versions.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `audio` | The audio data to be saved as an MP3 file | AUDIO | Yes | - |
| `filename_prefix` | The prefix for the output filename (default: "audio/ComfyUI") | STRING | No | - |
| `quality` | The MP3 encoding quality setting (default: "V0"). V0 uses variable bitrate for high quality; 128k and 320k use fixed bitrates of 128 and 320 kbps | COMBO | No | `"V0"`<br>`"128k"`<br>`"320k"` |
| `prompt` | Internal prompt data, automatically provided by the system | PROMPT | No | - |
| `extra_pnginfo` | Additional PNG information, automatically provided by the system | EXTRA_PNGINFO | No | - |

**Note:** If the `audio` input is None (for example, when the source video has no audio track), the node raises a ValueError.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `audio` | The audio data that was saved as an MP3 file | AUDIO |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/en.md)

---
**Source fingerprint (SHA-256):** `7d3b439dfd7cb211dd6568f6b5124bb225909dcf0ae150addc4ca226d947a4f0`
