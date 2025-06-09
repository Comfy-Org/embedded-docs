
Este nodo se especializa en combinar dos entradas de máscara a través de una variedad de operaciones como adición, sustracción y operaciones lógicas, para producir una nueva máscara modificada. Maneja abstractamente la manipulación de datos de máscara para lograr efectos de enmascaramiento complejos, sirviendo como un componente crucial en flujos de trabajo de edición y procesamiento de imágenes basados en máscaras.

## Entradas

| Parámetro    | Data Type | Descripción                                                                                                                                      |
| ------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `destination`| MASK        | La máscara principal que se modificará en función de la operación con la máscara fuente. Juega un papel central en la operación de composición, actuando como base para las modificaciones. |
| `source`     | MASK        | La máscara secundaria que se utilizará junto con la máscara de destino para realizar la operación especificada, influyendo en la máscara de salida final. |
| `x`          | INT         | El desplazamiento horizontal en el que se aplicará la máscara fuente a la máscara de destino, afectando la posición del resultado compuesto.       |
| `y`          | INT         | El desplazamiento vertical en el que se aplicará la máscara fuente a la máscara de destino, afectando la posición del resultado compuesto.         |
| `operation`  | COMBO[STRING]| Especifica el tipo de operación a aplicar entre las máscaras de destino y fuente, como 'add', 'subtract', u operaciones lógicas, determinando la naturaleza del efecto compuesto. |

## Salidas

| Parámetro | Data Type | Descripción                                                                 |
| --------- | ------------ | ---------------------------------------------------------------------------- |
| `mask`    | MASK        | La máscara resultante después de aplicar la operación especificada entre las máscaras de destino y fuente, representando el resultado compuesto. |
