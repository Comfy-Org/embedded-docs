# And

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyAndNode/en.md)

## Visão Geral

O nó And realiza uma operação lógica E em um conjunto de valores de entrada. Ele retorna `true` somente se todos os valores fornecidos forem considerados verdadeiros de acordo com as regras de veracidade do Python. Este nó é útil para verificar se múltiplas condições são todas atendidas antes de prosseguir.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `valores` | Uma lista de valores a serem avaliados. O nó aceita pelo menos um valor, e você pode adicionar mais clicando no botão "+" no nó. | ANY | Sim | 1 ou mais valores |

**Nota:** O nó utiliza as regras de veracidade do Python para determinar se um valor é `true` ou `false`. Por exemplo, uma string vazia, o número 0, uma lista vazia e `None` são todos considerados `false`. Todos os outros valores são considerados `true`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `BOOLEAN` | Retorna `true` se todos os valores de entrada forem verdadeiros, caso contrário retorna `false`. | BOOLEAN |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyAndNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fd9d18ce698472a7e35ad3082f2ccff8ae264b11bd887a498f929cd877ff38c4`
