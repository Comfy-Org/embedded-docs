O nó StringCompare compara duas strings de texto usando diferentes métodos de comparação. Ele pode verificar se uma string começa com outra, termina com outra ou se ambas as strings são exatamente iguais. A comparação pode ser realizada considerando ou não diferenças entre maiúsculas e minúsculas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `string_a` | A primeira string a ser comparada | STRING | Sim | - |
| `string_b` | A segunda string para comparação | STRING | Sim | - |
| `modo` | O método de comparação a ser usado (padrão: "Starts With") | COMBO | Sim | "Starts With"<br>"Ends With"<br>"Equal" |
| `diferenciar_maiusculas_minusculas` | Se deve considerar diferenças entre maiúsculas e minúsculas durante a comparação (padrão: true) | BOOLEAN | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | Retorna true se a condição de comparação for atendida, false caso contrário | BOOLEAN |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringCompare/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4491e4acd2c1881e9c924c6ae51d764dec5f46279094d173fe551e9ee9256597`
