# And

O nó And realiza uma operação lógica E (AND) sobre um conjunto de valores de entrada. Ele retorna `true` somente se todos os valores fornecidos forem considerados verdadeiros de acordo com as regras de truthiness do Python. Este nó é útil para verificar se múltiplas condições são todas atendidas antes de prosseguir.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `values` | Uma lista expansível de valores para avaliar. O nó exige pelo menos um valor, e você pode adicionar mais campos clicando no botão "+" no nó. Cada campo aceita qualquer tipo de dados. | ANY | Sim | 1 ou mais valores |

**Nota:** O nó usa as regras de truthiness do Python para determinar se um valor é `true` ou `false`. Por exemplo, uma string vazia, o número 0, uma lista vazia e `None` são todos considerados `false`. Todos os outros valores são considerados `true`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `BOOLEAN` | Retorna `true` se todos os valores de entrada forem verdadeiros (truthy); caso contrário, retorna `false`. | BOOLEAN |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyAndNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e7359c46da62f9859ea4f4a239cf20c565b5f7de22d280afc00c7ca321f1c89d`
