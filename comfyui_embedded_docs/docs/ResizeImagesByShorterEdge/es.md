> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByShorterEdge/es.md)

Este nodo redimensiona imágenes para que el borde más corto coincida con una longitud específica, manteniendo la relación de aspecto original. Calcula las nuevas dimensiones basándose en la longitud objetivo para el lado más corto y devuelve la imagen redimensionada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que se va a redimensionar. |
| `borde_más_corto` | INT | No | 1 a 8192 | Longitud objetivo para el borde más corto. (predeterminado: 512) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `image` | IMAGE | La imagen redimensionada con el borde más corto coincidiendo con la longitud objetivo especificada. |

---
**Source fingerprint (SHA-256):** `011949390faa9032587aec210d9e38d55b79e474c7a6dcd5d3c0e75594a1fc29`
