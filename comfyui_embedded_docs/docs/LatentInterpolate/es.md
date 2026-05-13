> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentInterpolate/es.md)

El nodo LatentInterpolate está diseñado para realizar interpolación entre dos conjuntos de muestras latentes basándose en una proporción especificada, combinando las características de ambos conjuntos para producir un nuevo conjunto intermedio de muestras latentes.

## Entradas

| Parámetro    | Tipo de Dato | Descripción |
|--------------|-------------|-------------|
| `muestras1`   | `LATENT`    | El primer conjunto de muestras latentes a interpolar. Sirve como punto de partida para el proceso de interpolación. |
| `muestras2`   | `LATENT`    | El segundo conjunto de muestras latentes a interpolar. Sirve como punto final para el proceso de interpolación. |
| `proporción`      | `FLOAT`     | Un valor de punto flotante que determina el peso de cada conjunto de muestras en la salida interpolada. Una proporción de 0 produce una copia del primer conjunto, mientras que una proporción de 1 produce una copia del segundo conjunto. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La salida es un nuevo conjunto de muestras latentes que representan un estado interpolado entre los dos conjuntos de entrada, basado en la proporción especificada. |