# YuE2 Generate ABC

This node generates ABC notation for a song based on a style description and lyrics, using a YuE2 text-and-lyrics model. The resulting `abc` output can be connected to the YuE2 Generate Music node to produce audio.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `clip` | The YuE2 model used to tokenize the style and lyrics and generate the ABC notation. | CLIP | Yes | - |
| `style` | Text describing the musical style of the song. | STRING | Yes | - |
| `lyrics` | Text containing the lyrics of the song. | STRING | Yes | - |
| `seed` | Random seed used for generation. Changing it produces different results. Default: 0. | INT | Yes | 0 to 18446744073709551615 |
| `mode` | full: generates melody and chords; melody: generates melody only, recommended for covers. | COMBO | Yes | "full"<br>"melody" |
| `max_abc_tokens` | Maximum number of tokens generated for the ABC notation. Default: 8192. | INT | Yes | 1 to 20000 |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `abc` | The generated ABC notation of the song, which can be connected to the YuE2 Generate Music node. | STRING |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateABC/en.md)

---
**Source fingerprint (SHA-256):** `3e06f980a53e90b750f4190a95199e0e5ed1bd8c54d4dbf8485602ff1af00102`
