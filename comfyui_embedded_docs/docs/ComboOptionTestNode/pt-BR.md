> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/pt-BR.md)

O ComboOptionTestNode é um nó de lógica projetado para testar e repassar seleções de caixas de combinação. Ele recebe duas entradas de caixa de combinação, cada uma com um conjunto predefinido de opções, e emite os valores selecionados diretamente, sem modificação.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `combo` | COMBO | Sim | `"option1"`<br>`"option2"`<br>`"option3"` | A primeira seleção de um conjunto de três opções de teste. |
| `combo2` | COMBO | Sim | `"option4"`<br>`"option5"`<br>`"option6"` | A segunda seleção de um conjunto diferente de três opções de teste. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output_1` | COMBO | Emite o valor selecionado na primeira caixa de combinação (`combo`). |
| `output_2` | COMBO | Emite o valor selecionado na segunda caixa de combinação (`combo2`). |
