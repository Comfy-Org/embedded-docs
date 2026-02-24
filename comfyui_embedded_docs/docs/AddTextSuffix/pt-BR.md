> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddTextSuffix/pt-BR.md)

Este nó adiciona um sufixo especificado ao final de uma string de texto de entrada. Ele recebe o texto original e o sufixo como entradas e retorna o resultado combinado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | Sim | | O texto original ao qual o sufixo será adicionado. |
| `suffix` | STRING | Não | | O sufixo a ser adicionado ao texto (padrão: ""). |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `text` | STRING | O texto resultante após a adição do sufixo. |
