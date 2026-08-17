# ComfySoftSwitchNode

O nó Soft Switch seleciona entre dois valores de entrada possíveis com base em uma condição booleana. Ele gera o valor da entrada `on_true` quando `switch` é verdadeiro, e o valor da entrada `on_false` quando `switch` é falso. Este nó foi projetado para ser preguiçoso, ou seja, ele só avalia a entrada necessária com base no estado de `switch`.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `switch` | A condição booleana que determina qual entrada será repassada. Quando verdadeiro, a entrada `on_true` é selecionada. Quando falso, a entrada `on_false` é selecionada. | BOOLEAN | Sim | true<br>false |
| `on_false` | O valor a ser gerado quando a condição `switch` for falsa. Esta entrada é opcional, mas pelo menos uma de `on_false` ou `on_true` deve estar conectada. | MATCH_TYPE | Não |  |
| `on_true` | O valor a ser gerado quando a condição `switch` for verdadeira. Esta entrada é opcional, mas pelo menos uma de `on_false` ou `on_true` deve estar conectada. | MATCH_TYPE | Não |  |

**Nota:** As entradas `on_false` e `on_true` devem ser do mesmo tipo de dados, conforme definido pelo template interno do nó. Pelo menos uma dessas duas entradas deve estar conectada para que o nó funcione. Se apenas uma entrada estiver conectada, esse valor será repassado à saída independentemente do estado de `switch`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | O valor selecionado. Ele corresponderá ao tipo de dados da entrada `on_false` ou `on_true` conectada. | MATCH_TYPE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7bf4bed69d8fd8c360e971ab8068382cd8ebaa02004d5df44312977a7309ae00`
