> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddTextPrefix/pt-BR.md)

O nó Add Text Prefix modifica o texto adicionando uma string especificada ao início de cada texto de entrada. Ele recebe o texto e um prefixo como entrada e retorna o resultado combinado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | Sim | | O texto ao qual o prefixo será adicionado. |
| `prefix` | STRING | Não | | A string a ser adicionada ao início do texto (padrão: ""). |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `text` | STRING | O texto resultante com o prefixo adicionado à frente. |
