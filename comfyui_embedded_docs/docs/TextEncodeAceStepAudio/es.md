# TextEncodeAceStepAudio

El nodo TextEncodeAceStepAudio procesa entradas de texto para el acondicionamiento de audio combinando etiquetas y letras en tokens, y luego codificándolos con una fuerza de letras ajustable. Toma un modelo CLIP junto con descripciones de texto y letras, los tokeniza juntos y genera datos de acondicionamiento adecuados para tareas de generación de audio. El nodo permite ajustar finamente la influencia de las letras mediante un parámetro de fuerza que controla su impacto en la salida final.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `clip` | El modelo CLIP utilizado para la tokenización y codificación | CLIP | Sí | - |
| `tags` | Etiquetas o descripciones de texto para el acondicionamiento de audio (admite entrada multilínea y prompts dinámicos) | STRING | Sí | - |
| `lyrics` | Texto de letras para el acondicionamiento de audio (admite entrada multilínea y prompts dinámicos) | STRING | Sí | - |
| `lyrics_strength` | Controla la fuerza de influencia de las letras en la salida del acondicionamiento (predeterminado: 1.0, paso: 0.01) | FLOAT | No | 0.0 - 10.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `conditioning` | Los datos de acondicionamiento codificados que contienen tokens de texto procesados con la fuerza de letras aplicada | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio/es.md)

---
**Source fingerprint (SHA-256):** `2226c9f25dd26bf454bcce2e298d6d261dace5a9bbed164a2fcf0e1204d7c3f4`
