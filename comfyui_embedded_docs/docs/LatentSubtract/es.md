> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentSubtract/es.md)

El nodo LatentSubtract está diseñado para restar una representación latente de otra. Esta operación puede utilizarse para manipular o modificar las características de las salidas de modelos generativos, eliminando eficazmente rasgos o atributos representados en un espacio latente de otro.

## Entradas

| Parámetro    | Tipo de Dato | Descripción |
|--------------|-------------|-------------|
| `muestras1`   | `LATENT`    | El primer conjunto de muestras latentes del cual se restará. Sirve como base para la operación de resta. |
| `muestras2`   | `LATENT`    | El segundo conjunto de muestras latentes que se restará del primer conjunto. Esta operación puede alterar la salida del modelo generativo resultante al eliminar atributos o rasgos. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | El resultado de restar el segundo conjunto de muestras latentes del primero. Esta representación latente modificada puede utilizarse para tareas generativas posteriores. |