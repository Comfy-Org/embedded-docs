> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyOrNode/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyOrNode/en.md)

# ComfyOrNode

O nó ComfyOrNode realiza uma operação lógica OU em um conjunto de valores de entrada. Ele retorna `true` se qualquer um dos valores fornecidos for considerado verdadeiro de acordo com as regras padrão de veracidade do Python.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `value` | ANY | Sim | Múltiplos valores aceitos | Um valor a ser avaliado quanto à veracidade. Você pode fornecer vários valores adicionando mais entradas. O nó retorna `true` se qualquer um desses valores for verdadeiro. |

**Nota:** O nó aceita no mínimo 1 valor de entrada. Você pode adicionar mais entradas conforme necessário usando o recurso de crescimento automático.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `BOOLEAN` | BOOLEAN | Retorna `true` se qualquer um dos valores de entrada for verdadeiro; retorna `false` se todos os valores de entrada forem falsos. |

---
**Source fingerprint (SHA-256):** `00c60d5c80bbddc993af0bcd92e35dc77f153731329c23a6e4e9a980709111b1`
