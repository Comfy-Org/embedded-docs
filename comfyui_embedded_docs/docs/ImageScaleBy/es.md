> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleBy/es.md)

El nodo ImageScaleBy está diseñado para escalar imágenes mediante un factor de escala específico utilizando diversos métodos de interpolación. Permite ajustar el tamaño de la imagen de manera flexible, adaptándose a diferentes necesidades de escalado.

## Entradas

| Parámetro       | Tipo de Dato | Descripción                                                                 |
|-----------------|--------------|-----------------------------------------------------------------------------|
| `image`         | `IMAGE`      | La imagen de entrada que se va a escalar. Este parámetro es fundamental, ya que proporciona la imagen base que se someterá al proceso de escalado. |
| `upscale_method`| COMBO[STRING]| Especifica el método de interpolación que se utilizará para el escalado. La elección del método puede afectar la calidad y las características de la imagen escalada. |
| `scale_by`      | `FLOAT`      | El factor por el cual se escalará la imagen. Esto determina el aumento de tamaño de la imagen de salida en relación con la imagen de entrada. |

## Salidas

| Parámetro | Tipo de Dato | Descripción                                                   |
|-----------|--------------|---------------------------------------------------------------|
| `image`   | `IMAGE`      | La imagen escalada, que es más grande que la imagen de entrada según el factor de escala y el método de interpolación especificados. |