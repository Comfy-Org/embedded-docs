El nodo ElevenLabs Text to Speech convierte texto escrito en audio hablado utilizando la API de ElevenLabs. Permite seleccionar una voz específica y ajustar diversas características del habla como estabilidad, velocidad y estilo para generar una salida de audio personalizada.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `voz` | Voz a utilizar para la síntesis de voz. Conéctelo desde el Selector de Voz o Clonación Instantánea de Voz. | CUSTOM | Sí | N/A |
| `texto` | El texto a convertir en voz. | STRING | Sí | N/A |
| `estabilidad` | Estabilidad de la voz. Valores más bajos proporcionan un rango emocional más amplio, valores más altos producen un habla más consistente pero potencialmente monótona (predeterminado: 0.5). | FLOAT | No | 0.0 - 1.0 |
| `aplicar_normalización_de_texto` | Modo de normalización de texto. 'auto' permite que el sistema decida, 'on' aplica siempre la normalización, 'off' la omite. | COMBO | No | `"auto"`<br>`"on"`<br>`"off"` |
| `modelo` | Modelo a utilizar para la conversión de texto a voz. Seleccionar un modelo revela sus parámetros específicos. | DYNAMICCOMBO | No | `"eleven_multilingual_v2"`<br>`"eleven_v3"` |
| `código_de_idioma` | Código de idioma ISO-639-1 o ISO-639-3 (ej., 'en', 'es', 'fra'). Déjelo vacío para detección automática (predeterminado: ""). | STRING | No | N/A |
| `semilla` | Semilla para reproducibilidad (no se garantiza determinismo) (predeterminado: 1). | INT | No | 0 - 2147483647 |
| `formato_de_salida` | Formato de salida de audio. | COMBO | No | `"mp3_44100_192"`<br>`"opus_48000_192"` |

**Parámetros Específicos del Modelo:**
Cuando el parámetro `model` está configurado en `"eleven_multilingual_v2"`, los siguientes parámetros adicionales están disponibles:

* `speed`: Velocidad del habla. 1.0 es normal, <1.0 más lento, >1.0 más rápido (predeterminado: 1.0, rango: 0.7 - 1.3).
* `similarity_boost`: Refuerzo de similitud. Valores más altos hacen que la voz sea más similar a la original (predeterminado: 0.75, rango: 0.0 - 1.0).
* `use_speaker_boost`: Refuerza la similitud con la voz del hablante original (predeterminado: Falso).
* `style`: Exageración del estilo. Valores más altos aumentan la expresión estilística pero pueden reducir la estabilidad (predeterminado: 0.0, rango: 0.0 - 0.2).

Cuando el parámetro `model` está configurado en `"eleven_v3"`, los siguientes parámetros adicionales están disponibles:

* `speed`: Velocidad del habla. 1.0 es normal, <1.0 más lento, >1.0 más rápido (predeterminado: 1.0, rango: 0.7 - 1.3).
* `similarity_boost`: Refuerzo de similitud. Valores más altos hacen que la voz sea más similar a la original (predeterminado: 0.75, rango: 0.0 - 1.0).

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `audio` | El audio generado a partir de la conversión de texto a voz. | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSpeech/es.md)

---
**Source fingerprint (SHA-256):** `d11d4ffa2d1f11dfd5ce378d9496cd9788d2197bf7f4135092ecefb287f3c2f7`
