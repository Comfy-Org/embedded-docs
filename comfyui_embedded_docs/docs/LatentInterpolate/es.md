
El nodo LatentInterpolate está diseñado para realizar la interpolación entre dos conjuntos de muestras latentes basándose en una proporción especificada, combinando las características de ambos conjuntos para producir un nuevo conjunto intermedio de muestras latentes.

## Entradas

| Parámetro    | Data Type | Descripción |
|--------------|-------------|-------------|
| `samples1`   | `LATENT`    | El primer conjunto de muestras latentes a interpolar. Sirve como punto de inicio para el proceso de interpolación. |
| `samples2`   | `LATENT`    | El segundo conjunto de muestras latentes a interpolar. Sirve como punto final para el proceso de interpolación. |
| `ratio`      | `FLOAT`     | Un valor de punto flotante que determina el peso de cada conjunto de muestras en la salida interpolada. Un ratio de 0 produce una copia del primer conjunto, mientras que un ratio de 1 produce una copia del segundo conjunto. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La salida es un nuevo conjunto de muestras latentes que representa un estado interpolado entre los dos conjuntos de entrada, basado en la proporción especificada. |
