# ElevenLabs Text to Sound Effects

The ElevenLabs Text to Sound Effects node generates sound effect audio from a text description using the ElevenLabs API. It sends your written prompt to the ElevenLabs sound generation service and returns the resulting audio, with controls for the duration, looping behavior, and how closely the sound follows the text.

## Inputs

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | Model to use for sound effect generation. The selected model determines the available generation parameters listed below. | DYNAMIC_COMBO | Yes | `"eleven_sfx_v2"` |
| `text` | Text description of the sound effect to generate. Must contain at least 1 character. (default: empty) | STRING | Yes | N/A |
| `output_format` | Audio output format. | COMBO | Yes | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### Eleven SFX v2 Inputs

Sub-parameters shown when `model` is set to `"eleven_sfx_v2"`.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `duration` | Duration of generated sound in seconds. (default: 5.0) | FLOAT | Yes | 0.5 to 30.0 (step: 0.1) |
| `loop` | Create a smoothly looping sound effect. (default: False) | BOOLEAN | No | True or False |
| `prompt_influence` | How closely generation follows the prompt. Higher values make the sound follow the text more closely. (default: 0.3) | FLOAT | Yes | 0.0 to 1.0 (step: 0.01) |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `audio` | The generated sound effect audio file. | AUDIO |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/en.md)

---
**Source fingerprint (SHA-256):** `218ff617256cea33f310c1bcfc6407c46aaadc59201a0324b0ec64583166ce58`
