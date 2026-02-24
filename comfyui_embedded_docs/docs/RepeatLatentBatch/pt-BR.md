> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RepeatLatentBatch/pt-BR.md)

O nó RepeatLatentBatch foi projetado para replicar um determinado lote de representações latentes um número especificado de vezes, potencialmente incluindo dados adicionais como máscaras de ruído e índices de lote. Essa funcionalidade é crucial para operações que exigem múltiplas instâncias dos mesmos dados latentes, como aumento de dados ou tarefas generativas específicas.

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | O parâmetro 'samples' representa as representações latentes a serem replicadas. É essencial para definir os dados que passarão pela repetição. |
| `amount`  | `INT`       | O parâmetro 'amount' especifica quantas vezes as amostras de entrada devem ser repetidas. Ele influencia diretamente o tamanho do lote de saída, afetando assim a carga computacional e a diversidade dos dados gerados. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | A saída é uma versão modificada das representações latentes de entrada, replicadas de acordo com o 'amount' especificado. Pode incluir máscaras de ruído replicadas e índices de lote ajustados, se aplicável. |
