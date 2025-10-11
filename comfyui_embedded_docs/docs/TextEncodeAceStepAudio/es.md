> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio/es.md)

El nodo TextEncodeAceStepAudio procesa entradas de texto para el condicionamiento de audio combinando etiquetas y letras en tokens, luego codificándolos con una fuerza de letra ajustable. Toma un modelo CLIP junto con descripciones de texto y letras, los tokeniza juntos y genera datos de condicionamiento adecuados para tareas de generación de audio. El nodo permite ajustar finamente la influencia de las letras a través de un parámetro de fuerza que controla su impacto en la salida final.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Sí | - | El modelo CLIP utilizado para la tokenización y codificación |
| `tags` | STRING | Sí | - | Etiquetas de texto o descripciones para el condicionamiento de audio (admite entrada multilínea y prompts dinámicos) |
| `lyrics` | STRING | Sí | - | Texto de letras para el condicionamiento de audio (admite entrada multilínea y prompts dinámicos) |
| `lyrics_strength` | FLOAT | No | 0.0 - 10.0 | Controla la fuerza de la influencia de las letras en la salida de condicionamiento (valor por defecto: 1.0, paso: 0.01) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | Los datos de condicionamiento codificados que contienen tokens de texto procesados con la fuerza de letra aplicada |