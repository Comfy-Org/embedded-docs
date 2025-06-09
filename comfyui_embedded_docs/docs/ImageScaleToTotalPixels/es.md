El nodo ImageScaleToTotalPixels está diseñado para redimensionar imágenes a un número total de píxeles especificado mientras se mantiene la relación de aspecto. Ofrece varios métodos para escalar la imagen y lograr el recuento de píxeles deseado.

## Entradas

| Parámetro       | Data Type | Descripción                                                                |
|-----------------|-------------|----------------------------------------------------------------------------|
| `image`         | `IMAGE`     | La imagen de entrada que se escalará al número total de píxeles especificado.    |
| `upscale_method`| COMBO[STRING] | El método utilizado para escalar la imagen. Afecta la calidad y las características de la imagen escalada. |
| `megapixels`    | `FLOAT`     | El tamaño objetivo de la imagen en megapíxeles. Esto determina el número total de píxeles en la imagen escalada. |

## Salidas

| Parámetro | Data Type | Descripción                                                           |
|-----------|-------------|-----------------------------------------------------------------------|
| `image`   | `IMAGE`     | La imagen escalada con el número total de píxeles especificado, manteniendo la relación de aspecto original. |
