# Stability AI Texto a Audio

Genera música y efectos de sonido de alta calidad a partir de descripciones textuales. Este nodo utiliza la tecnología de generación de audio de Stability AI para crear contenido de audio basado en tus indicaciones de texto.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de generación de audio a utilizar (predeterminado: "stable-audio-2.5") | COMBO | Sí | `"stable-audio-2.5"` |
| `prompt` | La descripción textual utilizada para generar contenido de audio (predeterminado: cadena vacía) | STRING | Sí | - |
| `duración` | Controla la duración en segundos del audio generado (predeterminado: 190) | INT | No | 1-190 |
| `semilla` | La semilla aleatoria utilizada para la generación (predeterminado: 0) | INT | No | 0-4294967294 |
| `pasos` | Controla el número de pasos de muestreo (predeterminado: 8) | INT | No | 4-8 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `audio` | El archivo de audio generado a partir de la indicación de texto | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityTextToAudio/es.md)

---
**Source fingerprint (SHA-256):** `5185241ca7a9b4bc38dfa8bafdae63ec3c151a3038a26ffe8e35492c0550fa88`
