# LatentApplyOperationCFG

O nó LatentApplyOperationCFG aplica uma operação latente dentro da etapa de classifier-free guidance (CFG) do processo de amostragem de um modelo. Ele intercepta as saídas de condicionamento produzidas antes do CFG, aplica a operação conectada aos valores latentes e retorna o modelo com esse comportamento de amostragem modificado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo ao qual a operação CFG será aplicada | MODEL | Sim | - |
| `operation` | A operação latente a ser aplicada durante o processo de amostragem CFG | LATENT_OPERATION | Sim | - |

Nota: Este nó está marcado como experimental. A operação é aplicada às saídas de condicionamento do modelo durante o processo de amostragem CFG. Quando duas saídas de condicionamento estão presentes, a operação é aplicada à diferença entre a primeira e a segunda saída, e a segunda saída é adicionada de volta ao resultado. Quando apenas uma saída de condicionamento está presente, a operação é aplicada diretamente a ela.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com a operação CFG aplicada ao seu processo de amostragem | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e383684a785878bfa4004c2fac78ae562d8e035fdfe081f8e4ebbb2c50161987`
