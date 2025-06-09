El nodo ImageSharpen mejora la claridad de una imagen acentuando sus bordes y detalles. Aplica un filtro de afilado a la imagen, que se puede ajustar en intensidad y radio, haciendo que la imagen parezca más definida y nítida.

## Entradas

| Campo          | Data Type | Descripción                                                                                   |
|----------------|-------------|-----------------------------------------------------------------------------------------------|
| `image`        | `IMAGE`     | La imagen de entrada a afilar. Este parámetro es crucial ya que determina la imagen base sobre la cual se aplicará el efecto de afilado. |
| `sharpen_radius`| `INT`       | Define el radio del efecto de afilado. Un radio mayor significa que más píxeles alrededor del borde serán afectados, llevando a un efecto de afilado más pronunciado. |
| `sigma`        | `FLOAT`     | Controla la extensión del efecto de afilado. Un valor de sigma más alto resulta en una transición más suave en los bordes, mientras que un sigma más bajo hace que el afilado sea más localizado. |
| `alpha`        | `FLOAT`     | Ajusta la intensidad del efecto de afilado. Valores de alpha más altos resultan en un efecto de afilado más fuerte. |

## Salidas

| Campo | Data Type | Descripción                                                              |
|-------|-------------|--------------------------------------------------------------------------|
| `image`| `IMAGE`     | La imagen afilada, con bordes y detalles mejorados, lista para un procesamiento o visualización adicional. |
