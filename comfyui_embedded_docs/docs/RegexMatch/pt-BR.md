> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexMatch/pt-BR.md)

O nó RegexMatch verifica se uma string de texto contém uma correspondência para um determinado padrão de expressão regular. Ele pesquisa a string de entrada e retorna um resultado simples de sim/não indicando se o padrão foi encontrado em qualquer parte do texto. Você pode ajustar como a pesquisa funciona ativando opções como correspondência sem distinção entre maiúsculas e minúsculas ou modo multilinha.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `string` | STRING | Sim | - | A string de texto a ser pesquisada por correspondências |
| `regex_pattern` | STRING | Sim | - | O padrão de expressão regular para corresponder à string |
| `case_insensitive` | BOOLEAN | Não | - | Se deve ignorar maiúsculas/minúsculas ao corresponder (padrão: Verdadeiro) |
| `multiline` | BOOLEAN | Não | - | Se deve ativar o modo multilinha para correspondência regex (padrão: Falso) |
| `dotall` | BOOLEAN | Não | - | Se deve ativar o modo dotall para correspondência regex (padrão: Falso) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `matches` | BOOLEAN | Retorna Verdadeiro se o padrão regex corresponder a qualquer parte da string de entrada, Falso caso contrário |

---
**Source fingerprint (SHA-256):** `b0ee05277edd8600d880051aa33a940c01abc170553515ab02960f25b1aec2be`
