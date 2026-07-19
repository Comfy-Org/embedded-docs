# Repetir Lote Latent

O nó RepeatLatentBatch foi projetado para replicar um lote de representações latentes um número especificado de vezes, podendo incluir dados adicionais como máscaras de ruído e índices de lote. Essa funcionalidade é essencial para operações que exigem múltiplas instâncias dos mesmos dados latentes, como aumento de dados ou tarefas generativas específicas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `amostras` | O parâmetro 'samples' representa as representações latentes a serem replicadas. É essencial para definir os dados que passarão pelo processo de repetição. | `LATENT` |
| `quantidade` | O parâmetro 'amount' especifica o número de vezes que as amostras de entrada devem ser repetidas. Ele influencia diretamente o tamanho do lote de saída, afetando assim a carga computacional e a diversidade dos dados gerados. | `INT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `latent` | A saída é uma versão modificada das representações latentes de entrada, replicadas de acordo com o 'amount' especificado. Pode incluir máscaras de ruído replicadas e índices de lote ajustados, quando aplicável. | `LATENT` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RepeatLatentBatch/pt-BR.md)
