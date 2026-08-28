# Or

O nó Or realiza uma operação lógica OU em um conjunto de valores de entrada. Ele retorna `true` se qualquer um dos valores fornecidos for considerado verdadeiro de acordo com as regras padrão de verdade do Python.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `valores` | Uma coleção expansível de valores para avaliar quanto à veracidade. Cada slot de entrada adicionado é nomeado `value_1`, `value_2` e assim por diante. O nó retorna `true` se qualquer um desses valores for considerado verdadeiro. | ANY | Sim | 1 ou mais valores |

**Observação:** O nó aceita no mínimo 1 valor de entrada. Você pode adicionar mais entradas conforme necessário usando o recurso de expansão automática.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `BOOLEAN` | Retorna `true` se qualquer um dos valores de entrada for considerado verdadeiro; retorna `false` se todos os valores de entrada forem considerados falsos. | BOOLEAN |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyOrNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f673aa2b0d754f55c51ba9c9ceea7d9de9a21d2e7308bd1281b4d4461243e4ad`
