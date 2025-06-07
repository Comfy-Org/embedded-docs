El nodo ImageScaleBy está diseñado para escalar imágenes por un factor de escala especificado utilizando varios métodos de interpolación. Permite ajustar el tamaño de la imagen de manera flexible, adaptándose a diferentes necesidades de escalado.

## Entradas

| Parámetro       | Data Type | Descripción                                                                 |
|-----------------|-------------|----------------------------------------------------------------------------|
| `image`         | `IMAGE`     | La imagen de entrada a escalar. Este parámetro es crucial ya que proporciona la imagen base que se someterá al proceso de escalado. |
| `upscale_method`| COMBO[STRING] | Especifica el método de interpolación que se utilizará para escalar. La elección del método puede afectar la calidad y las características de la imagen escalada. |
| `scale_by`      | `FLOAT`     | El factor por el cual se escalará la imagen. Esto determina el aumento en el tamaño de la imagen de salida en relación con la imagen de entrada. |

## Salidas

| Parámetro | Data Type | Descripción                                                   |
|-----------|-------------|---------------------------------------------------------------|
| `image`   | `IMAGE`     | La imagen escalada, que es más grande que la imagen de entrada según el factor de escala y el método de interpolación especificados. |
