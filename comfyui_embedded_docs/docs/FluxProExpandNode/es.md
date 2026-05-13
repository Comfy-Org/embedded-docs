> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProExpandNode/es.md)

Expande una imagen basándose en un `prompt`. Este nodo amplía una imagen añadiendo píxeles en los lados superior, inferior, izquierdo y derecho, mientras genera nuevo contenido que coincide con la descripción de texto proporcionada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que se va a expandir |
| `prompt` | STRING | No | - | Prompt para la generación de la imagen (predeterminado: "") |
| `prompt_upsampling` | BOOLEAN | No | - | Si se debe realizar un sobremuestreo en el `prompt`. Si está activo, modifica automáticamente el `prompt` para una generación más creativa, pero los resultados no son deterministas (la misma semilla no producirá exactamente el mismo resultado). (predeterminado: False) |
| `top` | INT | No | 0-2048 | Número de píxeles a expandir en la parte superior de la imagen (predeterminado: 0) |
| `bottom` | INT | No | 0-2048 | Número de píxeles a expandir en la parte inferior de la imagen (predeterminado: 0) |
| `left` | INT | No | 0-2048 | Número de píxeles a expandir en la parte izquierda de la imagen (predeterminado: 0) |
| `right` | INT | No | 0-2048 | Número de píxeles a expandir en la parte derecha de la imagen (predeterminado: 0) |
| `guidance` | FLOAT | No | 1.5-100 | Fuerza de guía para el proceso de generación de la imagen (predeterminado: 60) |
| `steps` | INT | No | 15-50 | Número de pasos para el proceso de generación de la imagen (predeterminado: 50) |
| `seed` | INT | No | 0-18446744073709551615 | La semilla aleatoria utilizada para crear el ruido. (predeterminado: 0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `image` | IMAGE | La imagen expandida de salida |

---
**Source fingerprint (SHA-256):** `15b21f1de8a98a6bcde131a61c01b062434c6a959bc563550d613972412973fe`
