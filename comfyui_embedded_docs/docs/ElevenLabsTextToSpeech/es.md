> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSpeech/es.md)

El nodo ElevenLabs Text to Speech convierte texto escrito en audio hablado utilizando la API de ElevenLabs. Permite seleccionar una voz específica y ajustar varias características del habla, como estabilidad, velocidad y estilo, para generar una salida de audio personalizada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `voice` | CUSTOM | Sí | N/A | Voz a utilizar para la síntesis de voz. Conectar desde Voice Selector o Instant Voice Clone. |
| `text` | STRING | Sí | N/A | El texto a convertir en voz. |
| `stability` | FLOAT | No | 0.0 - 1.0 | Estabilidad de la voz. Valores más bajos dan un rango emocional más amplio, valores más altos producen un habla más consistente pero potencialmente monótona (por defecto: 0.5). |
| `apply_text_normalization` | COMBO | No | `"auto"`<br>`"on"`<br>`"off"` | Modo de normalización de texto. 'auto' deja que el sistema decida, 'on' siempre aplica normalización, 'off' la omite. |
| `model` | DYNAMICCOMBO | No | `"eleven_multilingual_v2"`<br>`"eleven_v3"` | Modelo a utilizar para la conversión de texto a voz. Seleccionar un modelo revela sus parámetros específicos. |
| `language_code` | STRING | No | N/A | Código de idioma ISO-639-1 o ISO-639-3 (ej., 'en', 'es', 'fra'). Dejar vacío para detección automática (por defecto: ""). |
| `seed` | INT | No | 0 - 2147483647 | Semilla para reproducibilidad (no se garantiza determinismo) (por defecto: 1). |
| `output_format` | COMBO | No | `"mp3_44100_192"`<br>`"opus_48000_192"` | Formato de salida de audio. |

**Parámetros Específicos del Modelo:**
Cuando el parámetro `model` se establece en `"eleven_multilingual_v2"`, los siguientes parámetros adicionales están disponibles:

* `speed`: Velocidad del habla. 1.0 es normal, <1.0 más lento, >1.0 más rápido (por defecto: 1.0, rango: 0.7 - 1.3).
* `similarity_boost`: Refuerzo de similitud. Valores más altos hacen que la voz sea más similar a la original (por defecto: 0.75, rango: 0.0 - 1.0).
* `use_speaker_boost`: Refuerza la similitud con la voz original del hablante (por defecto: False).
* `style`: Exageración del estilo. Valores más altos aumentan la expresión estilística pero pueden reducir la estabilidad (por defecto: 0.0, rango: 0.0 - 0.2).

Cuando el parámetro `model` se establece en `"eleven_v3"`, los siguientes parámetros adicionales están disponibles:

* `speed`: Velocidad del habla. 1.0 es normal, <1.0 más lento, >1.0 más rápido (por defecto: 1.0, rango: 0.7 - 1.3).
* `similarity_boost`: Refuerzo de similitud. Valores más altos hacen que la voz sea más similar a la original (por defecto: 0.75, rango: 0.0 - 1.0).

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `audio` | AUDIO | El audio generado a partir de la conversión de texto a voz. |
