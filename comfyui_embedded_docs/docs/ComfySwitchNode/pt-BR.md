# Alternar

O nó If/Else Switch seleciona entre duas entradas possíveis com base em uma condição booleana. Quando `switch` está habilitado (true), ele passa a entrada `on_true` para a saída; quando desabilitado (false), ele passa `on_false`. As entradas têm avaliação preguiçosa (lazy), de modo que apenas o ramo selecionado é avaliado e a outra entrada não precisa estar conectada.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `switch` | Uma condição booleana que determina qual entrada é passada para a saída. Quando habilitado (true), a entrada `on_true` é selecionada. Quando desabilitado (false), a entrada `on_false` é selecionada. | BOOLEAN | Sim |  |
| `on_false` | Os dados a serem passados para a saída quando `switch` estiver desabilitado (false). Esta entrada é solicitada apenas quando `switch` for false. | MATCH_TYPE | Não |  |
| `on_true` | Os dados a serem passados para a saída quando `switch` estiver habilitado (true). Esta entrada é solicitada apenas quando `switch` for true. | MATCH_TYPE | Não |  |

**Nota sobre os requisitos das entradas:** As entradas `on_false` e `on_true` são solicitadas condicionalmente. O nó solicita `on_true` apenas quando `switch` for true, e solicita `on_false` apenas quando `switch` for false. Ambas as entradas devem ser do mesmo tipo de dados, e esse tipo deve corresponder ao tipo de dados da saída. Se a entrada selecionada não estiver conectada, o nó não gera nenhum valor.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `output` | Os dados selecionados: o valor de `on_true` quando `switch` for true, ou o valor de `on_false` quando `switch` for false. | MATCH_TYPE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `42c442efeda0197d950702c52647233dee1a30216fb07e1ce4bc844784a6c5f2`
