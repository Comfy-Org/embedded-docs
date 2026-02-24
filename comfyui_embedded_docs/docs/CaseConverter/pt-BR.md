> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CaseConverter/pt-BR.md)

O nó Case Converter transforma strings de texto em diferentes formatos de caixa de letras. Ele recebe uma string de entrada e a converte com base no modo selecionado, produzindo uma string de saída com a formatação de caixa especificada aplicada. O nó suporta quatro opções diferentes de conversão de caixa para modificar a capitalização do seu texto.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `string` | STRING | String | - | - | A string de texto a ser convertida para um formato de caixa diferente |
| `mode` | STRING | Combo | - | ["UPPERCASE", "lowercase", "Capitalize", "Title Case"] | O modo de conversão de caixa a aplicar: UPPERCASE converte todas as letras para maiúsculas, lowercase converte todas as letras para minúsculas, Capitalize coloca em maiúscula apenas a primeira letra, Title Case coloca em maiúscula a primeira letra de cada palavra |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | STRING | A string de entrada convertida para o formato de caixa especificado |
