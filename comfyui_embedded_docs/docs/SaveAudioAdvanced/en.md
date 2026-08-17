# Save Audio (Advanced)

Save Audio (Advanced)

Saves the input audio to your ComfyUI output directory. You can export audio in FLAC, MP3, or Opus format, with selectable quality settings for MP3 and Opus files.

## Inputs

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `format` | The file format in which to save the audio. | DYNAMIC_COMBO | Yes | "flac"<br>"mp3"<br>"opus" |
| `audio` | The audio to save. | AUDIO | Yes | - |
| `filename_prefix` | The prefix for the file to save. May include formatting tokens such as %date:yyyy-MM-dd%. (default: "audio/ComfyUI") | STRING | Yes | - |

### flac Inputs

The `flac` format does not require any additional settings.

### mp3 Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `quality` | The encoding quality for MP3 files. (default: "V0") | COMBO | Yes | "V0"<br>"128k"<br>"320k" |

### opus Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `quality` | The encoding quality for Opus files. (default: "128k") | COMBO | Yes | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

**Note:** The `quality` setting is shown only when `format` is `mp3` or `opus`. If no `quality` value is provided, the audio is saved using the selected format's default quality.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `audio` | The input audio, passed through after being saved. | AUDIO |
| `ui` | UI output containing the saved audio file information. | UI |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioAdvanced/en.md)

---
**Source fingerprint (SHA-256):** `5f3af49670b485bbd31f0ed0c5667c12e9b9b23014cadcf64442a486255d0e6d`
