> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringCompare/pt-BR.md)

O nó StringCompare compara duas strings de texto usando diferentes métodos de comparação. Ele pode verificar se uma string começa com outra, termina com outra ou se ambas as strings são exatamente iguais. A comparação pode ser realizada considerando ou não as diferenças entre letras maiúsculas e minúsculas.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `string_a` | STRING | Sim | - | A primeira string a ser comparada |
| `string_b` | STRING | Sim | - | A segunda string contra a qual comparar |
| `mode` | COMBO | Sim | "Starts With"<br>"Ends With"<br>"Equal" | O método de comparação a ser utilizado |
| `case_sensitive` | BOOLEAN | Não | - | Se deve considerar a diferença entre maiúsculas e minúsculas durante a comparação (padrão: true) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | BOOLEAN | Retorna verdadeiro se a condição de comparação for atendida, falso caso contrário |
