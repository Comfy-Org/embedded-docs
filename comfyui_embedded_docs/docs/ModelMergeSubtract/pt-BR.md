Este nó foi projetado para operações avançadas de mesclagem de modelos, especificamente para subtrair os parâmetros de um modelo de outro com base em um multiplicador especificado. Ele permite a personalização dos comportamentos do modelo ajustando a influência dos parâmetros de um modelo sobre outro, facilitando a criação de novos modelos híbridos.

## Entradas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model1` | O modelo base do qual os parâmetros serão subtraídos. | `MODEL` |
| `model2` | O modelo cujos parâmetros serão subtraídos do modelo base. | `MODEL` |
| `multiplicador` | Um valor de ponto flutuante que escala o efeito da subtração nos parâmetros do modelo base. | `FLOAT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo resultante após subtrair os parâmetros de um modelo de outro, escalados pelo multiplicador. | `MODEL` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSubtract/pt-BR.md)
