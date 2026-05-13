> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/es.md)

El nodo ElevenLabs Speech to Speech transforma un archivo de audio de entrada de una voz a otra. Utiliza la API de ElevenLabs para convertir el habla preservando el contenido original y el tono emocional del audio.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `voz` | CUSTOM | Sí | - | Voz de destino para la transformación. Conéctelo desde el Selector de Voz o Clonación Instantánea de Voz. |
| `audio` | AUDIO | Sí | - | Audio de origen a transformar. |
| `estabilidad` | FLOAT | No | 0.0 - 1.0 | Estabilidad de la voz. Valores más bajos brindan un rango emocional más amplio; valores más altos producen un habla más consistente pero potencialmente monótona (predeterminado: 0.5). |
| `modelo` | DYNAMICCOMBO | No | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` | Modelo a utilizar para la transformación de voz a voz. Cada opción proporciona un conjunto específico de ajustes de voz (similarity_boost, style, use_speaker_boost, speed). |
| `formato_de_salida` | COMBO | No | `"mp3_44100_192"`<br>`"opus_48000_192"` | Formato de salida de audio (predeterminado: "mp3_44100_192"). |
| `semilla` | INT | No | 0 - 4294967295 | Semilla para reproducibilidad (predeterminado: 0). |
| `eliminar_ruido_de_fondo` | BOOLEAN | No | - | Eliminar el ruido de fondo del audio de entrada mediante aislamiento de audio (predeterminado: Falso). |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `audio` | AUDIO | El archivo de audio transformado en el formato de salida especificado. |

---
**Source fingerprint (SHA-256):** `118fe6e85b146d0649b104d814abb518d37f69ade2e53becac365a0ec90146fd`
