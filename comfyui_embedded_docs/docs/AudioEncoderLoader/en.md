> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/en.md)

The AudioEncoderLoader node loads an audio encoder model from a file in your audio encoders folder. It takes the filename of an audio encoder model as input and returns the loaded model, which can then be used for audio processing tasks in your workflow.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `audio_encoder_name` | STRING | Yes | List of available audio encoder files in the audio_encoders folder | Selects which audio encoder model file to load |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `audio_encoder` | AUDIO_ENCODER | The loaded audio encoder model, ready for use in audio processing workflows |

---
**Source fingerprint (SHA-256):** `24cbd45198db7d950633358c29de57f56c999bc33534fabe80404528d194163c`
