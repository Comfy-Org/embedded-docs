# Latent de Lote

Este nó foi projetado para extrair um subconjunto específico de amostras latentes de um lote fornecido, com base no índice e comprimento do lote especificados. Ele permite o processamento seletivo de amostras latentes, facilitando operações em segmentos menores do lote para maior eficiência ou manipulação direcionada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `amostras` | A coleção de amostras latentes da qual um subconjunto será extraído. Este parâmetro é essencial para determinar o lote de origem das amostras a serem processadas. | `LATENT` |
| `índice_do_lote` | Especifica o índice inicial dentro do lote a partir do qual o subconjunto de amostras começará. Este parâmetro permite a extração direcionada de amostras de posições específicas no lote. | `INT` |
| `comprimento` | Define o número de amostras a serem extraídas a partir do índice inicial especificado. Este parâmetro controla o tamanho do subconjunto a ser processado, permitindo manipulação flexível de segmentos do lote. | `INT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `latent` | O subconjunto extraído de amostras latentes, agora disponível para processamento ou análise adicional. | `LATENT` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentFromBatch/pt-BR.md)
