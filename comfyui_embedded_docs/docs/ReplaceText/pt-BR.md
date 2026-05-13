> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceText/pt-BR.md)

O nó Replace Text realiza uma substituição simples de texto. Ele procura por um trecho de texto específico dentro da entrada e substitui cada ocorrência por um novo trecho de texto. A operação é aplicada a todas as entradas de texto fornecidas ao nó.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `text` | STRING | Sim | - | O texto a ser processado. |
| `find` | STRING | Sim | - | Texto a ser encontrado (padrão: string vazia). |
| `replace` | STRING | Sim | - | Texto para substituir (padrão: string vazia). |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `text` | STRING | O texto processado com todas as ocorrências do texto `find` substituídas pelo texto `replace`. |

---
**Source fingerprint (SHA-256):** `e9d4681e638c5ca2732ec254282243e9e9cdd01cc985af8bbfa41dea208cb7dd`
