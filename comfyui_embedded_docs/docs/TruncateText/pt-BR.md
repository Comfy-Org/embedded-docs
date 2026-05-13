> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TruncateText/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TruncateText/en.md)

Este nó encurta um texto cortando-o em um comprimento máximo especificado. Ele recebe qualquer texto de entrada e retorna apenas a primeira parte, até o número de caracteres que você definir. É uma forma simples de garantir que o texto não ultrapasse um determinado tamanho.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `text` | STRING | Sim | N/A | A string de texto a ser truncada. |
| `comprimento_máximo` | INT | Sim | 1 a 10000 | Comprimento máximo do texto. O texto será cortado após esse número de caracteres (padrão: 77). |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `string` | STRING | O texto truncado, contendo apenas os primeiros `comprimento_máximo` caracteres da entrada. |

---
**Source fingerprint (SHA-256):** `271a77a910967c4fd86a07485449679fb8db89f6b3f2bf0a8fa2ff224ea2f7b2`
