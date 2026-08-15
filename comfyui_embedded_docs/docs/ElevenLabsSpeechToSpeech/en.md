# ElevenLabs Speech to Speech

The ElevenLabs Speech to Speech node transforms an input audio file from one voice to another. It uses the ElevenLabs API to convert speech while preserving the original content and emotional tone of the audio.

## Inputs

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | Model to use for speech-to-speech transformation. Each model option provides a matching set of voice settings (similarity_boost, style, use_speaker_boost, speed). | DYNAMIC_COMBO | No | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` |
| `voice` | Target voice for the transformation. Connect from Voice Selector or Instant Voice Clone. | CUSTOM | Yes | - |
| `audio` | Source audio to transform. | AUDIO | Yes | - |
| `stability` | Voice stability. Lower values give broader emotional range, higher values produce more consistent but potentially monotonous speech (default: 0.5). | FLOAT | No | 0.0 - 1.0 |
| `output_format` | Audio output format (default: "mp3_44100_192"). | COMBO | No | `"mp3_44100_192"`<br>`"opus_48000_192"` |
| `seed` | Seed for reproducibility (default: 0). | INT | No | 0 - 4294967295 |
| `remove_background_noise` | Remove background noise from input audio using audio isolation (default: False). | BOOLEAN | No | - |

### Voice Settings (Shared by `eleven_multilingual_sts_v2` and `eleven_english_sts_v2`)

When a model is selected, these voice settings become available for the transformation.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `speed` | Speech speed. 1.0 is normal, <1.0 slower, >1.0 faster (default: 1.0). | FLOAT | No | 0.7 - 1.3 |
| `similarity_boost` | Similarity boost. Higher values make the voice more similar to the original (default: 0.75). | FLOAT | No | 0.0 - 1.0 |
| `use_speaker_boost` | Boost similarity to the original speaker voice (default: False). | BOOLEAN | No | - |
| `style` | Style exaggeration. Higher values increase stylistic expression but may reduce stability (default: 0.0). | FLOAT | No | 0.0 - 0.2 |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `audio` | The transformed audio file in the specified output format. | AUDIO |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/en.md)

---
**Source fingerprint (SHA-256):** `a3cd602181d134b9ab517bfac092ea30b62ef5a9942a905c0c3e6959b34370ca`
