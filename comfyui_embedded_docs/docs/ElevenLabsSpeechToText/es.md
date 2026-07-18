El nodo ElevenLabs Speech to Text transcribe archivos de audio a texto. Utiliza la API de ElevenLabs para convertir palabras habladas en una transcripción escrita, con funciones como detección automática de idioma, identificación de diferentes hablantes y etiquetado de sonidos no verbales como música o risas.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `audio` | Audio a transcribir. | AUDIO | Sí | - |
| `modelo` | Modelo a utilizar para la transcripción. Al seleccionar este modelo se revelan parámetros adicionales. | COMBO | Sí | `"scribe_v2"` |
| `tag_audio_events` | Anotar sonidos como (risas), (música), etc. en la transcripción. Este parámetro se revela cuando se selecciona el modelo `"scribe_v2"`. (predeterminado: False) | BOOLEAN | No | - |
| `diarize` | Anotar qué hablante está hablando. Este parámetro se revela cuando se selecciona el modelo `"scribe_v2"`. (predeterminado: False) | BOOLEAN | No | - |
| `diarization_threshold` | Sensibilidad de separación de hablantes. Valores más bajos son más sensibles a cambios de hablante. Este parámetro se revela cuando se selecciona el modelo `"scribe_v2"` y `diarize` está habilitado. (predeterminado: 0.22) | FLOAT | No | 0.1 - 0.4 |
| `temperature` | Control de aleatoriedad. 0.0 usa el valor predeterminado del modelo. Valores más altos aumentan la aleatoriedad. Este parámetro se revela cuando se selecciona el modelo `"scribe_v2"`. (predeterminado: 0.0) | FLOAT | No | 0.0 - 2.0 |
| `timestamps_granularity` | Precisión de tiempo para las palabras de la transcripción. Este parámetro se revela cuando se selecciona el modelo `"scribe_v2"`. (predeterminado: "word") | COMBO | No | `"word"`<br>`"character"`<br>`"none"` |
| `código_de_idioma` | Código de idioma ISO-639-1 o ISO-639-3 (ej. 'en', 'es', 'fra'). Déjelo vacío para detección automática. (predeterminado: "") | STRING | No | - |
| `número_de_hablantes` | Número máximo de hablantes a predecir. Establezca en 0 para detección automática. (predeterminado: 0) | INT | No | 0 - 32 |
| `semilla` | Semilla para reproducibilidad (no se garantiza determinismo). (predeterminado: 1) | INT | No | 0 - 2147483647 |

**Nota:** El parámetro `num_speakers` no puede establecerse en un valor mayor a 0 cuando la opción `diarize` está habilitada. Debe deshabilitar `diarize` o establecer `num_speakers` en 0.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `texto` | El texto transcrito del audio. | STRING |
| `código_de_idioma` | El código de idioma detectado del audio. | STRING |
| `palabras_json` | Una cadena con formato JSON que contiene información detallada a nivel de palabra, incluyendo marcas de tiempo y etiquetas de hablante si están habilitadas. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/es.md)

---
**Source fingerprint (SHA-256):** `aca2ac04d7280ef2b604f7c8d29ad7fea1e7abcfc38beabb64ba6b268a8cade1`
