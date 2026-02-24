> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringContains/pt-BR.md)

O nó StringContains verifica se uma determinada string contém uma substring especificada. Ele pode realizar essa verificação com correspondência sensível ou não sensível a maiúsculas e minúsculas, retornando um resultado booleano indicando se a substring foi encontrada dentro da string principal.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Sim | - | A string de texto principal na qual será feita a busca |
| `substring` | STRING | Sim | - | O texto a ser procurado dentro da string principal |
| `case_sensitive` | BOOLEAN | Não | - | Determina se a busca deve ser sensível a maiúsculas e minúsculas (padrão: true) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `contains` | BOOLEAN | Retorna verdadeiro se a substring for encontrada na string, falso caso contrário |
