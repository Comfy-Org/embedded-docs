O nó PairConditioningCombine mescla dois pares de condicionamento separados (cada um consistindo em um condicionamento positivo e negativo) em um único par combinado. Ele recebe os condicionamentos positivo e negativo de duas fontes diferentes e os combina usando a lógica interna do ComfyUI, gerando um condicionamento positivo final e um condicionamento negativo final. Este nó é experimental e projetado para fluxos de trabalho avançados de manipulação de condicionamento.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo_A` | Primeira entrada de condicionamento positivo | CONDITIONING | Sim | - |
| `negativo_A` | Primeira entrada de condicionamento negativo | CONDITIONING | Sim | - |
| `positivo_B` | Segunda entrada de condicionamento positivo | CONDITIONING | Sim | - |
| `negativo_B` | Segunda entrada de condicionamento negativo | CONDITIONING | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positive` | Saída de condicionamento positivo combinado | CONDITIONING |
| `negative` | Saída de condicionamento negativo combinado | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningCombine/pt-BR.md)

---
**Source fingerprint (SHA-256):** `34c14207930ba31fea054b2e641e9666e738ed786aa117449c4a27667bde41b1`
