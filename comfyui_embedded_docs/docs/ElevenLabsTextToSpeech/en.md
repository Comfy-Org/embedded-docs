# ElevenLabs Text to Speech

The ElevenLabs Text to Speech node converts written text into spoken audio using the ElevenLabs API. It lets you choose a voice and adjust speech characteristics such as stability, speed, and style to create customized audio output.

## Inputs

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | Model to use for text-to-speech. Selecting a model reveals its specific parameters. | DYNAMIC_COMBO | Yes | "eleven_multilingual_v2"<br>"eleven_v3" |
| `voice` | Voice to use for speech synthesis. Connect from Voice Selector or Instant Voice Clone. | ELEVENLABS_VOICE | Yes | N/A |
| `text` | The text to convert to speech. Must contain at least one character. | STRING | Yes | N/A |
| `stability` | Voice stability. Lower values give broader emotional range, higher values produce more consistent but potentially monotonous speech (default: 0.5). | FLOAT | Yes | 0.0 - 1.0 |
| `apply_text_normalization` | Text normalization mode. 'auto' lets the system decide, 'on' always applies normalization, 'off' skips it. | COMBO | Yes | "auto"<br>"on"<br>"off" |
| `language_code` | ISO-639-1 or ISO-639-3 language code (e.g., 'en', 'es', 'fra'). Leave empty for automatic detection (default: ""). | STRING | Yes | N/A |
| `seed` | Seed for reproducibility (determinism not guaranteed) (default: 1). | INT | Yes | 0 - 2147483647 |
| `output_format` | Audio output format. | COMBO | Yes | "mp3_44100_192"<br>"opus_48000_192" |

### eleven_multilingual_v2 Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `speed` | Speech speed. 1.0 is normal, <1.0 slower, >1.0 faster (default: 1.0). | FLOAT | Yes | 0.7 - 1.3 |
| `similarity_boost` | Similarity boost. Higher values make the voice more similar to the original (default: 0.75). | FLOAT | Yes | 0.0 - 1.0 |
| `use_speaker_boost` | Boost similarity to the original speaker voice (default: False). | BOOLEAN | Yes | True<br>False |
| `style` | Style exaggeration. Higher values increase stylistic expression but may reduce stability (default: 0.0). | FLOAT | Yes | 0.0 - 0.2 |

### eleven_v3 Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `speed` | Speech speed. 1.0 is normal, <1.0 slower, >1.0 faster (default: 1.0). | FLOAT | Yes | 0.7 - 1.3 |
| `similarity_boost` | Similarity boost. Higher values make the voice more similar to the original (default: 0.75). | FLOAT | Yes | 0.0 - 1.0 |

**Note:** The `text` input must contain at least one character. If `language_code` is left empty, the language is detected automatically. The `use_speaker_boost` and `style` parameters are available only for the `eleven_multilingual_v2` model.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `audio` | The generated audio from the text-to-speech conversion. | AUDIO |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSpeech/en.md)

---
**Source fingerprint (SHA-256):** `78ed1c6af2d0b1cc0293d725492a8b104b6d0c6bc18d9971b75047db946cdd33`
