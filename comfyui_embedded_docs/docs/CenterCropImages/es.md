> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CenterCropImages/es.md)

El nodo Recortar Imágenes desde el Centro recorta una imagen desde su centro a un ancho y alto especificados. Calcula la región central de la imagen de entrada y extrae un área rectangular de las dimensiones definidas. Si el tamaño de recorte solicitado es mayor que la imagen, el recorte se limitará a los bordes de la imagen.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que se va a recortar. |
| `width` | INT | No | 1 a 8192 | El ancho del área de recorte (valor por defecto: 512). |
| `height` | INT | No | 1 a 8192 | La altura del área de recorte (valor por defecto: 512). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La imagen resultante después de la operación de recorte central. |
