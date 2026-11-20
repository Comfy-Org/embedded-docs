# HeyGen Decision (Choice)

Elija una de sus propias opciones para el texto, las imágenes, el audio o el video que conecte, y obtenga la opción elegida, su posición y una confianza. Conecte `choice` a un nodo Branch cuyas entradas lleven los mismos nombres de opción, o enrute según `option_index`.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model` | Modelo a usar. `heygen-decision-1-turbo` es más rápido y cuesta menos que `heygen-decision-1` (predeterminado: `"heygen-decision-1"`). | COMBO | Sí | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `question` | La pregunta que responden las opciones, hasta 5000 caracteres (predeterminado: "What style is the image?"). | STRING | Sí | 1 a 5000 caracteres |
| `options` | Una opción por línea, utilizada exactamente como se escribe, hasta 128 caracteres cada una. Agregue una opción como `other` para entradas que no encajen en ninguna de ellas (predeterminado: `photo`, `illustration`, `3d render`, `anime`, `sketch`, `other`). | STRING | Sí | 2 a 255 opciones |
| `images` | Imágenes a clasificar, hasta 4 en total, contando cada fotograma de un lote. Se numeran de `image_1` a `image_4` en orden a través de los sockets. | IMAGE | No | Hasta 4 imágenes |
| `audio_1` | Audio a clasificar, hasta 30 minutos. | AUDIO | No | Hasta 30 minutos |
| `video_1` | Video a clasificar, hasta 60 segundos. | VIDEO | No | Hasta 60 segundos |
| `text` | Texto sobre el que trata la pregunta, como un prompt o una respuesta de un LLM, hasta 20000 caracteres. | STRING | No | Hasta 20000 caracteres |

Proporcione de 2 a 255 opciones, ninguna de ellas repetida y ninguna que difiera solo en mayúsculas y minúsculas, o el nodo lanza un error. Conecte al menos una entrada para clasificar y nómbrelas por socket dentro de la pregunta, por ejemplo: «¿Qué temporada se muestra en image_1?».

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `choice` | La opción elegida, exactamente como se escribió en `options`. | STRING |
| `option_index` | Posición de la opción elegida en `options`, comenzando en 0. | INT |
| `confidence` | Confianza en la elección, entre 0 y 1. | FLOAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionChoice/es.md)

---
**Source fingerprint (SHA-256):** `dd21b3b8021b8917e7ee4d120471974634ae6771ff17b0f49e9460f82a2fbe78`
