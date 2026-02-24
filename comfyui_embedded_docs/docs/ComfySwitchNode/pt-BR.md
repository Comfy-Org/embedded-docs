> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/pt-BR.md)

O nó Switch seleciona entre duas entradas possíveis com base em uma condição booleana. Ele retorna a entrada `on_true` quando o `switch` está ativado e a entrada `on_false` quando o `switch` está desativado. Isso permite criar lógica condicional e escolher diferentes caminhos de dados em seu fluxo de trabalho.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `switch` | BOOLEAN | Sim | | Uma condição booleana que determina qual entrada será repassada. Quando ativado (true), a entrada `on_true` é selecionada. Quando desativado (false), a entrada `on_false` é selecionada. |
| `on_false` | MATCH_TYPE | Não | | Os dados a serem passados para a saída quando o `switch` está desativado (false). Esta entrada só é necessária quando o `switch` é false. |
| `on_true` | MATCH_TYPE | Não | | Os dados a serem passados para a saída quando o `switch` está ativado (true). Esta entrada só é necessária quando o `switch` é true. |

**Nota sobre os Requisitos de Entrada:** As entradas `on_false` e `on_true` são condicionalmente obrigatórias. O nó solicitará a entrada `on_true` apenas quando o `switch` for true e a entrada `on_false` apenas quando o `switch` for false. Ambas as entradas devem ser do mesmo tipo de dado.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | MATCH_TYPE | O dado selecionado. Este será o valor da entrada `on_true` se o `switch` for true, ou o valor da entrada `on_false` se o `switch` for false. |
