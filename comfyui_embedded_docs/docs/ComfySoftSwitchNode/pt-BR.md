> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/pt-BR.md)

O nó Soft Switch seleciona entre dois valores de entrada possíveis com base em uma condição booleana. Ele emite o valor da entrada `on_true` quando o `switch` é verdadeiro, e o valor da entrada `on_false` quando o `switch` é falso. Este nó foi projetado para ser "lazy" (preguiçoso), o que significa que ele avalia apenas a entrada necessária com base no estado do switch.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `switch` | BOOLEAN | Sim | | A condição booleana que determina qual entrada será repassada. Quando verdadeira, a entrada `on_true` é selecionada. Quando falsa, a entrada `on_false` é selecionada. |
| `on_false` | MATCH_TYPE | Não | | O valor a ser emitido quando a condição `switch` for falsa. Esta entrada é opcional, mas pelo menos uma das entradas `on_false` ou `on_true` deve estar conectada. |
| `on_true` | MATCH_TYPE | Não | | O valor a ser emitido quando a condição `switch` for verdadeira. Esta entrada é opcional, mas pelo menos uma das entradas `on_false` ou `on_true` deve estar conectada. |

**Observação:** As entradas `on_false` e `on_true` devem ser do mesmo tipo de dados, conforme definido pelo template interno do nó. Pelo menos uma dessas duas entradas deve estar conectada para que o nó funcione.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | MATCH_TYPE | O valor selecionado. Ele corresponderá ao tipo de dados da entrada `on_false` ou `on_true` conectada. |
