> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentFromBatch/pt-BR.md)

Este nó foi projetado para extrair um subconjunto específico de amostras latentes de um lote fornecido, com base no índice e no comprimento do lote especificados. Ele permite o processamento seletivo de amostras latentes, facilitando operações em segmentos menores do lote para maior eficiência ou manipulação direcionada.

## Entradas

| Parâmetro     | Tipo de Dados | Descrição |
|---------------|-------------|-------------|
| `samples`     | `LATENT`    | A coleção de amostras latentes da qual um subconjunto será extraído. Este parâmetro é crucial para determinar o lote de origem das amostras a serem processadas. |
| `batch_index` | `INT`       | Especifica o índice inicial dentro do lote a partir do qual o subconjunto de amostras começará. Este parâmetro permite a extração direcionada de amostras de posições específicas no lote. |
| `length`      | `INT`       | Define o número de amostras a serem extraídas a partir do índice inicial especificado. Este parâmetro controla o tamanho do subconjunto a ser processado, permitindo uma manipulação flexível de segmentos do lote. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | O subconjunto extraído de amostras latentes, agora disponível para processamento ou análise posterior. |
