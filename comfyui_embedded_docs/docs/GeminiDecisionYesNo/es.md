# Google Gemini Decision (Yes/No)

Haz una pregunta de sí/no sobre el texto, las imágenes, el audio o el video que conectes y obtén un booleano con el que enrutar. Conecta `result` a un nodo If/Else Switch para enviar la ejecución por una de dos rutas, y lee `answer` y `probability` cuando quieras ver por qué el modelo respondió de esa manera.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model` | Modelo a usar (predeterminado: `"gemini-decision-1"`). | COMBO | Sí | `"gemini-decision-1"` |
| `question` | La pregunta de sí/no sobre lo que está conectado, de hasta 5000 caracteres. Formúlala de modo que «sí» sea el caso sobre el que actuar (predeterminado: "¿Hay una persona en la imagen?"). | STRING | Sí | 1 a 5000 caracteres |
| `threshold` | Probabilidad de «sí» a la que `result` se vuelve verdadero. Las respuestas claras de «sí» puntúan alrededor de 0.85 a 0.92, por lo que 0.9 o más rechaza muchas de ellas (predeterminado: 0.5). | FLOAT | Sí | 0.01 a 0.99 (paso 0.01) |
| `images` | Imágenes sobre las que preguntar, hasta 16 en total en las ranuras ampliables (`image_1` ... `image_16`). Una imagen en un lote cuenta una vez por cada imagen. | IMAGE | No | Hasta 16 imágenes |
| `audio` | Clip de audio sobre el que preguntar. | AUDIO | No | - |
| `video` | Clip de video sobre el que preguntar. | VIDEO | No | - |
| `text` | Texto sobre el que trata la pregunta, como un prompt o una respuesta de LLM, de hasta 20000 caracteres. | STRING | No | Hasta 20000 caracteres |

Conecta al menos uno de `text`, `images`, `audio` o `video`; el nodo lanza un error cuando no hay nada que examinar. Con varias imágenes, nómbralas `image_1`, `image_2`, etc. dentro de la pregunta.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `result` | La respuesta como booleano: verdadero para «sí», falso para «no». | BOOLEAN |
| `answer` | La respuesta como la cadena `"yes"` o `"no"`. | STRING |
| `probability` | Probabilidad de «sí» entre 0 y 1. | FLOAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionYesNo/es.md)

---
**Source fingerprint (SHA-256):** `0339031baf5648609b82526bed97ce8744986878bcbb706dcd3aa79a7370d83f`
