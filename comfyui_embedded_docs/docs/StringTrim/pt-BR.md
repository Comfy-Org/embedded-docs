> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringTrim/pt-BR.md)

O nó StringTrim remove caracteres de espaço em branco do início, fim ou ambos os lados de uma string de texto. Você pode escolher aparar pelo lado esquerdo, direito ou ambos os lados da string. Isso é útil para limpar entradas de texto, removendo espaços, tabulações ou quebras de linha indesejados.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `string` | STRING | Sim | - | A string de texto a ser processada. Suporta entrada multilinha. |
| `modo` | COMBO | Sim | "Both"<br>"Left"<br>"Right" | Especifica qual(is) lado(s) da string deve(m) ser aparado(s). "Both" remove espaços em branco de ambas as extremidades, "Left" remove apenas do início, "Right" remove apenas do final. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | STRING | A string de texto aparada, com espaços em branco removidos de acordo com o modo selecionado. |

---
**Source fingerprint (SHA-256):** `29b4da100373585af8a672ccfbd4c0b597705c1d8c176b2f88f3e878c1192460`
