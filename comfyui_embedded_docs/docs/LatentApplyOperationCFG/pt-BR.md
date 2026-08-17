# LatentApplyOperationCFG

O nó LatentApplyOperationCFG aplica uma operação latente para modificar o processo de orientação de condicionamento em um modelo. Ele funciona interceptando as saídas de condicionamento durante o processo de amostragem de orientação livre de classificador (CFG) e aplicando a operação especificada às representações latentes antes de serem usadas para geração.

Quando o modelo produz duas saídas de condicionamento (por exemplo, condicionamento positivo e negativo), a operação é aplicada à diferença entre elas, e o segundo condicionamento é então adicionado de volta. Quando há apenas uma saída de condicionamento, a operação é aplicada diretamente a ela. Este nó é marcado como experimental.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo ao qual a operação CFG será aplicada | MODEL | Sim | - |
| `operation` | A operação latente a ser aplicada durante o processo de amostragem CFG | LATENT_OPERATION | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com a operação CFG aplicada ao seu processo de amostragem | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e383684a785878bfa4004c2fac78ae562d8e035fdfe081f8e4ebbb2c50161987`
