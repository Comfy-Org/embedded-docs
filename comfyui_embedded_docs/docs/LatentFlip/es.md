
El nodo LatentFlip está diseñado para manipular representaciones latentes volteándolas vertical u horizontalmente. Esta operación permite la transformación del espacio latente, potencialmente descubriendo nuevas variaciones o perspectivas dentro de los datos.

## Entradas

| Parámetro     | Data Type | Descripción |
|---------------|--------------|-------------|
| `samples`     | `LATENT`     | El parámetro 'samples' representa las representaciones latentes a voltear. La operación de volteo altera estas representaciones, ya sea vertical u horizontalmente, dependiendo del parámetro 'flip_method', transformando así los datos en el espacio latente. |
| `flip_method` | COMBO[STRING] | El parámetro 'flip_method' especifica el eje a lo largo del cual se voltearán las muestras latentes. Puede ser 'x-axis: vertically' o 'y-axis: horizontally', determinando la dirección del volteo y, por lo tanto, la naturaleza de la transformación aplicada a las representaciones latentes. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La salida es una versión modificada de las representaciones latentes de entrada, habiendo sido volteadas según el método especificado. Esta transformación puede introducir nuevas variaciones dentro del espacio latente. |
