# And

O nó And realiza uma operação lógica AND em um grupo de valores de entrada. Ele retorna `true` apenas quando todos os valores conectados são considerados truthy de acordo com as regras de truthiness do Python, o que o torna útil para verificar se várias condições são atendidas ao mesmo tempo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `valores` | Um grupo expansível de valores a serem avaliados. O nó começa com um slot e você pode adicionar mais clicando no botão "+" no nó. Aceita qualquer tipo de dados. | ANY | Sim | Mínimo 1 (sem máximo) |

**Nota:** Esta entrada é um grupo de slots expansível. Os slots são adicionados individualmente (por exemplo, `value_1`, `value_2` e assim por diante), e pelo menos um slot deve estar presente.

**Nota:** O nó usa as regras de truthiness do Python para decidir se um valor é `true` ou `false`. Por exemplo, uma string vazia, o número 0, uma lista vazia e `None` são todos tratados como `false`. Todos os outros valores são tratados como `true`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `BOOLEAN` | Retorna `true` se todos os valores de entrada forem truthy; caso contrário, retorna `false`. | BOOLEAN |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyAndNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e7359c46da62f9859ea4f4a239cf20c565b5f7de22d280afc00c7ca321f1c89d`
