> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByLongerEdge/es.md)

El nodo **Redimensionar imágenes por el borde más largo** redimensiona una o más imágenes de modo que su lado más largo coincida con una longitud objetivo especificada. Determina automáticamente si el ancho o el alto es mayor y escala la otra dimensión de forma proporcional para conservar la relación de aspecto original. Esto es útil para estandarizar tamaños de imagen según su dimensión más grande.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen o lote de imágenes de entrada que se redimensionarán. |
| `borde_más_largo` | INT | Sí | 1 - 8192 | Longitud objetivo para el borde más largo. El borde más corto se escalará proporcionalmente. (valor predeterminado: 1024) |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `image` | IMAGE | La imagen o lote de imágenes redimensionadas. La salida tendrá la misma cantidad de imágenes que la entrada, y el borde más largo de cada una coincidirá con la longitud especificada en `borde_más_largo`. |

---
**Source fingerprint (SHA-256):** `687d5f159967eccbf64f0ec529ae6edeb94f4707ae10a3c75a5d0b08c86dd828`
