# Truncar Texto

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TruncateText/en.md)

Este nó encurta um texto cortando-o em um comprimento máximo especificado. Ele recebe qualquer texto de entrada e retorna apenas a primeira parte, até o número de caracteres que você definir. É uma forma simples de garantir que o texto não ultrapasse um determinado tamanho.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `text` | A string de texto a ser truncada. | STRING | Sim | N/A |
| `comprimento_máximo` | Comprimento máximo do texto. O texto será cortado após esse número de caracteres (padrão: 77). | INT | Sim | 1 a 10000 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `string` | O texto truncado, contendo apenas os primeiros `comprimento_máximo` caracteres da entrada. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TruncateText/pt-BR.md)

---
**Source fingerprint (SHA-256):** `271a77a910967c4fd86a07485449679fb8db89f6b3f2bf0a8fa2ff224ea2f7b2`
