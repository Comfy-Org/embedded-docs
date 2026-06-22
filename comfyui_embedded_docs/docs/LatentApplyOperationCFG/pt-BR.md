# LatentApplyOperationCFG

O nó **LatentApplyOperationCFG** aplica uma operação latente para modificar o processo de orientação por condicionamento em um modelo. Ele funciona interceptando as saídas de condicionamento durante o processo de amostragem por orientação livre de classificador (CFG) e aplicando a operação especificada às representações latentes antes que elas sejam utilizadas para a geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo ao qual a operação CFG será aplicada | MODEL | Sim | - |
| `operação` | A operação latente a ser aplicada durante o processo de amostragem CFG | LATENT_OPERATION | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `modelo` | O modelo modificado com a operação CFG aplicada ao seu processo de amostragem | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9fbcc9183abf89bb93e55263bb655e931549360c05a561f7dacae8723db62e52`
