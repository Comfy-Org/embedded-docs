> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAdd/pt-BR.md)

O nó ModelMergeAdd é projetado para mesclar dois modelos adicionando patches-chave de um modelo a outro. Este processo envolve clonar o primeiro modelo e, em seguida, aplicar patches do segundo modelo, permitindo a combinação de características ou comportamentos de ambos os modelos.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `model1`  | `MODEL`     | O primeiro modelo a ser clonado e ao qual os patches do segundo modelo serão adicionados. Serve como o modelo base para o processo de mesclagem. |
| `model2`  | `MODEL`     | O segundo modelo do qual os patches-chave são extraídos e adicionados ao primeiro modelo. Contribui com características ou comportamentos adicionais para o modelo mesclado. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `model`   | MODEL     | O resultado da mesclagem de dois modelos pela adição de patches-chave do segundo modelo ao primeiro. Este modelo mesclado combina características ou comportamentos de ambos os modelos. |
