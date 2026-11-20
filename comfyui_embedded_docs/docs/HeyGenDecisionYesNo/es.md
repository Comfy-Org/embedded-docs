# HeyGen Decision (Yes/No)

Haz una pregunta de sí/no sobre el texto, las imágenes, el audio o el video que conectes y obtén un booleano para enrutar. Conecta `result` a un nodo If/Else Switch para elegir entre dos rutas, y lee `answer` y `probability` para ver qué tan clara fue la respuesta.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model` | Modelo que se va a usar. `heygen-decision-1-turbo` es más rápido y cuesta menos que `heygen-decision-1` (predeterminado: `"heygen-decision-1"`). | COMBO | Sí | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `question` | La pregunta de sí/no sobre lo que está conectado, de hasta 5000 caracteres. Formúlala de modo que «sí» sea el caso sobre el que se actúa (predeterminado: «¿Hay una persona en la imagen?»). | STRING | Sí | 1 a 5000 caracteres |
| `threshold` | Probabilidad de «sí» a la que `result` se vuelve true; las respuestas claras están cerca de 0 o 1 (predeterminado: 0.5). | FLOAT | Sí | 0.01 a 0.99 (paso: 0.01) |
| `images` | Imágenes sobre las que preguntar, hasta 4 en total, contando cada fotograma de un lote. Se numeran de `image_1` a `image_4` en orden a través de los sockets. | IMAGE | No | Hasta 4 imágenes |
| `audio_1` | Audio sobre el que preguntar, de hasta 30 minutos. | AUDIO | No | Hasta 30 minutos |
| `video_1` | Video sobre el que preguntar, de hasta 60 segundos. | VIDEO | No | Hasta 60 segundos |
| `text` | Texto sobre el que trata la pregunta, como un prompt o una respuesta de LLM, de hasta 20000 caracteres. | STRING | No | Hasta 20000 caracteres |

Conecta al menos uno de `text`, `images`, `audio_1` o `video_1`, y haz referencia a ellos por el nombre del socket dentro de la pregunta; por ejemplo, «¿Muestra image_2 a la misma persona que image_1?».

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `result` | La respuesta como un booleano: true para «sí», false para «no». | BOOLEAN |
| `answer` | La respuesta como la cadena `"yes"` o `"no"`. | STRING |
| `probability` | Probabilidad de «sí» entre 0 y 1. | FLOAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionYesNo/es.md)

---
**Source fingerprint (SHA-256):** `5a6a606d5c6ef62eb3424bd54a0da3dc177da7d0acf4b5c235a62b78ad8d2df1`
