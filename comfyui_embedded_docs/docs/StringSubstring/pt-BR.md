> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringSubstring/pt-BR.md)

O nó StringSubstring extrai uma parte do texto de uma string maior. Ele usa uma posição inicial e uma posição final para definir a seção que você deseja extrair e retorna o texto entre essas duas posições.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `string` | STRING | Sim | - | A string de texto de entrada para extrair. Suporta texto com múltiplas linhas. |
| `início` | INT | Sim | - | O índice da posição inicial para a substring. O primeiro caractere está no índice 0. |
| `fim` | INT | Sim | - | O índice da posição final para a substring. O caractere neste índice não é incluído no resultado. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | STRING | A substring extraída do texto de entrada, contendo todos os caracteres da posição `início` até (mas não incluindo) a posição `fim`. |

---
**Source fingerprint (SHA-256):** `962d0b19af88b6c95b5c9d374081ecd55ee8cffbfb638de7ed38e6e378b220c5`
