
El nodo LatentRotate está diseñado para rotar representaciones latentes de imágenes por ángulos especificados. Abstrae la complejidad de manipular el espacio latente para lograr efectos de rotación, permitiendo a los usuarios transformar fácilmente imágenes en el espacio latente de un modelo generativo.

## Entradas

| Parámetro  | Data Type | Descripción |
|------------|-------------|-------------|
| `samples`  | `LATENT`    | El parámetro 'samples' representa las representaciones latentes de imágenes a rotar. Es crucial para determinar el punto de inicio de la operación de rotación. |
| `rotation` | COMBO[STRING] | El parámetro 'rotation' especifica el ángulo por el cual deben rotarse las imágenes latentes. Influye directamente en la orientación de las imágenes resultantes. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La salida es una versión modificada de las representaciones latentes de entrada, rotadas por el ángulo especificado. |
