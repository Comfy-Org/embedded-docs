
El nodo LatentCompositeMasked está diseñado para mezclar dos representaciones latentes en coordenadas especificadas, utilizando opcionalmente una máscara para una composición más controlada. Este nodo permite la creación de imágenes latentes complejas al superponer partes de una imagen sobre otra, con la capacidad de redimensionar la imagen fuente para un ajuste perfecto.

## Entradas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `destination` | `LATENT`    | La representación latente sobre la cual se compondrá otra representación latente. Actúa como la capa base para la operación de composición. |
| `source` | `LATENT`    | La representación latente que se compondrá sobre el destino. Esta capa fuente puede ser redimensionada y posicionada según los parámetros especificados. |
| `x` | `INT`       | La coordenada x en la representación latente de destino donde se colocará la fuente. Permite un posicionamiento preciso de la capa fuente. |
| `y` | `INT`       | La coordenada y en la representación latente de destino donde se colocará la fuente, permitiendo un posicionamiento preciso de la superposición. |
| `resize_source` | `BOOLEAN` | Un indicador booleano que indica si la representación latente de la fuente debe ser redimensionada para coincidir con las dimensiones del destino antes de la composición. |
| `mask` | `MASK`     | Una máscara opcional que se puede usar para controlar la mezcla de la fuente sobre el destino. La máscara define qué partes de la fuente serán visibles en la composición final. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La representación latente resultante después de componer la fuente sobre el destino, utilizando potencialmente una máscara para una mezcla selectiva. |
