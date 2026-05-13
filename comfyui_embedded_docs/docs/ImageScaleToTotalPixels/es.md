> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToTotalPixels/es.md)

El nodo ImageScaleToTotalPixels está diseñado para redimensionar imágenes a un número total de píxeles especificado, manteniendo la relación de aspecto. Proporciona varios métodos para escalar la imagen y alcanzar la cantidad de píxeles deseada.

## Entradas

| Parámetro       | Tipo de Dato | Descripción                                                                |
|-----------------|--------------|----------------------------------------------------------------------------|
| `image`         | `IMAGE`      | La imagen de entrada que se escalará al número total de píxeles especificado. |
| `upscale_method`| COMBO[STRING] | El método utilizado para escalar la imagen. Afecta la calidad y las características de la imagen escalada. |
| `megapixels`    | `FLOAT`      | El tamaño objetivo de la imagen en megapíxeles. Esto determina el número total de píxeles en la imagen escalada. |

## Salidas

| Parámetro | Tipo de Dato | Descripción                                                           |
|-----------|--------------|-----------------------------------------------------------------------|
| `image`   | `IMAGE`      | La imagen escalada con el número total de píxeles especificado, manteniendo la relación de aspecto original. |