> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAdd/pt-BR.md)

O nó **ModelMergeAdd** foi projetado para mesclar dois modelos, adicionando patches-chave de um modelo a outro. Esse processo envolve clonar o primeiro modelo e, em seguida, aplicar patches do segundo modelo, permitindo a combinação de características ou comportamentos de ambos os modelos.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|---------------|-----------|
| `modelo1`  | `MODEL`       | O primeiro modelo a ser clonado e ao qual os patches do segundo modelo serão adicionados. Ele serve como modelo base para o processo de mesclagem. |
| `modelo2`  | `MODEL`       | O segundo modelo do qual os patches-chave são extraídos e adicionados ao primeiro modelo. Ele contribui com características ou comportamentos adicionais para o modelo mesclado. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|---------------|-----------|
| `model`   | MODEL         | O resultado da mesclagem de dois modelos, adicionando patches-chave do segundo modelo ao primeiro. Este modelo mesclado combina características ou comportamentos de ambos os modelos. |