> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVPreprocess/es.md)

El nodo LTXVPreprocess aplica preprocesamiento de compresión a imágenes. Toma imágenes de entrada y las procesa con un nivel de compresión específico, generando como salida las imágenes procesadas con los ajustes de compresión aplicados.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que será procesada |
| `img_compression` | INT | No | 0-100 | Cantidad de compresión a aplicar sobre la imagen (por defecto: 35) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output_image` | IMAGE | La imagen de salida procesada con la compresión aplicada |