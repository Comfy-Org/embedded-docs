# Or

O ComfyOrNode executa uma operação lógica OR (OU) em um conjunto de valores de entrada. Ele retorna `true` se qualquer um dos valores fornecidos for considerado truthy, de acordo com as regras padrão de avaliação de verdade do Python.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `value` | Um valor a ser avaliado quanto à veracidade. Você pode fornecer vários valores adicionando mais entradas. O nó retorna `true` se qualquer um desses valores for truthy. | ANY | Sim | Mínimo de 1 valor; múltiplos valores aceitos |

**Observação:** O nó aceita no mínimo 1 valor de entrada. Você pode adicionar mais entradas conforme necessário usando o recurso autogrow.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `BOOLEAN` | Retorna `true` se qualquer um dos valores de entrada for truthy; retorna `false` se todos os valores de entrada forem falsy. | BOOLEAN |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyOrNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f673aa2b0d754f55c51ba9c9ceea7d9de9a21d2e7308bd1281b4d4461243e4ad`
