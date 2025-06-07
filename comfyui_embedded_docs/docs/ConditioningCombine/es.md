Este nodo combina dos entradas de condicionamiento en una sola salida, fusionando efectivamente su información.

## Entradas

| Parámetro            | Comfy dtype        | Descripción |
|----------------------|--------------------|-------------|
| `conditioning_1`      | `CONDITIONING`     | La primera entrada de condicionamiento a combinar. Juega un papel igual al de conditioning_2 en el proceso de combinación. |
| `conditioning_2`      | `CONDITIONING`     | La segunda entrada de condicionamiento a combinar. Es igualmente importante que conditioning_1 en el proceso de fusión. |

## Salidas

| Parámetro            | Comfy dtype        | Descripción |
|----------------------|--------------------|-------------|
| `conditioning`        | `CONDITIONING`     | El resultado de combinar conditioning_1 y conditioning_2, encapsulando la información fusionada. |
