# MiniMaxMusic3TextEncode

MiniMax Music3 Text Encode utiliza un modelo CLIP MiniMax Music3 para convertir descripciones de texto y letras en una secuencia de acondicionamiento acústico para la generación de música. El nodo devuelve los datos CONDITIONING resultantes, junto con la duración real del audio en segundos calculada a partir de la duración máxima de entrada.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `clip` | El modelo CLIP MiniMax Music3, utilizado para la codificación de texto y la generación de secuencias de acondicionamiento. | CLIP | Sí | - |
| `caption` | Texto que describe la música a generar. Admite texto multilínea y prompts dinámicos. | STRING | Sí | - |
| `letras` | El texto de la letra que se utilizará para generar la música. Admite texto multilínea y prompts dinámicos. | STRING | Sí | - |
| `semilla` | Semilla aleatoria reproducible para el proceso de generación. Valor predeterminado: 0. | INT | Sí | 0 a 18446744073709551615 (0xffffffffffffffff) |
| `max_duration` | Duración máxima en segundos; el modelo puede finalizar la canción antes. Valor predeterminado: 120.0. | FLOAT | Sí | 0.04 to the model's maximum audio duration (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), step 0.04 |
| `cfg_scale` | Escala de guía sin clasificador. Valor predeterminado: constante CFG_SCALE del modelo. Parámetro avanzado. | FLOAT | Sí | 0.0 a 100.0, step 0.1 (keeps 2 decimal places) |
| `top_k` | Valor de muestreo top-k utilizado para la selección de tokens acústicos. Valor predeterminado: constante CFG_TOP_K del modelo. Parámetro avanzado. | INT | Sí | 1 to the model's vocabulary size (C0_VOCAB_SIZE) |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `conditioning` | La secuencia de acondicionamiento acústico generada, utilizada para guiar la generación de música posterior. | CONDITIONING |
| `segundos` | La duración real de la secuencia de acondicionamiento, en segundos. | FLOAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxMusic3TextEncode/es.md)

---
**Source fingerprint (SHA-256):** `c3fbfd189d0358ebf081dd4f9c32be9231a9d0b97fd767401ea4b7955224c25c`
