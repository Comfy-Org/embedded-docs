> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/pt-BR.md)

O ComboOptionTestNode é um nó lógico projetado para testar e repassar seleções de caixas de combinação. Ele recebe duas entradas de caixa de combinação, cada uma com um conjunto predefinido de opções, e gera os valores selecionados diretamente, sem modificação.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `combo` | COMBO | Sim | `"option1"`<br>`"option2"`<br>`"option3"` | A primeira seleção de um conjunto de três opções de teste. |
| `combo2` | COMBO | Sim | `"option4"`<br>`"option5"`<br>`"option6"` | A segunda seleção de um conjunto diferente de três opções de teste. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `output_1` | COMBO | Gera o valor selecionado na primeira caixa de combinação (`combo`). |
| `output_2` | COMBO | Gera o valor selecionado na segunda caixa de combinação (`combo2`). |

---
**Source fingerprint (SHA-256):** `2f5a73eb7c2962a983b12688159e52d4d05f569d67909f536956ab18a6cc87d7`
