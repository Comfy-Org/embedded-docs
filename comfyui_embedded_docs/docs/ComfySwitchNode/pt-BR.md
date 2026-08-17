# Alternar

O nó Switch seleciona entre duas entradas possíveis com base em uma condição booleana. Ele gera a entrada `on_true` quando o `switch` está habilitado e a entrada `on_false` quando o `switch` está desabilitado, permitindo criar lógica condicional e escolher diferentes caminhos de dados no seu fluxo de trabalho. Este nó está atualmente marcado como experimental.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `switch` | Uma condição booleana que determina qual entrada será passada adiante. Quando habilitado (verdadeiro), a entrada `on_true` é selecionada. Quando desabilitado (falso), a entrada `on_false` é selecionada. | BOOLEAN | Sim |  |
| `on_false` | Os dados a serem passados para a saída quando o `switch` estiver desabilitado (falso). Esta entrada é necessária apenas quando o `switch` for falso. | MATCH_TYPE | Não |  |
| `on_true` | Os dados a serem passados para a saída quando o `switch` estiver habilitado (verdadeiro). Esta entrada é necessária apenas quando o `switch` for verdadeiro. | MATCH_TYPE | Não |  |

**Nota sobre Requisitos de Entrada:** As entradas `on_false` e `on_true` são condicionalmente obrigatórias. O nó solicitará a entrada `on_true` apenas quando o `switch` for verdadeiro, e a entrada `on_false` apenas quando o `switch` for falso. Ambas as entradas devem ser do mesmo tipo de dados.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | Os dados selecionados. Este será o valor da entrada `on_true` se o `switch` for verdadeiro, ou o valor da entrada `on_false` se o `switch` for falso. | MATCH_TYPE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d0adda02e7f997f27182cb26e11e934660ae5bd80f3091bed2fed7c981632ce5`
