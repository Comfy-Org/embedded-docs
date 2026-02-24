> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBatch/pt-BR.md)

O nó LatentBatch foi projetado para mesclar dois conjuntos de amostras latentes em um único lote, potencialmente redimensionando um dos conjuntos para corresponder às dimensões do outro antes da concatenação. Esta operação facilita a combinação de diferentes representações latentes para tarefas de processamento ou geração subsequentes.

## Entradas

| Parâmetro    | Tipo de Dados | Descrição |
|--------------|-------------|-------------|
| `samples1`   | `LATENT`    | O primeiro conjunto de amostras latentes a ser mesclado. Ele desempenha um papel crucial na determinação da forma final do lote combinado. |
| `samples2`   | `LATENT`    | O segundo conjunto de amostras latentes a ser mesclado. Se suas dimensões diferirem do primeiro conjunto, ele será redimensionado para garantir compatibilidade antes da mesclagem. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | O conjunto mesclado de amostras latentes, agora combinado em um único lote para processamento posterior. |
