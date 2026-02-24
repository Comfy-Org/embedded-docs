> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceText/pt-BR.md)

O nó Replace Text realiza uma substituição simples de texto. Ele procura por um trecho de texto especificado na entrada e substitui cada ocorrência por um novo trecho de texto. A operação é aplicada a todos os textos de entrada fornecidos ao nó.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | Sim | - | O texto a ser processado. |
| `find` | STRING | Não | - | O texto a ser localizado e substituído (padrão: string vazia). |
| `replace` | STRING | Não | - | O texto que substituirá o texto encontrado (padrão: string vazia). |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `text` | STRING | O texto processado, com todas as ocorrências do texto `find` substituídas pelo texto `replace`. |
