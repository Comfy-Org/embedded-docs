El nodo `ImageBlur` aplica un desenfoque gaussiano a una imagen, permitiendo suavizar los bordes y reducir los detalles y el ruido. Proporciona control sobre la intensidad y el alcance del desenfoque a través de parámetros.

## Entradas

| Campo          | Data Type | Descripción                                                                   |
|----------------|-------------|-------------------------------------------------------------------------------|
| `image`        | `IMAGE`     | La imagen de entrada a desenfocar. Este es el objetivo principal del efecto de desenfoque. |
| `blur_radius`  | `INT`       | Determina el radio del efecto de desenfoque. Un radio mayor resulta en un desenfoque más pronunciado. |
| `sigma`        | `FLOAT`     | Controla el alcance del desenfoque. Un valor de sigma más alto significa que el desenfoque afectará a un área más amplia alrededor de cada píxel. |

## Salidas

| Campo | Data Type | Descripción                                                              |
|-------|-------------|--------------------------------------------------------------------------|
| `image`| `IMAGE`     | La salida es la versión desenfocada de la imagen de entrada, con el grado de desenfoque determinado por los parámetros de entrada. |
