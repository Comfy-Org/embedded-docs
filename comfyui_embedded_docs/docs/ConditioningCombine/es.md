> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningCombine/es.md)

Este nodo combina dos entradas de condicionamiento en una única salida, fusionando efectivamente su información. Las dos condiciones se combinan mediante concatenación de listas.

## Entradas

| Nombre del Parámetro | Tipo de Dato       | Descripción |
|----------------------|--------------------|-------------|
| `conditioning_1`     | `CONDITIONING`     | La primera entrada de condicionamiento que se va a combinar. Tiene la misma importancia que `conditioning_2` en el proceso de combinación. |
| `conditioning_2`     | `CONDITIONING`     | La segunda entrada de condicionamiento que se va a combinar. Tiene la misma importancia que `conditioning_1` en el proceso de combinación. |

## Salidas

| Nombre del Parámetro | Tipo de Dato       | Descripción |
|----------------------|--------------------|-------------|
| `conditioning`       | `CONDITIONING`     | El resultado de combinar `conditioning_1` y `conditioning_2`, que encapsula la información fusionada. |

## Escenarios de Uso

Compara los dos grupos a continuación: el lado izquierdo utiliza el nodo ConditioningCombine, mientras que el lado derecho muestra la salida normal.

![Comparar](./asset/compare.jpg)

En este ejemplo, las dos condiciones utilizadas en `Conditioning Combine` tienen importancia equivalente. Por lo tanto, puedes usar diferentes codificaciones de texto para el estilo de la imagen, las características del sujeto, etc., permitiendo que las características del prompt se generen de manera más completa. El segundo prompt utiliza el prompt completo combinado, pero la comprensión semántica puede codificar condiciones completamente diferentes.

Usando este nodo, puedes lograr:

- **Combinación básica de texto**: Conecta las salidas de dos nodos `CLIP Text Encode` a los dos puertos de entrada de `Conditioning Combine`
- **Combinación compleja de prompts**: Combina prompts positivos y negativos, o codifica por separado descripciones principales y descripciones de estilo antes de fusionarlas
- **Combinación en cadena condicional**: Se pueden usar múltiples nodos `Conditioning Combine` en serie para lograr la combinación gradual de múltiples condiciones