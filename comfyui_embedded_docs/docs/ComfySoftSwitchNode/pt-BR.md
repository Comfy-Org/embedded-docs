# ComfySoftSwitchNode

O nó Soft Switch seleciona entre dois valores de entrada possíveis com base em uma condição booleana. Ele gera como saída o valor da entrada `on_true` quando `switch` for true, e o valor da entrada `on_false` quando `switch` for false. Este nó foi projetado para ser lazy, o que significa que ele só avalia a entrada que é realmente necessária com base no estado de `switch`.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `switch` | A condição booleana que determina qual entrada será passada adiante. Quando true, a entrada `on_true` é selecionada. Quando false, a entrada `on_false` é selecionada. | BOOLEAN | Sim | True or False |
| `on_false` | O valor a ser gerado na saída quando a condição `switch` for false. Esta entrada é opcional, mas pelo menos uma das entradas `on_false` ou `on_true` deve estar conectada. | MATCH_TYPE | Não | Mesmo tipo de dados que `on_true` |
| `on_true` | O valor a ser gerado na saída quando a condição `switch` for true. Esta entrada é opcional, mas pelo menos uma das entradas `on_false` ou `on_true` deve estar conectada. | MATCH_TYPE | Não | Mesmo tipo de dados que `on_false` |

**Nota:** As entradas `on_false` e `on_true` devem ser do mesmo tipo de dados, conforme definido pelo template interno do nó. Pelo menos uma dessas duas entradas deve estar conectada; caso contrário, o nó retorna a mensagem de validação "At least one of on_false or on_true must be connected to Switch node". Como o nó é lazy, quando apenas uma entrada está conectada, o nó sempre gera o valor dessa entrada independentemente do estado de `switch`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | O valor selecionado. Ele corresponde ao tipo de dados da entrada `on_false` ou `on_true` conectada. Quando ambas as entradas estão conectadas, ele gera `on_true` se `switch` for true, e `on_false` se `switch` for false. | MATCH_TYPE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7bf4bed69d8fd8c360e971ab8068382cd8ebaa02004d5df44312977a7309ae00`
