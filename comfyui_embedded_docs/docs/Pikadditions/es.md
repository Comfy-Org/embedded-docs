> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikadditions/es.md)

El nodo Pikadditions permite agregar cualquier objeto o imagen a tu video. Subes un video y especificas qué te gustaría añadir para obtener un resultado integrado de forma natural. Este nodo utiliza la API de Pika para insertar imágenes en videos con una integración de aspecto realista.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `video` | VIDEO | Sí | - | El video al que se le agregará una imagen. |
| `image` | IMAGE | Sí | - | La imagen que se agregará al video. |
| `prompt_text` | STRING | Sí | - | Descripción textual de lo que se agregará al video. |
| `negative_prompt` | STRING | Sí | - | Descripción textual de lo que se debe evitar en el video. |
| `seed` | INT | Sí | 0 a 4294967295 | Valor de semilla aleatoria para obtener resultados reproducibles. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El video procesado con la imagen insertada. |

---
**Source fingerprint (SHA-256):** `cf7bb4ee0a672e20c0ffc128fa95df43e05356aea03b2070f928a0263aff6234`
