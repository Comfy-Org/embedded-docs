# Alternar

O nó Switch seleciona entre duas possíveis entradas com base em uma condição booleana. Ele envia para a saída a entrada `on_true` quando o `switch` está habilitado, e a entrada `on_false` quando o `switch` está desabilitado. Apenas o ramo selecionado é avaliado, portanto a outra entrada não é obrigatória. Isso permite criar lógica condicional e escolher diferentes caminhos de dados no seu fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `alternar` | Uma condição booleana que determina qual entrada será repassada. Quando habilitado (true), a entrada `on_true` é selecionada. Quando desabilitado (false), a entrada `on_false` é selecionada. | BOOLEAN | Sim |  |
| `falso` | Os dados a serem enviados para a saída quando o `switch` está desabilitado (false). Esta entrada só é obrigatória quando o `switch` é false. | MATCH_TYPE | Não |  |
| `verdadeiro` | Os dados a serem enviados para a saída quando o `switch` está habilitado (true). Esta entrada só é obrigatória quando o `switch` é true. | MATCH_TYPE | Não |  |

**Nota sobre os requisitos de entrada:** As entradas `on_false` e `on_true` são obrigatórias condicionalmente. O nó solicitará a entrada `on_true` somente quando o `switch` for true, e a entrada `on_false` somente quando o `switch` for false. Ambas as entradas devem ser do mesmo tipo de dados e devem corresponder ao tipo de dados da saída.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `saída` | Os dados selecionados. Este será o valor da entrada `on_true` se o `switch` for true, ou o valor da entrada `on_false` se o `switch` for false. | MATCH_TYPE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d0adda02e7f997f27182cb26e11e934660ae5bd80f3091bed2fed7c981632ce5`
