# ElevenLabs Texto a Voz

El nodo ElevenLabs Text to Speech convierte texto escrito en audio hablado mediante la API de ElevenLabs. Permite seleccionar una voz específica y ajustar con precisión diversas características del habla, como estabilidad, velocidad y estilo, para generar una salida de audio personalizada.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `modelo` | Modelo a utilizar para la conversión de texto a voz. Al seleccionar un modelo, se muestran sus parámetros específicos. | DYNAMIC_COMBO | No | `"eleven_multilingual_v2"`<br>`"eleven_v3"` |
| `voz` | Voz a utilizar para la síntesis del habla. Conéctela desde el Selector de voz o Instant Voice Clone. | CUSTOM | Sí | N/A |
| `texto` | El texto que se convertirá en voz. Debe contener al menos un carácter. | STRING | Sí | N/A |
| `estabilidad` | Estabilidad de la voz. Los valores más bajos ofrecen un rango emocional más amplio; los valores más altos producen un habla más consistente pero potencialmente monótona (predeterminado: 0.5). | FLOAT | No | 0.0 - 1.0 |
| `aplicar_normalización_de_texto` | Modo de normalización del texto. 'auto' permite que el sistema decida, 'on' aplica siempre la normalización, 'off' la omite. | COMBO | No | `"auto"`<br>`"on"`<br>`"off"` |
| `código_de_idioma` | Código de idioma ISO-639-1 o ISO-639-3 (p. ej., 'en', 'es', 'fra'). Déjelo vacío para la detección automática (predeterminado: ""). | STRING | No | N/A |
| `semilla` | Semilla para reproducibilidad (no se garantiza el determinismo) (predeterminado: 1). | INT | No | 0 - 2147483647 |
| `formato_de_salida` | Formato de salida de audio. | COMBO | No | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### Entradas de eleven_multilingual_v2

Estos parámetros están disponibles cuando `model` está configurado como `"eleven_multilingual_v2"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `speed` | Velocidad del habla. 1.0 es normal, <1.0 más lenta, >1.0 más rápida (predeterminado: 1.0). | FLOAT | No | 0.7 - 1.3 |
| `similarity_boost` | Refuerzo de similitud. Los valores más altos hacen que la voz sea más similar a la original (predeterminado: 0.75). | FLOAT | No | 0.0 - 1.0 |
| `use_speaker_boost` | Refuerza la similitud con la voz del hablante original (predeterminado: False). | BOOLEAN | No | True / False |
| `style` | Exageración del estilo. Los valores más altos aumentan la expresión estilística pero pueden reducir la estabilidad (predeterminado: 0.0). | FLOAT | No | 0.0 - 0.2 |

### Entradas de eleven_v3

Estos parámetros están disponibles cuando `model` está configurado como `"eleven_v3"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `speed` | Velocidad del habla. 1.0 es normal, <1.0 más lenta, >1.0 más rápida (predeterminado: 1.0). | FLOAT | No | 0.7 - 1.3 |
| `similarity_boost` | Refuerzo de similitud. Los valores más altos hacen que la voz sea más similar a la original (predeterminado: 0.75). | FLOAT | No | 0.0 - 1.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `audio` | El audio generado a partir de la conversión de texto a voz. | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSpeech/es.md)

---
**Source fingerprint (SHA-256):** `78ed1c6af2d0b1cc0293d725492a8b104b6d0c6bc18d9971b75047db946cdd33`
