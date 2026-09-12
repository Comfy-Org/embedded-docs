# YuE2 Generate Music

Generates music tokens and acoustic conditioning from a style, lyrics, and an ABC notation. It returns the conditioning and the generated duration in seconds, which should be provided to the Empty YuE2 Latent Audio node. If the ABC input is left empty, the selected mode is ignored and off mode is used automatically.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `clip` | The CLIP model used to tokenize and encode the music inputs. | CLIP | Yes | - |
| `style` | Text describing the musical style. Supports multiline input and dynamic prompts. | STRING | Yes | Multiline text |
| `lyrics` | Lyrics for the generated music. Supports multiline input and dynamic prompts. | STRING | Yes | Multiline text |
| `abc` | Connect the ABC generator or supply an edited score. Leave empty to use off mode automatically. default: "" | STRING | Yes | Multiline text |
| `seed` | Random seed for generation. default: 0 | INT | Yes | 0 to 18446744073709551615 |
| `mode` | full: generates melody and chords; melody: generates melody only, recommended for covers. default: "full" | COMBO | Yes | "full"<br>"melody" |
| `max_duration` | Maximum duration; generation can stop earlier. The release uses a 360-second budget. default: 360.0 | FLOAT | Yes | 0.04 to 360.0 |
| `temperature` | Sampling temperature for generation. default: 1.0 | FLOAT | Yes | 0.0 to 5.0 |
| `top_p` | Nucleus sampling probability threshold. default: 0.95 | FLOAT | Yes | 0.01 to 1.0 |
| `top_k` | Top-k sampling limit. default: 100 | INT | Yes | 1 to 32768 |
| `repetition_penalty` | Penalty applied to repeated tokens. default: 1.2 | FLOAT | Yes | 0.01 to 10.0 |

Note: If `abc` is empty or contains only whitespace, the `mode` selection is ignored and off mode is used automatically.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `CONDITIONING` | Acoustic conditioning generated from the music tokens. | CONDITIONING |
| `seconds` | The generated audio duration in seconds. Provide this value to the Empty YuE2 Latent Audio node. | FLOAT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateMusic/en.md)

---
**Source fingerprint (SHA-256):** `5b498d0530da04da77d0dde2c4e52abdc7e5f60f54d3021dd19b5c802adbeadc`
