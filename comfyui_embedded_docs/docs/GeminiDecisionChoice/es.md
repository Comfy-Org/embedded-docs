# Google Gemini Decision (Choice)

Elige una de tus propias opciones para el texto, las imágenes, el audio o el video que conectes, y obtén la opción elegida, su posición y una confianza. Conecta `choice` a un nodo Branch cuyas entradas lleven los mismos nombres de opción, o enruta según `option_index` cuando no haya un nodo Branch disponible.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model` | Modelo a usar (predeterminado: `"gemini-decision-1"`). | COMBO | Sí | `"gemini-decision-1"` |
| `question` | La pregunta a la que responden las opciones, hasta 5000 caracteres (predeterminado: "What style is the image?"). | STRING | Sí | 1 a 5000 caracteres |
| `options` | Una opción por línea, usada exactamente como se escribió, hasta 128 caracteres cada una. Agrega una opción como `other` para entradas que no encajen en ninguna de ellas (predeterminado: `photo`, `illustration`, `3d render`, `anime`, `sketch`, `other`). | STRING | Sí | 2 a 255 opciones |
| `images` | Imágenes a clasificar, hasta 16 entre las ranuras ampliables (`image_1` ... `image_16`). Una imagen procesada en lote cuenta una vez por cada imagen. | IMAGE | No | Hasta 16 imágenes |
| `audio` | Clip de audio a clasificar. | AUDIO | No | - |
| `video` | Clip de video a clasificar. | VIDEO | No | - |
| `text` | Texto sobre el que trata la pregunta, como un prompt o una respuesta de LLM, hasta 20000 caracteres. | STRING | No | Hasta 20000 caracteres |

Proporciona al menos 2 y como máximo 255 opciones, y no repitas ninguna; de lo contrario, el nodo genera un error. Conecta al menos uno de `text`, `images`, `audio` o `video`, y nombra varias imágenes como `image_1`, `image_2`, etc., dentro de la pregunta.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `choice` | La opción elegida, exactamente como se escribió en `options`. | STRING |
| `option_index` | Posición de la opción elegida en `options`, comenzando en 0. | INT |
| `confidence` | Confianza en la elección, entre 0 y 1. | FLOAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionChoice/es.md)

---
**Source fingerprint (SHA-256):** `200c63a9197cd95ba0a21da88c5f3117014b37b0651541094a775219381afe43`
