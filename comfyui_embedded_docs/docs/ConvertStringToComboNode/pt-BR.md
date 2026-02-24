> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConvertStringToComboNode/pt-BR.md)

O nó Convert String to Combo recebe uma string de texto como entrada e a converte para o tipo de dados COMBO. Isso permite que você use um valor de texto como uma seleção para outros nós que exigem uma entrada do tipo COMBO. Ele simplesmente passa o valor da string inalterado, mas altera seu tipo de dados.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Sim | N/A | A string de texto a ser convertida para o tipo COMBO. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | COMBO | A string de entrada, agora formatada como um tipo de dados COMBO. |
