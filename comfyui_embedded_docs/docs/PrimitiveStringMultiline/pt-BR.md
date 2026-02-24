> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveStringMultiline/pt-BR.md)

O nó PrimitiveStringMultiline fornece um campo de entrada de texto multilinha para inserir e passar valores de string através do seu fluxo de trabalho. Ele aceita entrada de texto com múltiplas linhas e emite o mesmo valor de string inalterado. Este nó é útil quando você precisa inserir conteúdo de texto mais longo ou texto formatado que abrange várias linhas.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `value` | STRING | Sim | N/A | O valor de entrada de texto que pode abranger múltiplas linhas |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | STRING | O mesmo valor de string que foi fornecido como entrada |
