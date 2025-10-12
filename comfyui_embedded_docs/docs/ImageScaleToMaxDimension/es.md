> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToMaxDimension/es.md)

El nodo ImageScaleToMaxDimension redimensiona imágenes para que se ajusten a una dimensión máxima especificada manteniendo la relación de aspecto original. Calcula si la imagen está orientada en vertical u horizontal, luego escala la dimensión más grande para que coincida con el tamaño objetivo mientras ajusta proporcionalmente la dimensión más pequeña. El nodo admite múltiples métodos de escalado para diferentes requisitos de calidad y rendimiento.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que se va a escalar |
| `upscale_method` | STRING | Sí | "area"<br>"lanczos"<br>"bilinear"<br>"nearest-exact"<br>"bicubic" | El método de interpolación utilizado para escalar la imagen |
| `largest_size` | INT | Sí | 0 a 16384 | La dimensión máxima para la imagen escalada (predeterminado: 512) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La imagen escalada con la dimensión más grande coincidiendo con el tamaño especificado |
