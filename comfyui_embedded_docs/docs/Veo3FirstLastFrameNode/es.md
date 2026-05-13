> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3FirstLastFrameNode/es.md)

El nodo Veo3FirstLastFrameNode utiliza el modelo Veo 3 de Google para generar un video basado en un prompt de texto, con un primer y último fotograma proporcionados que definen el inicio y el final de la secuencia de video.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `prompt` | STRING | Sí | N/A | Descripción textual del video (valor predeterminado: cadena vacía). |
| `negative_prompt` | STRING | No | N/A | Prompt de texto negativo para guiar qué evitar en el video (valor predeterminado: cadena vacía). |
| `resolution` | COMBO | Sí | `"720p"`<br>`"1080p"`<br>`"4k"` | La resolución del video de salida. |
| `aspect_ratio` | COMBO | No | `"16:9"`<br>`"9:16"` | Relación de aspecto del video de salida (valor predeterminado: "16:9"). |
| `duration` | INT | No | 4 a 8 | Duración del video de salida en segundos (valor predeterminado: 8). |
| `seed` | INT | No | 0 a 4294967295 | Semilla para la generación del video (valor predeterminado: 0). |
| `first_frame` | IMAGE | Sí | N/A | El fotograma de inicio del video. |
| `last_frame` | IMAGE | Sí | N/A | El fotograma final del video. |
| `model` | COMBO | No | `"veo-3.1-generate"`<br>`"veo-3.1-fast-generate"`<br>`"veo-3.1-lite"` | El modelo Veo 3 específico a utilizar para la generación (valor predeterminado: "veo-3.1-generate"). |
| `generate_audio` | BOOLEAN | No | N/A | Generar audio para el video (valor predeterminado: True). |

**Nota:** El modelo `veo-3.1-lite` no admite resolución 4K. Si seleccionas `veo-3.1-lite` y resolución `4k`, se producirá un error.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El archivo de video generado. |

---
**Source fingerprint (SHA-256):** `b486b22e71a305172700760bb3eff256b0e571bba75e68f27e23a1e1a1319b5a`
