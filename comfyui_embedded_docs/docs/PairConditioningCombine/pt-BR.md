> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningCombine/pt-BR.md)

O nó PairConditioningCombine mescla dois pares de condicionamento separados (cada um consistindo em um condicionamento positivo e negativo) em um único par combinado. Ele recebe os condicionamentos positivo e negativo de duas fontes diferentes e os combina usando a lógica interna do ComfyUI, gerando um condicionamento positivo final e um condicionamento negativo final. Este nó é experimental e projetado para fluxos de trabalho avançados de manipulação de condicionamento.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `positive_A` | CONDITIONING | Sim | - | Primeira entrada de condicionamento positivo |
| `negative_A` | CONDITIONING | Sim | - | Primeira entrada de condicionamento negativo |
| `positive_B` | CONDITIONING | Sim | - | Segunda entrada de condicionamento positivo |
| `negative_B` | CONDITIONING | Sim | - | Segunda entrada de condicionamento negativo |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `positive` | CONDITIONING | Saída de condicionamento positivo combinado |
| `negative` | CONDITIONING | Saída de condicionamento negativo combinado |

---
**Source fingerprint (SHA-256):** `34c14207930ba31fea054b2e641e9666e738ed786aa117449c4a27667bde41b1`
