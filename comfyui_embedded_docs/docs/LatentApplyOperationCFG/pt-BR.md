# LatentApplyOperationCFG

O nó LatentApplyOperationCFG aplica uma operação latente para modificar o processo de orientação de condicionamento em um modelo. Ele funciona interceptando as saídas de condicionamento durante o processo de amostragem com orientação sem classificador (CFG) e aplicando a operação especificada às representações latentes antes de serem usadas para a geração. Quando o amostrador produz duas saídas de condicionamento, a operação é aplicada à diferença entre elas, e a segunda saída é então adicionada de volta ao resultado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo ao qual a operação de CFG será aplicada | MODEL | Sim | - |
| `operação` | A operação latente a ser aplicada durante o processo de amostragem do CFG | LATENT_OPERATION | Sim | - |

Observação: Este nó é marcado como experimental. A operação é aplicada às saídas de condicionamento do modelo durante o processo de amostragem do CFG. Quando duas saídas de condicionamento estão presentes, a operação é aplicada à diferença entre a primeira e a segunda saída, e a segunda saída é adicionada de volta. Quando apenas uma saída de condicionamento está presente, a operação é aplicada diretamente a ela.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com a operação de CFG aplicada ao seu processo de amostragem | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e383684a785878bfa4004c2fac78ae562d8e035fdfe081f8e4ebbb2c50161987`
