> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageSharpen/es.md)

El nodo ImageSharpen mejora la nitidez de una imagen acentuando sus bordes y detalles. Aplica un filtro de enfoque a la imagen, cuya intensidad y radio pueden ajustarse, haciendo que la imagen parezca más definida y nítida.

## Entradas

| Campo           | Tipo de Dato | Descripción                                                                                   |
|----------------|-------------|-----------------------------------------------------------------------------------------------|
| `image`        | `IMAGE`     | La imagen de entrada que se va a enfocar. Este parámetro es fundamental, ya que determina la imagen base sobre la cual se aplicará el efecto de enfoque. |
| `sharpen_radius`| `INT`       | Define el radio del efecto de enfoque. Un radio mayor significa que más píxeles alrededor del borde se verán afectados, lo que genera un efecto de enfoque más pronunciado. |
| `sigma`        | `FLOAT`     | Controla la dispersión del efecto de enfoque. Un valor de sigma más alto produce una transición más suave en los bordes, mientras que un valor más bajo hace que el enfoque sea más localizado. |
| `alpha`        | `FLOAT`     | Ajusta la intensidad del efecto de enfoque. Los valores de alfa más altos producen un efecto de enfoque más fuerte. |

## Salidas

| Campo  | Tipo de Dato | Descripción                                                              |
|--------|-------------|--------------------------------------------------------------------------|
| `image`| `IMAGE`     | La imagen enfocada, con bordes y detalles mejorados, lista para su posterior procesamiento o visualización. |