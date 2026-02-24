> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByLongerEdge/es.md)

El nodo Redimensionar Imágenes por Borde Más Largo redimensiona una o más imágenes para que su lado más largo coincida con una longitud objetivo especificada. Determina automáticamente si el ancho o el alto es más largo y escala la otra dimensión proporcionalmente para preservar la relación de aspecto original. Esto es útil para estandarizar tamaños de imagen basándose en su dimensión más grande.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada o lote de imágenes a redimensionar. |
| `longer_edge` | INT | No | 1 - 8192 | Longitud objetivo para el borde más largo. El borde más corto se escalará proporcionalmente. (por defecto: 1024) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La imagen o lote de imágenes redimensionadas. La salida tendrá el mismo número de imágenes que la entrada, con el borde más largo de cada una coincidiendo con la longitud `longer_edge` especificada. |
