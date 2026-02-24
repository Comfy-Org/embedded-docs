> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringLength/pt-BR.md)

O nó StringLength calcula o número de caracteres em uma string de texto. Ele recebe qualquer entrada de texto e retorna a contagem total de caracteres, incluindo espaços e pontuação. Isso é útil para medir o comprimento do texto ou validar requisitos de tamanho de string.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Sim | N/A | A string de texto cujo comprimento será medido. Suporta entrada de múltiplas linhas. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `length` | INT | O número total de caracteres na string de entrada, incluindo espaços e caracteres especiais. |
