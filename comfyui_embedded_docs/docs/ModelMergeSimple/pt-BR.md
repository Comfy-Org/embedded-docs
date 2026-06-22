# ModelMergeSimple

O nó **ModelMergeSimple** foi projetado para mesclar dois modelos combinando seus parâmetros com base em uma proporção especificada. Esse nó facilita a criação de modelos híbridos que combinam os pontos fortes ou as características de ambos os modelos de entrada.

O parâmetro `ratio` determina a proporção da mesclagem entre os dois modelos. Quando esse valor é 1, o modelo de saída é 100% `model1` e, quando esse valor é 0, o modelo de saída é 100% `model2`.

## Entradas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model1` | O primeiro modelo a ser mesclado. Ele serve como modelo base sobre o qual os patches do segundo modelo são aplicados. | `MODEL` |
| `model2` | O segundo modelo cujos patches são aplicados sobre o primeiro modelo, influenciados pela proporção especificada. | `MODEL` |
| `proporção` | Quando esse valor é 1, o modelo de saída é 100% `model1` e, quando esse valor é 0, o modelo de saída é 100% `model2`. | `FLOAT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo mesclado resultante, incorporando elementos de ambos os modelos de entrada de acordo com a proporção especificada. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSimple/pt-BR.md)
