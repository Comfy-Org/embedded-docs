> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/pt-BR.md)

O nó PreviewAny exibe uma prévia de qualquer tipo de dado de entrada em formato de texto. Ele aceita qualquer tipo de dado como entrada e o converte em uma representação de string legível para visualização. O nó lida automaticamente com diferentes tipos de dados, incluindo strings, números, booleanos e objetos complexos, tentando serializá-los para o formato JSON.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `source` | ANY | Sim | Qualquer tipo de dado | Aceita qualquer tipo de dado de entrada para exibição em prévia |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| Exibição de Texto na Interface | TEXT | Exibe os dados de entrada convertidos para formato de texto na interface do usuário |
