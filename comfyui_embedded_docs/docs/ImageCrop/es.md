El nodo `ImageCrop` está diseñado para recortar imágenes a un ancho y alto especificados comenzando desde una coordenada x e y dada. Esta funcionalidad es esencial para enfocar regiones específicas de una imagen o para ajustar el tamaño de la imagen para cumplir con ciertos requisitos.

## Entradas

| Campo | Data Type | Descripción                                                                                   |
|-------|-------------|-----------------------------------------------------------------------------------------------|
| `image` | `IMAGE` | La imagen de entrada a recortar. Este parámetro es crucial ya que define la imagen fuente de la cual se extraerá una región basada en las dimensiones y coordenadas especificadas. |
| `width` | `INT` | Especifica el ancho de la imagen recortada. Este parámetro determina cuán ancha será la imagen recortada resultante. |
| `height` | `INT` | Especifica la altura de la imagen recortada. Este parámetro determina la altura de la imagen recortada resultante. |
| `x` | `INT` | La coordenada x de la esquina superior izquierda del área de recorte. Este parámetro establece el punto de inicio para la dimensión de ancho del recorte. |
| `y` | `INT` | La coordenada y de la esquina superior izquierda del área de recorte. Este parámetro establece el punto de inicio para la dimensión de altura del recorte. |

## Salidas

| Campo | Data Type | Descripción                                                                   |
|-------|-------------|-------------------------------------------------------------------------------|
| `image` | `IMAGE` | La imagen recortada como resultado de la operación de recorte. Esta salida es significativa para un procesamiento o análisis adicional de la región de imagen especificada. |
