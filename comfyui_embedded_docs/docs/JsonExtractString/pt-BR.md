> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JsonExtractString/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JsonExtractString/en.md)

O nó JsonExtractString lê uma string de texto contendo dados JSON e extrai o valor associado a uma chave específica. Ele converte o valor extraído em uma string. Se o JSON for inválido, a chave não for encontrada ou o valor for nulo, o nó retorna uma string vazia.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `json_string` | STRING | Sim | N/A | O texto contendo os dados JSON a serem analisados. |
| `key` | STRING | Sim | N/A | A chave específica cujo valor em string você deseja extrair do objeto JSON. |

**Observação:** O nó extrai apenas valores de objetos JSON (dicionários). Se o JSON analisado não for um objeto ou se a chave especificada não existir dentro dele, a saída será uma string vazia.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `output` | STRING | O valor em string extraído do JSON para a chave especificada, ou uma string vazia se a extração falhar. |