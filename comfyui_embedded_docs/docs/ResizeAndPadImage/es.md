> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeAndPadImage/es.md)

El nodo ResizeAndPadImage redimensiona una imagen para que se ajuste a dimensiones específicas manteniendo su relación de aspecto original. Escala la imagen proporcionalmente para que quepa dentro del ancho y alto objetivo, luego añade relleno alrededor de los bordes para llenar cualquier espacio restante. El color del relleno y el método de interpolación se pueden personalizar para controlar la apariencia de las áreas con relleno y la calidad del redimensionamiento.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que se va a redimensionar y rellenar |
| `target_width` | INT | Sí | 1 a MAX_RESOLUTION | El ancho deseado para la imagen de salida (por defecto: 512) |
| `target_height` | INT | Sí | 1 a MAX_RESOLUTION | El alto deseado para la imagen de salida (por defecto: 512) |
| `padding_color` | COMBO | Sí | "white"<br>"black" | El color a utilizar para las áreas de relleno alrededor de la imagen redimensionada |
| `interpolation` | COMBO | Sí | "area"<br>"bicubic"<br>"nearest-exact"<br>"bilinear"<br>"lanczos" | El método de interpolación utilizado para redimensionar la imagen |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La imagen de salida redimensionada y con relleno |