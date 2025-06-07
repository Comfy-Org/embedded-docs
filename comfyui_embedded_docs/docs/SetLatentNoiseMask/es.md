
Este nodo está diseñado para aplicar una máscara de ruido a un conjunto de muestras latentes. Modifica las muestras de entrada integrando una máscara especificada, alterando así sus características de ruido.

## Entradas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | Las muestras latentes a las que se aplicará la máscara de ruido. Este parámetro es crucial para determinar el contenido base que será modificado. |
| `mask`    | `MASK`      | La máscara que se aplicará a las muestras latentes. Define las áreas e intensidad de la alteración de ruido dentro de las muestras. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Las muestras latentes modificadas con la máscara de ruido aplicada. |
