Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/en.md)

O nó Switch seleciona entre duas entradas possíveis com base em uma condição booleana. Ele produz a entrada `on_true` quando o `switch` está ativado, e a entrada `on_false` quando o `switch` está desativado. Isso permite criar lógica condicional e escolher diferentes caminhos de dados no seu fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `alternar` | Uma condição booleana que determina qual entrada será passada adiante. Quando ativado (verdadeiro), a entrada `verdadeiro` é selecionada. Quando desativado (falso), a entrada `falso` é selecionada. | BOOLEAN | Sim |  |
| `falso` | Os dados a serem passados para a saída quando o `alternar` estiver desativado (falso). Esta entrada é necessária apenas quando o `alternar` é falso. | MATCH_TYPE | Não |  |
| `verdadeiro` | Os dados a serem passados para a saída quando o `alternar` estiver ativado (verdadeiro). Esta entrada é necessária apenas quando o `alternar` é verdadeiro. | MATCH_TYPE | Não |  |

**Nota sobre Requisitos de Entrada:** As entradas `on_false` e `on_true` são condicionalmente obrigatórias. O nó solicitará a entrada `on_true` apenas quando o `switch` for verdadeiro, e a entrada `on_false` apenas quando o `switch` for falso. Ambas as entradas devem ser do mesmo tipo de dado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | Os dados selecionados. Será o valor da entrada `verdadeiro` se o `alternar` for verdadeiro, ou o valor da entrada `falso` se o `alternar` for falso. | MATCH_TYPE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9f3cf58c1a04116fa0cbe8007fe3ed90e93c4de2e65f6778761d03fb21a63af3`
