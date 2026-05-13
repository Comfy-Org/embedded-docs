> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCrop/es.md)

El nodo `ImageCrop` está diseñado para recortar imágenes a un ancho y alto específicos, comenzando desde una coordenada x e y determinada. Esta funcionalidad es esencial para enfocarse en regiones específicas de una imagen o para ajustar el tamaño de la imagen a ciertos requisitos.

## Entradas

| Campo | Tipo de Dato | Descripción                                                                                   |
|-------|-------------|-----------------------------------------------------------------------------------------------|
| `image` | `IMAGE` | La imagen de entrada que se va a recortar. Este parámetro es crucial, ya que define la imagen fuente de la cual se extraerá una región según las dimensiones y coordenadas especificadas. |
| `width` | `INT` | Especifica el ancho de la imagen recortada. Este parámetro determina qué tan ancha será la imagen recortada resultante. |
| `height` | `INT` | Especifica el alto de la imagen recortada. Este parámetro determina la altura de la imagen recortada resultante. |
| `x` | `INT` | La coordenada x de la esquina superior izquierda del área de recorte. Este parámetro establece el punto de inicio para la dimensión de ancho del recorte. |
| `y` | `INT` | La coordenada y de la esquina superior izquierda del área de recorte. Este parámetro establece el punto de inicio para la dimensión de alto del recorte. |

## Salidas

| Campo | Tipo de Dato | Descripción                                                                   |
|-------|-------------|-------------------------------------------------------------------------------|
| `image` | `IMAGE` | La imagen recortada como resultado de la operación de recorte. Esta salida es importante para el procesamiento o análisis posterior de la región de imagen especificada. |