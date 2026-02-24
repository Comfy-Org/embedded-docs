> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/pt-BR.md)

O nó T5TokenizerOptions permite configurar parâmetros do tokenizador para vários tipos de modelo T5. Ele define parâmetros de preenchimento mínimo e comprimento mínimo para múltiplas variantes do modelo T5, incluindo t5xxl, pile_t5xl, t5base, mt5xl e umt5xxl. O nó recebe uma entrada CLIP e retorna um CLIP modificado com as opções de tokenizador especificadas aplicadas.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Sim | - | O modelo CLIP para o qual configurar as opções do tokenizador |
| `min_padding` | INT | Não | 0-10000 | Valor de preenchimento mínimo a ser definido para todos os tipos de modelo T5 (padrão: 0) |
| `min_length` | INT | Não | 0-10000 | Valor de comprimento mínimo a ser definido para todos os tipos de modelo T5 (padrão: 0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | CLIP | O modelo CLIP modificado com as opções de tokenizador atualizadas aplicadas a todas as variantes T5 |
