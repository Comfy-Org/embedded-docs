El nodo TextEncodeAceStepAudio procesa entradas de texto para el acondicionamiento de audio combinando etiquetas y letras en tokens, luego codificándolos con una intensidad de letras ajustable. Toma un modelo CLIP junto con descripciones de texto y letras, los tokeniza en conjunto y genera datos de acondicionamiento adecuados para tareas de generación de audio. El nodo permite ajustar la influencia de las letras mediante un parámetro de intensidad que controla su impacto en la salida final.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `clip` | El modelo CLIP utilizado para tokenización y codificación | CLIP | Sí | - |
| `etiquetas` | Etiquetas o descripciones de texto para el acondicionamiento de audio (admite entrada multilínea y avisos dinámicos) | STRING | Sí | - |
| `letras` | Texto de letras para el acondicionamiento de audio (admite entrada multilínea y avisos dinámicos) | STRING | Sí | - |
| `intensidad_letras` | Controla la intensidad de la influencia de las letras en la salida de acondicionamiento (predeterminado: 1.0, incremento: 0.01) | FLOAT | No | 0.0 - 10.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `conditioning` | Los datos de acondicionamiento codificados que contienen los tokens de texto procesados con la intensidad de letras aplicada | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio/es.md)

---
**Source fingerprint (SHA-256):** `89600133d8b0edaa36958530dacffe812675b595b0d77db702bb7709567cd83d`
