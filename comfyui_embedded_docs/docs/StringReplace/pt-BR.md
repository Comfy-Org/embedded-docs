> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringReplace/pt-BR.md)

O nó StringReplace executa operações de substituição de texto em strings de entrada. Ele procura por uma substring especificada dentro do texto de entrada e substitui todas as ocorrências por uma substring diferente. Este nó retorna a string modificada com todas as substituições aplicadas.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Sim | - | A string de texto de entrada onde as substituições serão realizadas |
| `find` | STRING | Sim | - | A substring a ser procurada dentro do texto de entrada |
| `replace` | STRING | Sim | - | O texto de substituição que irá substituir todas as ocorrências encontradas |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | STRING | A string modificada com todas as ocorrências do texto de busca substituídas pelo texto de substituição |
