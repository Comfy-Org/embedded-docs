# QwenImageTextToImageApi

Qwen Image 3 Text to Image genera una o más imágenes a partir de un prompt de texto utilizando los modelos Qwen-Image 3.0. Seleccionas un modelo y proporcionas un prompt, y el nodo devuelve las imágenes generadas como un lote.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `model` | Modelo a utilizar (por defecto: "qwen-image-3.0-pro"). Este selector compuesto también proporciona el prompt, el ancho de imagen, el alto de imagen y el prompt negativo opcional. | MODEL | Sí | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `n` | Número de imágenes a generar, devueltas como un lote (por defecto: 1). | INT | No | 1 a 6 |
| `seed` | Semilla a utilizar para la generación (por defecto: 42). Puede configurarse para actualizarse automáticamente después de cada generación. | INT | No | 0 a 2147483647 |
| `prompt_extend` | Si se debe mejorar el prompt con asistencia de IA (por defecto: true). Opción avanzada. | BOOLEAN | No | true<br>false |
| `watermark` | Si se debe añadir una marca de agua generada por IA al resultado (por defecto: false). Opción avanzada. | BOOLEAN | No | true<br>false |

Nota: La entrada `model` es un selector compuesto con los siguientes subcampos: `model` (ID del modelo), `prompt` (el prompt de texto, que debe contener al menos 1 carácter), `width` y `height` (dimensiones de imagen, validadas por el nodo), y `negative_prompt` (prompt negativo opcional).

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `image` | La imagen o imágenes generadas, devueltas como un lote. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageTextToImageApi/es.md)

---
**Source fingerprint (SHA-256):** `c58454d26360a78b795b28dd776fa8650ec0ec7b1e4a902e81b6561f292e0fa2`
