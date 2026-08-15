# ElevenLabs Conversión de Voz a Voz

El nodo ElevenLabs Speech to Speech transforma un archivo de audio de entrada de una voz a otra. Utiliza la API de ElevenLabs para convertir el habla, preservando el contenido original y el tono emocional del audio.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `modelo` | Modelo a utilizar para la transformación de voz a voz. Cada opción de modelo proporciona un conjunto correspondiente de ajustes de voz (similarity_boost, style, use_speaker_boost, speed). | DYNAMIC_COMBO | No | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` |
| `voz` | Voz de destino para la transformación. Conectar desde Voice Selector o Instant Voice Clone. | CUSTOM | Sí | - |
| `audio` | Audio de origen a transformar. | AUDIO | Sí | - |
| `estabilidad` | Estabilidad de la voz. Los valores más bajos ofrecen un rango emocional más amplio; los valores más altos producen una voz más consistente pero potencialmente monótona (por defecto: 0.5). | FLOAT | No | 0.0 - 1.0 |
| `formato_de_salida` | Formato de audio de salida (por defecto: "mp3_44100_192"). | COMBO | No | `"mp3_44100_192"`<br>`"opus_48000_192"` |
| `semilla` | Semilla para reproducibilidad (por defecto: 0). | INT | No | 0 - 4294967295 |
| `eliminar_ruido_de_fondo` | Elimina el ruido de fondo del audio de entrada mediante aislamiento de audio (por defecto: False). | BOOLEAN | No | - |

### Ajustes de voz (compartidos por `eleven_multilingual_sts_v2` y `eleven_english_sts_v2`)

Cuando se selecciona un modelo, estos ajustes de voz quedan disponibles para la transformación.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `speed` | Velocidad del habla. 1.0 es normal, <1.0 más lenta, >1.0 más rápida (por defecto: 1.0). | FLOAT | No | 0.7 - 1.3 |
| `similarity_boost` | Refuerzo de similitud. Los valores más altos hacen que la voz sea más similar a la original (por defecto: 0.75). | FLOAT | No | 0.0 - 1.0 |
| `use_speaker_boost` | Refuerza la similitud con la voz del hablante original (por defecto: False). | BOOLEAN | No | - |
| `style` | Exageración del estilo. Los valores más altos aumentan la expresión estilística pero pueden reducir la estabilidad (por defecto: 0.0). | FLOAT | No | 0.0 - 0.2 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `audio` | El archivo de audio transformado en el formato de salida especificado. | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/es.md)

---
**Source fingerprint (SHA-256):** `a3cd602181d134b9ab517bfac092ea30b62ef5a9942a905c0c3e6959b34370ca`
