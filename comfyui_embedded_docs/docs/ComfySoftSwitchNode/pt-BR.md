# ComfySoftSwitchNode

O nó Soft Switch seleciona entre dois valores de entrada possíveis com base em uma condição booleana. Ele produz o valor da entrada `on_true` quando o `switch` é verdadeiro, e o valor da entrada `on_false` quando o `switch` é falso. Este nó é projetado com avaliação preguiçosa, ou seja, ele só avalia a entrada necessária com base no estado do `switch`.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `switch` | A condição booleana que determina qual entrada será passada adiante. Quando for verdadeira, a entrada `on_true` é selecionada. Quando for falsa, a entrada `on_false` é selecionada. | BOOLEAN | Sim | True or False |
| `on_false` | O valor a ser produzido quando a condição `switch` for falsa. Esta entrada é opcional, mas pelo menos uma das entradas `on_false` ou `on_true` deve estar conectada. | MATCH_TYPE | Não | Mesmo tipo de dados que `on_true` |
| `on_true` | O valor a ser produzido quando a condição `switch` for verdadeira. Esta entrada é opcional, mas pelo menos uma das entradas `on_false` ou `on_true` deve estar conectada. | MATCH_TYPE | Não | Mesmo tipo de dados que `on_false` |

**Nota:** As entradas `on_false` e `on_true` devem ser do mesmo tipo de dados, conforme definido pelo template interno do nó. Pelo menos uma dessas duas entradas deve estar conectada para que o nó funcione. Como o nó é preguiçoso, quando apenas uma entrada está conectada, o nó sempre produz o valor dessa entrada, independentemente do estado do `switch`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | O valor selecionado. Ele corresponde ao tipo de dados da entrada `on_false` ou `on_true` conectada. Quando ambas as entradas estão conectadas, ele produz `on_true` se `switch` for verdadeiro, e `on_false` se `switch` for falso. | MATCH_TYPE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7bf4bed69d8fd8c360e971ab8068382cd8ebaa02004d5df44312977a7309ae00`
