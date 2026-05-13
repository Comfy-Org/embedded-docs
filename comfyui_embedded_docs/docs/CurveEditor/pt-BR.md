> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CurveEditor/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CurveEditor/en.md)

O nó Curve Editor fornece uma interface visual para ajustar e refinar uma curva. Ele permite modificar a forma de uma curva de entrada e, opcionalmente, visualizar sua distribuição com um histograma. O nó gera a curva modificada para uso em outras partes do seu fluxo de trabalho.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `curve` | CURVE | Sim | N/A | A curva de entrada a ser editada. |
| `histogram` | HISTOGRAM | Não | N/A | Um histograma opcional para exibir junto com a curva como referência visual. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `curve` | CURVE | A curva editada após os ajustes realizados na interface do nó. |

---
**Source fingerprint (SHA-256):** `34cf36a5b934c44ebfce0b81e7c515f1b31fb17f3b7e1ad52255d1d72f68240b`
