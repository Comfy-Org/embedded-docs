# ElevenLabs Voz a Texto

El nodo ElevenLabs Speech to Text transcribe audio a texto mediante la API de conversión de voz a texto de ElevenLabs. Es compatible con la detección automática de idioma, la identificación de qué hablante está hablando y el etiquetado de sonidos no lingüísticos, como (risas) o (música), en la transcripción.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | Modelo a utilizar para la transcripción. Al seleccionar un modelo se muestran sus parámetros específicos. | DYNAMIC_COMBO | Sí | `"scribe_v2"` |
| `audio` | Audio a transcribir. | AUDIO | Sí | - |
| `código_de_idioma` | Código de idioma ISO-639-1 o ISO-639-3 (p. ej., 'en', 'es', 'fra'). Déjelo vacío para la detección automática. (predeterminado: "") | STRING | No | - |
| `número_de_hablantes` | Número máximo de hablantes a predecir. Establezca 0 para la detección automática. (predeterminado: 0) | INT | No | 0 - 32 |
| `semilla` | Semilla para reproducibilidad (no se garantiza el determinismo). (predeterminado: 1) | INT | No | 0 - 2147483647 |

### Entradas de Scribe v2

Estos parámetros aparecen cuando se selecciona el modelo `"scribe_v2"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `tag_audio_events` | Anota sonidos como (risas), (música), etc. en la transcripción. (predeterminado: False) | BOOLEAN | No | - |
| `diarize` | Anota qué hablante está hablando. (predeterminado: False) | BOOLEAN | No | - |
| `diarization_threshold` | Sensibilidad de separación de hablantes. Los valores más bajos son más sensibles a los cambios de hablante. Solo se usa cuando `diarize` está habilitado. (predeterminado: 0.22) | FLOAT | No | 0.1 - 0.4 |
| `temperature` | Control de aleatoriedad. 0.0 utiliza el valor predeterminado del modelo. Los valores más altos aumentan la aleatoriedad. (predeterminado: 0.0) | FLOAT | No | 0.0 - 2.0 |
| `timestamps_granularity` | Precisión temporal para las palabras de la transcripción. (predeterminado: "word") | COMBO | No | `"word"`<br>`"character"`<br>`"none"` |

**Nota:** `num_speakers` no puede establecerse en un valor mayor que 0 cuando `diarize` está habilitado. Deshabilite `diarize` o establezca `num_speakers` en 0; de lo contrario, se producirá un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `texto` | El texto transcrito del audio. | STRING |
| `código_de_idioma` | El código de idioma detectado del audio. | STRING |
| `palabras_json` | Una cadena con formato JSON que contiene información detallada a nivel de palabra, incluidas marcas de tiempo y etiquetas de hablante si están habilitadas. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/es.md)

---
**Source fingerprint (SHA-256):** `7eb5d72615aa8a9e4a8014e45b39cf83dc8d8432d7ce0dccba20489be80a5830`
