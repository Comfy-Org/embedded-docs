# Google Gemini Decision (Score)

Califica del 1 al 10 el texto, las imágenes, el audio o el video que conectes, y obtén la puntuación más un booleano que cambia en un umbral que establezcas. Úsalo para filtrar u ordenar salidas; por ejemplo, para conservar solo las imágenes que obtengan al menos 7, y conecta `result` a un nodo If/Else Switch para actuar en consecuencia.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model` | Modelo a usar (predeterminado: `"gemini-decision-1"`). | COMBO | Sí | `"gemini-decision-1"` |
| `question` | Qué evaluar, indicando qué significan 1 y 10 (predeterminado: "Rate the technical quality of the image from 1 (worst) to 10 (best)."). | STRING | Sí | 1 a 5000 caracteres |
| `threshold` | `result` es verdadero cuando la puntuación es al menos este valor. Las imágenes limpias y nítidas suelen puntuar alrededor de 7 a 8; las muy dañadas, alrededor de 3 a 5 (predeterminado: 6.0). | FLOAT | Sí | 1.0 a 10.0 (paso: 0.1) |
| `images` | Imágenes a evaluar, hasta 16 en las ranuras ampliables (`image_1` ... `image_16`). Una imagen por lotes cuenta una vez por cada imagen. | IMAGE | No | Hasta 16 imágenes |
| `audio` | Clip de audio a evaluar. | AUDIO | No | - |
| `video` | Clip de video a evaluar. | VIDEO | No | - |
| `text` | Texto sobre el que trata la pregunta, como un prompt o una respuesta de LLM, de hasta 20000 caracteres. | STRING | No | Hasta 20000 caracteres |

Conecta al menos uno de `text`, `images`, `audio` o `video`; el nodo lanza un error cuando no hay nada que evaluar. Si hay varias imágenes, nómbralas `image_1`, `image_2`, etc., dentro de la pregunta.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `result` | Verdadero cuando la puntuación es al menos `threshold`; de lo contrario, falso. | BOOLEAN |
| `score` | La puntuación del 1 al 10. | FLOAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionScore/es.md)

---
**Source fingerprint (SHA-256):** `9b0a68cc7f29b1d4d23e23e051a008f34932aac6d1fe1a16e45a0e70b4df412f`
