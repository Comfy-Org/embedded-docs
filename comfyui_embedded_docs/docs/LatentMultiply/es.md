
El nodo LatentMultiply está diseñado para escalar la representación latente de muestras mediante un multiplicador especificado. Esta operación permite ajustar la intensidad o magnitud de las características dentro del espacio latente, habilitando el ajuste fino del contenido generado o la exploración de variaciones dentro de una dirección latente dada.

## Entradas

| Parámetro    | Data Type | Descripción |
|--------------|-------------|-------------|
| `samples`    | `LATENT`    | El parámetro 'samples' representa las representaciones latentes a escalar. Es crucial para definir los datos de entrada sobre los cuales se realizará la operación de multiplicación. |
| `multiplier` | `FLOAT`     | El parámetro 'multiplier' especifica el factor de escala que se aplicará a las muestras latentes. Juega un papel clave en el ajuste de la magnitud de las características latentes, permitiendo un control matizado sobre la salida generada. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La salida es una versión modificada de las muestras latentes de entrada, escaladas por el multiplicador especificado. Esto permite la exploración de variaciones dentro del espacio latente ajustando la intensidad de sus características. |
