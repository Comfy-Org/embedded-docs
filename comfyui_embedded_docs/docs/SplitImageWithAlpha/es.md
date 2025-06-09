
El nodo SplitImageWithAlpha está diseñado para separar los componentes de color y alfa de una imagen. Procesa un tensor de imagen de entrada, extrayendo los canales RGB como el componente de color y el canal alfa como el componente de transparencia, facilitando operaciones que requieren la manipulación de estos aspectos distintos de la imagen.

## Entradas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | El parámetro 'image' representa el tensor de imagen de entrada del cual se deben separar los canales RGB y alfa. Es crucial para la operación ya que proporciona los datos fuente para la separación. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | La salida 'image' representa los canales RGB separados de la imagen de entrada, proporcionando el componente de color sin la información de transparencia. |
| `mask`    | `MASK`      | La salida 'mask' representa el canal alfa separado de la imagen de entrada, proporcionando la información de transparencia. |
