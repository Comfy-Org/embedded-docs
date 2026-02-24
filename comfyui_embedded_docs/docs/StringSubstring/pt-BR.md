> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringSubstring/pt-BR.md)

O nó StringSubstring extrai uma porção de texto de uma string maior. Ele recebe uma posição inicial e uma posição final para definir a seção que você deseja extrair e, em seguida, retorna o texto entre essas duas posições.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Sim | - | A string de texto de entrada da qual será extraída a substring |
| `start` | INT | Sim | - | O índice da posição inicial para a substring |
| `end` | INT | Sim | - | O índice da posição final para a substring |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | STRING | A substring extraída do texto de entrada |
