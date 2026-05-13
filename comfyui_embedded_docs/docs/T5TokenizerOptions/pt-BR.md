> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/pt-BR.md)

O nó T5TokenizerOptions permite configurar as configurações do tokenizador para vários tipos de modelo T5. Ele define parâmetros de preenchimento mínimo e comprimento mínimo para múltiplas variantes do modelo T5, incluindo t5xxl, pile_t5xl, t5base, mt5xl e umt5xxl. O nó recebe uma entrada CLIP e retorna um CLIP modificado com as opções de tokenizador especificadas aplicadas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Sim | - | O modelo CLIP para configurar as opções do tokenizador |
| `preenchimento_mínimo` | INT | Não | 0 a 10000 | Valor mínimo de preenchimento a ser definido para todos os tipos de modelo T5 (padrão: 0) |
| `comprimento_mínimo` | INT | Não | 0 a 10000 | Valor mínimo de comprimento a ser definido para todos os tipos de modelo T5 (padrão: 0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | CLIP | O modelo CLIP modificado com as opções de tokenizador atualizadas aplicadas a todas as variantes T5 |

---
**Source fingerprint (SHA-256):** `bc05c714e4006786d0c948ed1de05324257472337397b0aa4ce574d7483929ff`
