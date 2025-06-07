
El nodo LatentCrop está diseñado para realizar operaciones de recorte en representaciones latentes de imágenes. Permite especificar las dimensiones y la posición del recorte, habilitando modificaciones específicas del espacio latente.

## Entradas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | El parámetro 'samples' representa las representaciones latentes a recortar. Es crucial para definir los datos sobre los que se realizará la operación de recorte. |
| `width`   | `INT`       | Especifica el ancho del área de recorte. Influye directamente en las dimensiones de la representación latente de salida. |
| `height`  | `INT`       | Especifica la altura del área de recorte, afectando el tamaño de la representación latente recortada resultante. |
| `x`       | `INT`       | Determina la coordenada x inicial del área de recorte, influyendo en la posición del recorte dentro de la representación latente original. |
| `y`       | `INT`       | Determina la coordenada y inicial del área de recorte, estableciendo la posición del recorte dentro de la representación latente original. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La salida es una representación latente modificada con el recorte especificado aplicado. |
