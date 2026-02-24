> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningCombine/pt-BR.md)

O nó PairConditioningCombine combina dois pares de dados de condicionamento (positivo e negativo) em um único par. Ele recebe dois pares de condicionamento separados como entrada e os mescla usando a lógica interna de combinação de condicionamento do ComfyUI. Este nó é experimental e é usado principalmente em fluxos de trabalho avançados de manipulação de condicionamento.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive_A` | CONDITIONING | Sim | - | Primeira entrada de condicionamento positivo |
| `negative_A` | CONDITIONING | Sim | - | Primeira entrada de condicionamento negativo |
| `positive_B` | CONDITIONING | Sim | - | Segunda entrada de condicionamento positivo |
| `negative_B` | CONDITIONING | Sim | - | Segunda entrada de condicionamento negativo |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Saída de condicionamento positivo combinado |
| `negative` | CONDITIONING | Saída de condicionamento negativo combinado |
