> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/es.md)

El nodo ElevenLabs Speech to Text transcribe archivos de audio a texto. Utiliza la API de ElevenLabs para convertir palabras habladas en una transcripción escrita, admitiendo funciones como detección automática de idioma, identificación de diferentes hablantes y etiquetado de sonidos no verbales como música o risas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Sí | - | Audio a transcribir. |
| `model` | COMBO | Sí | `"scribe_v2"` | Modelo a utilizar para la transcripción. Seleccionar este modelo revela parámetros adicionales. |
| `tag_audio_events` | BOOLEAN | No | - | Anota sonidos como (risas), (música), etc. en la transcripción. Este parámetro se revela cuando se selecciona el modelo `"scribe_v2"`. (valor por defecto: Falso) |
| `diarize` | BOOLEAN | No | - | Anota qué hablante está hablando. Este parámetro se revela cuando se selecciona el modelo `"scribe_v2"`. (valor por defecto: Falso) |
| `diarization_threshold` | FLOAT | No | 0.1 - 0.4 | Sensibilidad de separación de hablantes. Valores más bajos son más sensibles a los cambios de hablante. Este parámetro se revela cuando se selecciona el modelo `"scribe_v2"` y `diarize` está habilitado. (valor por defecto: 0.22) |
| `temperature` | FLOAT | No | 0.0 - 2.0 | Control de aleatoriedad. 0.0 usa el valor por defecto del modelo. Valores más altos aumentan la aleatoriedad. Este parámetro se revela cuando se selecciona el modelo `"scribe_v2"`. (valor por defecto: 0.0) |
| `timestamps_granularity` | COMBO | No | `"word"`<br>`"character"`<br>`"none"` | Precisión de temporización para las palabras de la transcripción. Este parámetro se revela cuando se selecciona el modelo `"scribe_v2"`. (valor por defecto: "word") |
| `language_code` | STRING | No | - | Código de idioma ISO-639-1 o ISO-639-3 (ej., 'en', 'es', 'fra'). Déjelo vacío para detección automática. (valor por defecto: "") |
| `num_speakers` | INT | No | 0 - 32 | Número máximo de hablantes a predecir. Establezca en 0 para detección automática. (valor por defecto: 0) |
| `seed` | INT | No | 0 - 2147483647 | Semilla para reproducibilidad (no se garantiza determinismo). (valor por defecto: 1) |

**Nota:** El parámetro `num_speakers` no puede establecerse en un valor mayor que 0 cuando la opción `diarize` está habilitada. Debe deshabilitar `diarize` o establecer `num_speakers` en 0.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `text` | STRING | El texto transcrito del audio. |
| `language_code` | STRING | El código de idioma detectado del audio. |
| `words_json` | STRING | Una cadena con formato JSON que contiene información detallada a nivel de palabra, incluyendo marcas de tiempo y etiquetas de hablante si están habilitadas. |
