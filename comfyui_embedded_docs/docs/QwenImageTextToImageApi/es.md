# QwenImageTextToImageApi

Qwen Image 3 Text to Image genera una o más imágenes a partir de un prompt de texto utilizando los modelos Qwen-Image 3.0. Seleccionas un modelo y proporcionas un prompt, y el nodo devuelve las imágenes generadas como un lote.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de dato | ¿Requerido? | Rango |
|-----------|-------------|--------------|-------------|-------|
| `model` | Modelo a utilizar (predeterminado: "qwen-image-3.0-pro"). Este selector compuesto también proporciona el prompt, el ancho de imagen, el alto de imagen y el prompt negativo opcional. | MODEL | Sí | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `n` | Número de imágenes a generar, devueltas como un lote (predeterminado: 1). | INT | No | 1 a 6 |
| `seed` | Semilla para la generación (predeterminado: 42). Puede configurarse para actualizarse automáticamente después de cada generación. | INT | No | 0 a 2147483647 |
| `prompt_extend` | Si se mejora el prompt con asistencia de IA (predeterminado: true). Opción avanzada. | BOOLEAN | No | true<br>false |
| `watermark` | Si se añade una marca de agua generada por IA al resultado (predeterminado: false). Opción avanzada. | BOOLEAN | No | true<br>false |

### Entradas de qwen-image-3.0-pro y qwen-image-3.0

Compartidas por qwen-image-3.0-pro y qwen-image-3.0.

| Parámetro | Descripción | Tipo de dato | ¿Requerido? | Rango |
|-----------|-------------|--------------|-------------|-------|
| `prompt` | Prompt que describe la imagen. Admite inglés y chino. Debe contener al menos 1 carácter. | STRING | Sí | Texto libre |
| `negative_prompt` | Prompt negativo que describe lo que se debe evitar (predeterminado: ""). | STRING | No | Texto libre |
| `width` | El área total de píxeles debe estar entre 512x512 y 2560x2560; cualquier relación de aspecto dentro de esa área funciona. (predeterminado: 1024) | INT | No | 256 a 2560 (paso 16) |
| `height` | El área total de píxeles debe estar entre 512x512 y 2560x2560; cualquier relación de aspecto dentro de esa área funciona. (predeterminado: 1024) | INT | No | 256 a 2560 (paso 16) |

Nota: La entrada `model` es un selector compuesto con los subcampos `model` (ID del modelo), `prompt` (obligatorio, debe contener al menos 1 carácter), `width` y `height` (dimensiones de la imagen), y `negative_prompt` (opcional). El área de píxeles combinada de `width` y `height` debe estar entre 262,144 píxeles (512x512) y 6,553,600 píxeles (2560x2560), y la relación de aspecto debe mantenerse entre 1:8 y 8:1.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `image` | La imagen o imágenes generadas, devueltas como un lote. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageTextToImageApi/es.md)

---
**Source fingerprint (SHA-256):** `c58454d26360a78b795b28dd776fa8650ec0ec7b1e4a902e81b6561f292e0fa2`
