O ComboOptionTestNode é um nó lógico projetado para testar e repassar seleções de caixas de combinação. Ele recebe duas entradas de caixa de combinação, cada uma com um conjunto predefinido de opções, e gera os valores selecionados diretamente, sem modificação.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `combo` | A primeira seleção de um conjunto de três opções de teste. | COMBO | Sim | `"option1"`<br>`"option2"`<br>`"option3"` |
| `combo2` | A segunda seleção de um conjunto diferente de três opções de teste. | COMBO | Sim | `"option4"`<br>`"option5"`<br>`"option6"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output_1` | Gera o valor selecionado na primeira caixa de combinação (`combo`). | COMBO |
| `output_2` | Gera o valor selecionado na segunda caixa de combinação (`combo2`). | COMBO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2f5a73eb7c2962a983b12688159e52d4d05f569d67909f536956ab18a6cc87d7`
