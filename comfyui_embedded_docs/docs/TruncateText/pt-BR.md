> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TruncateText/pt-BR.md)

Este nó encurta textos cortando-os em um comprimento máximo especificado. Ele recebe qualquer texto de entrada e retorna apenas a primeira parte, até o número de caracteres que você definir. É uma forma simples de garantir que o texto não exceda um determinado tamanho.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | Sim | N/A | A string de texto a ser truncada. |
| `max_length` | INT | Não | 1 a 10000 | Comprimento máximo do texto. O texto será cortado após este número de caracteres (padrão: 77). |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `string` | STRING | O texto truncado, contendo apenas os primeiros `max_length` caracteres da entrada. |
