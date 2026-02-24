> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexMatch/pt-BR.md)

O nó RegexMatch verifica se uma string de texto corresponde a um padrão de expressão regular especificado. Ele pesquisa a string de entrada por qualquer ocorrência do padrão regex e retorna se uma correspondência foi encontrada. Você pode configurar várias flags de regex, como sensibilidade a maiúsculas/minúsculas, modo multilinha e modo dotall, para controlar como o casamento de padrões se comporta.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Sim | - | A string de texto na qual buscar correspondências |
| `regex_pattern` | STRING | Sim | - | O padrão de expressão regular para comparar com a string |
| `case_insensitive` | BOOLEAN | Não | - | Se deve ignorar maiúsculas/minúsculas ao fazer a correspondência (padrão: Verdadeiro) |
| `multiline` | BOOLEAN | Não | - | Se deve habilitar o modo multilinha para a correspondência regex (padrão: Falso) |
| `dotall` | BOOLEAN | Não | - | Se deve habilitar o modo dotall para a correspondência regex (padrão: Falso) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `matches` | BOOLEAN | Retorna Verdadeiro se o padrão regex corresponder a qualquer parte da string de entrada, Falso caso contrário |
