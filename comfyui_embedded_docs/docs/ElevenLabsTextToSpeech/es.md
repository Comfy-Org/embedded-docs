# ElevenLabs Texto a Voz

El nodo ElevenLabs Text to Speech convierte texto escrito en audio hablado mediante la API de ElevenLabs. Permite elegir una voz y ajustar características del habla como estabilidad, velocidad y estilo para crear una salida de audio personalizada.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `modelo` | Modelo a utilizar para la conversión de texto a voz. Al seleccionar un modelo, se muestran sus parámetros específicos. | DYNAMIC_COMBO | Sí | "eleven_multilingual_v2"<br>"eleven_v3" |
| `voz` | Voz a utilizar para la síntesis de voz. Conéctela desde Voice Selector o Instant Voice Clone. | ELEVENLABS_VOICE | Sí | N/A |
| `texto` | El texto a convertir en voz. Debe contener al menos un carácter. | STRING | Sí | N/A |
| `estabilidad` | Estabilidad de la voz. Los valores más bajos proporcionan un rango emocional más amplio; los valores más altos producen un habla más consistente pero potencialmente monótona (por defecto: 0.5). | FLOAT | Sí | 0.0 - 1.0 |
| `aplicar_normalización_de_texto` | Modo de normalización de texto. 'auto' permite que el sistema decida, 'on' aplica siempre la normalización, 'off' la omite. | COMBO | Sí | "auto"<br>"on"<br>"off" |
| `código_de_idioma` | Código de idioma ISO-639-1 o ISO-639-3 (p. ej., 'en', 'es', 'fra'). Déjelo vacío para la detección automática (por defecto: ""). | STRING | Sí | N/A |
| `semilla` | Semilla para reproducibilidad (no se garantiza el determinismo) (por defecto: 1). | INT | Sí | 0 - 2147483647 |
| `formato_de_salida` | Formato de salida de audio. | COMBO | Sí | "mp3_44100_192"<br>"opus_48000_192" |

### Entradas de eleven_multilingual_v2

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `speed` | Velocidad del habla. 1.0 es normal, <1.0 más lento, >1.0 más rápido (por defecto: 1.0). | FLOAT | Sí | 0.7 - 1.3 |
| `similarity_boost` | Refuerzo de similitud. Los valores más altos hacen que la voz sea más similar a la original (por defecto: 0.75). | FLOAT | Sí | 0.0 - 1.0 |
| `use_speaker_boost` | Aumenta la similitud con la voz del hablante original (por defecto: False). | BOOLEAN | Sí | True<br>False |
| `style` | Exageración del estilo. Los valores más altos aumentan la expresión estilística pero pueden reducir la estabilidad (por defecto: 0.0). | FLOAT | Sí | 0.0 - 0.2 |

### Entradas de eleven_v3

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `speed` | Velocidad del habla. 1.0 es normal, <1.0 más lento, >1.0 más rápido (por defecto: 1.0). | FLOAT | Sí | 0.7 - 1.3 |
| `similarity_boost` | Refuerzo de similitud. Los valores más altos hacen que la voz sea más similar a la original (por defecto: 0.75). | FLOAT | Sí | 0.0 - 1.0 |

**Nota:** La entrada `text` debe contener al menos un carácter. Si `language_code` se deja vacío, el idioma se detecta automáticamente. Los parámetros `use_speaker_boost` y `style` están disponibles únicamente para el modelo `eleven_multilingual_v2`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `audio` | El audio generado a partir de la conversión de texto a voz. | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSpeech/es.md)

---
**Source fingerprint (SHA-256):** `78ed1c6af2d0b1cc0293d725492a8b104b6d0c6bc18d9971b75047db946cdd33`
