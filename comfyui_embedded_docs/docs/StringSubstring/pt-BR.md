O nó StringSubstring extrai uma parte do texto de uma string maior. Ele usa uma posição inicial e uma posição final para definir a seção que você deseja extrair e retorna o texto entre essas duas posições.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `string` | A string de texto de entrada para extrair. Suporta texto com múltiplas linhas. | STRING | Sim | - |
| `início` | O índice da posição inicial para a substring. O primeiro caractere está no índice 0. | INT | Sim | - |
| `fim` | O índice da posição final para a substring. O caractere neste índice não é incluído no resultado. | INT | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A substring extraída do texto de entrada, contendo todos os caracteres da posição `início` até (mas não incluindo) a posição `fim`. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringSubstring/pt-BR.md)

---
**Source fingerprint (SHA-256):** `962d0b19af88b6c95b5c9d374081ecd55ee8cffbfb638de7ed38e6e378b220c5`
