> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSubtract/pt-BR.md)

Este nó foi projetado para operações avançadas de fusão de modelos, especificamente para subtrair os parâmetros de um modelo de outro com base em um multiplicador especificado. Ele permite a personalização dos comportamentos do modelo ao ajustar a influência dos parâmetros de um modelo sobre outro, facilitando a criação de novos modelos híbridos.

## Entradas

| Parâmetro     | Tipo de Dados | Descrição |
|---------------|--------------|-------------|
| `model1`      | `MODEL`     | O modelo base do qual os parâmetros serão subtraídos. |
| `model2`      | `MODEL`     | O modelo cujos parâmetros serão subtraídos do modelo base. |
| `multiplier`  | `FLOAT`     | Um valor de ponto flutuante que escala o efeito da subtração nos parâmetros do modelo base. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `model`   | MODEL     | O modelo resultante após subtrair os parâmetros de um modelo de outro, escalonados pelo multiplicador. |
