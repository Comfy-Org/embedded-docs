> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSimple/pt-BR.md)

O nó **ModelMergeSimple** foi projetado para mesclar dois modelos combinando seus parâmetros com base em uma proporção especificada. Esse nó facilita a criação de modelos híbridos que combinam os pontos fortes ou as características de ambos os modelos de entrada.

O parâmetro `ratio` determina a proporção da mesclagem entre os dois modelos. Quando esse valor é 1, o modelo de saída é 100% `model1` e, quando esse valor é 0, o modelo de saída é 100% `model2`.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|---------------|-----------|
| `model1`  | `MODEL`       | O primeiro modelo a ser mesclado. Ele serve como modelo base sobre o qual os patches do segundo modelo são aplicados. |
| `model2`  | `MODEL`       | O segundo modelo cujos patches são aplicados sobre o primeiro modelo, influenciados pela proporção especificada. |
| `ratio`   | `FLOAT`       | Quando esse valor é 1, o modelo de saída é 100% `model1` e, quando esse valor é 0, o modelo de saída é 100% `model2`. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|---------------|-----------|
| `model`   | MODEL         | O modelo mesclado resultante, incorporando elementos de ambos os modelos de entrada de acordo com a proporção especificada. |