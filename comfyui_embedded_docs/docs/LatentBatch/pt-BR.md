# LatentBatch

O nó **LatentBatch** é projetado para mesclar dois conjuntos de amostras latentes em um único lote, redimensionando potencialmente um conjunto para corresponder às dimensões do outro antes da concatenação. Essa operação facilita a combinação de diferentes representações latentes para tarefas de processamento ou geração posteriores.

## Entradas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `amostras1` | O primeiro conjunto de amostras latentes a ser mesclado. Ele desempenha um papel crucial na determinação da forma final do lote mesclado. | `LATENT` |
| `amostras2` | O segundo conjunto de amostras latentes a ser mesclado. Se suas dimensões diferirem do primeiro conjunto, ele é redimensionado para garantir compatibilidade antes da mesclagem. | `LATENT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `latent` | O conjunto mesclado de amostras latentes, agora combinado em um único lote para processamento posterior. | `LATENT` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBatch/pt-BR.md)
