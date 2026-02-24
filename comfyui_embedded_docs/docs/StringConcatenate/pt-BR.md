> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringConcatenate/pt-BR.md)

O nó StringConcatenate combina duas strings de texto em uma, unindo-as com um delimitador especificado. Ele recebe duas strings de entrada e um caractere ou string delimitador, e então produz uma única string onde as duas entradas são conectadas com o delimitador posicionado entre elas.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `string_a` | STRING | Sim | - | A primeira string de texto a ser concatenada |
| `string_b` | STRING | Sim | - | A segunda string de texto a ser concatenada |
| `delimiter` | STRING | Não | - | O caractere ou string a ser inserido entre as duas strings de entrada (padrão: string vazia) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | STRING | A string combinada com o delimitador inserido entre `string_a` e `string_b` |
