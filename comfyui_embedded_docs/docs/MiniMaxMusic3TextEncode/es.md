# MiniMaxMusic3TextEncode

MiniMax Music3 Text Encode utiliza el modelo MiniMax Music3 CLIP para convertir descripciones de texto y letras en secuencias de condicionamiento acústico destinadas a la generación de música. Este nodo devuelve los datos CONDITIONING convertidos, así como la duración real de audio en segundos calculada a partir de la duración de entrada.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `clip` | Modelo MiniMax Music3 CLIP utilizado para la codificación de texto y la generación de secuencias de condicionamiento. | CLIP | Sí | - |
| `caption` | Contenido de texto que describe la música a generar. Admite texto multilínea y prompts dinámicos. | STRING | Sí | - |
| `lyrics` | Texto de la letra que se utilizará para generar la música. Admite texto multilínea y prompts dinámicos. | STRING | Sí | - |
| `seed` | Semilla aleatoria reproducible para el proceso de generación. Valor predeterminado: 0. | INT | Sí | 0 a 18446744073709551615 (0xffffffffffffffff) |
| `max_duration` | Duración máxima (en segundos) de la música generada; el modelo puede finalizar la canción de forma anticipada. Valor predeterminado: 120.0. | FLOAT | Sí | 0.04 a la duración máxima de audio del modelo (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), paso 0.04 |
| `cfg_scale` | Factor de escala de guía libre de clasificador. Valor predeterminado: constante del modelo CFG_SCALE. Parámetro avanzado. | FLOAT | Sí | 0.0 a 100.0, paso 0.1 (se conservan 2 decimales) |
| `top_k` | Valor de muestreo top-k para la selección de tokens acústicos. Valor predeterminado: constante del modelo CFG_TOP_K. Parámetro avanzado. | INT | Sí | 1 al tamaño del vocabulario del modelo (C0_VOCAB_SIZE) |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `conditioning` | Secuencia de condicionamiento acústico generada, utilizada para guiar la generación musical posterior. | CONDITIONING |
| `seconds` | Duración real correspondiente a la secuencia de condicionamiento, en segundos. | FLOAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxMusic3TextEncode/es.md)

---
**Source fingerprint (SHA-256):** `c3fbfd189d0358ebf081dd4f9c32be9231a9d0b97fd767401ea4b7955224c25c`
