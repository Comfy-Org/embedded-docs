
El nodo Fusión de Modelos por Suma está diseñado para fusionar dos modelos añadiendo parches clave de un modelo a otro. Este proceso implica clonar el primer modelo y luego aplicar parches del segundo modelo, permitiendo la combinación de características o comportamientos de ambos modelos.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `model1`  | `MODEL`     | El primer modelo que se clonará y al que se añadirán los parches del segundo modelo. Sirve como el modelo base para el proceso de fusión. |
| `model2`  | `MODEL`     | El segundo modelo del cual se extraen los parches clave y se añaden al primer modelo. Contribuye con características o comportamientos adicionales al modelo fusionado. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `model`   | MODEL     | El resultado de fusionar dos modelos añadiendo parches clave del segundo modelo al primero. Este modelo fusionado combina características o comportamientos de ambos modelos. |
