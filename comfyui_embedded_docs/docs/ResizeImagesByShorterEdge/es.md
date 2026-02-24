> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByShorterEdge/es.md)

Este nodo redimensiona imágenes ajustando sus dimensiones para que la longitud del lado más corto coincida con un valor objetivo especificado. Calcula nuevas dimensiones manteniendo la relación de aspecto original de la imagen. Devuelve la imagen redimensionada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que se va a redimensionar. |
| `shorter_edge` | INT | No | 1 a 8192 | Longitud objetivo para el lado más corto. (por defecto: 512) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La imagen redimensionada. |
