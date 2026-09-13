# ElevenLabs Texto a Voz

El nodo ElevenLabs Text to Speech convierte texto escrito en audio hablado usando la API de ElevenLabs. Permite seleccionar una voz específica y ajustar diversas características del habla, como la estabilidad, la velocidad y el estilo, para generar una salida de audio personalizada. El texto debe contener al menos un carácter.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model` | Modelo que se utilizará para texto a voz. Al seleccionar un modelo, se revelan sus parámetros específicos. | DYNAMIC_COMBO | No | `"eleven_multilingual_v2"`<br>`"eleven_v3"` |
| `voice` | Voz que se utilizará para la síntesis de voz. Conectar desde Voice Selector o Instant Voice Clone. | CUSTOM | Sí | N/A |
| `text` | El texto que se convertirá a voz. Debe contener al menos un carácter. | STRING | Sí | N/A |
| `stability` | Estabilidad de la voz. Los valores más bajos ofrecen un rango emocional más amplio; los valores más altos producen un habla más consistente pero potencialmente monótona (predeterminado: 0.5). | FLOAT | No | 0.0 - 1.0 |
| `apply_text_normalization` | Modo de normalización de texto. 'auto' deja que el sistema decida, 'on' siempre aplica la normalización, 'off' la omite. | COMBO | No | `"auto"`<br>`"on"`<br>`"off"` |
| `language_code` | Código de idioma ISO-639-1 o ISO-639-3 (p. ej., 'en', 'es', 'fra'). Dejar vacío para detección automática (predeterminado: ""). | STRING | No | N/A |
| `seed` | Semilla para reproducibilidad (no se garantiza el determinismo) (predeterminado: 1). | INT | No | 0 - 2147483647 |
| `output_format` | Formato de salida de audio. | COMBO | No | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### Entradas de eleven_multilingual_v2

Estos parámetros están disponibles cuando `model` se establece en `"eleven_multilingual_v2"`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `speed` | Velocidad del habla. 1.0 es normal, <1.0 más lento, >1.0 más rápido (predeterminado: 1.0). | FLOAT | No | 0.7 - 1.3 |
| `similarity_boost` | Refuerzo de similitud. Los valores más altos hacen que la voz sea más similar a la original (predeterminado: 0.75). | FLOAT | No | 0.0 - 1.0 |
| `use_speaker_boost` | Refuerza la similitud con la voz del hablante original (predeterminado: False). | BOOLEAN | No | True / False |
| `style` | Exageración del estilo. Los valores más altos aumentan la expresión estilística, pero pueden reducir la estabilidad (predeterminado: 0.0). | FLOAT | No | 0.0 - 0.2 |

### Entradas de eleven_v3

Estos parámetros están disponibles cuando `model` se establece en `"eleven_v3"`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `speed` | Velocidad del habla. 1.0 es normal, <1.0 más lento, >1.0 más rápido (predeterminado: 1.0). | FLOAT | No | 0.7 - 1.3 |
| `similarity_boost` | Refuerzo de similitud. Los valores más altos hacen que la voz sea más similar a la original (predeterminado: 0.75). | FLOAT | No | 0.0 - 1.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `audio` | El audio generado a partir de la conversión de texto a voz. | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSpeech/es.md)

---
**Source fingerprint (SHA-256):** `78ed1c6af2d0b1cc0293d725492a8b104b6d0c6bc18d9971b75047db946cdd33`
