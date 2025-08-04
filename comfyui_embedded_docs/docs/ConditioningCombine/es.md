Este nodo combina dos entradas de condicionamiento en una sola salida, fusionando efectivamente su información. Las dos condiciones se combinan mediante concatenación de listas.

## Entradas

| Nombre del Parámetro | Tipo de Datos      | Descripción |
|----------------------|--------------------|-------------|
| `acondicionamiento_1` | `CONDITIONING`     | La primera entrada de condicionamiento a combinar. Tiene igual importancia que `acondicionamiento_2` en el proceso de combinación. |
| `acondicionamiento_2` | `CONDITIONING`     | La segunda entrada de condicionamiento a combinar. Tiene igual importancia que `acondicionamiento_1` en el proceso de combinación. |

## Salidas

| Nombre del Parámetro | Tipo de Datos      | Descripción |
|----------------------|--------------------|-------------|
| `acondicionamiento`   | `CONDITIONING`     | El resultado de combinar `acondicionamiento_1` y `acondicionamiento_2`, encapsulando la información fusionada. |

## Escenarios de Uso

Compara los dos grupos a continuación: el lado izquierdo usa el nodo ConditioningCombine, mientras que el lado derecho muestra la salida normal.

![Compare](./asset/compare.jpg)

En este ejemplo, las dos condiciones utilizadas en `Acondicionamiento (Combinar)` tienen importancia equivalente. Por lo tanto, puedes usar diferentes codificaciones de texto para el estilo de imagen, características del sujeto, etc., permitiendo que las características del prompt se generen de manera más completa. El segundo prompt usa el prompt completo combinado, pero la comprensión semántica puede codificar condiciones completamente diferentes.

Usando este nodo, puedes lograr:
- Fusión básica de texto: Conecta las salidas de dos nodos de `Codificación de Texto CLIP` a los dos puertos de entrada de `Acondicionamiento (Combinar)`
- Combinación compleja de prompts: Combina prompts positivos y negativos, o codifica por separado las descripciones principales y las descripciones de estilo antes de fusionarlas
- Combinación en cadena condicional: Múltiples nodos de `Acondicionamiento (Combinar)` pueden usarse en serie para lograr la combinación gradual de múltiples condiciones
