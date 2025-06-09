El nodo LatentAdd está diseñado para la suma de dos representaciones latentes. Facilita la combinación de características o propiedades codificadas en estas representaciones mediante la suma elemento a elemento.

## Entradas

| Parámetro    | Data Type | Descripción |
|--------------|-------------|-------------|
| `samples1`   | `LATENT`    | El primer conjunto de muestras latentes a sumar. Representa una de las entradas cuyas características se combinarán con otro conjunto de muestras latentes. |
| `samples2`   | `LATENT`    | El segundo conjunto de muestras latentes a sumar. Sirve como la otra entrada cuyas características se combinan con el primer conjunto de muestras latentes mediante la suma elemento a elemento. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | El resultado de la suma elemento a elemento de dos muestras latentes, representando un nuevo conjunto de muestras latentes que combina las características de ambas entradas. |
