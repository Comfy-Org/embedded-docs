> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexExtract/pt-BR.md)

O nó RegexExtract busca padrões em texto usando expressões regulares. Ele pode encontrar a primeira correspondência, todas as correspondências, grupos específicos das correspondências ou todos os grupos em múltiplas correspondências. O nó suporta várias flags de regex para sensibilidade a maiúsculas/minúsculas, correspondência multilinha e comportamento dotall.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `string` | STRING | Sim | - | O texto de entrada para buscar padrões |
| `regex_pattern` | STRING | Sim | - | O padrão de expressão regular a ser buscado |
| `mode` | COMBO | Sim | "Primeira Correspondência"<br>"Todas as Correspondências"<br>"Primeiro Grupo"<br>"Todos os Grupos" | O modo de extração determina quais partes das correspondências são retornadas (padrão: "Primeira Correspondência") |
| `case_insensitive` | BOOLEAN | Não | - | Se deve ignorar maiúsculas/minúsculas ao corresponder (padrão: Verdadeiro) |
| `multiline` | BOOLEAN | Não | - | Se deve tratar a string como múltiplas linhas (padrão: Falso) |
| `dotall` | BOOLEAN | Não | - | Se o ponto (.) corresponde a quebras de linha (padrão: Falso) |
| `group_index` | INT | Não | 0-100 | O índice do grupo de captura a extrair ao usar modos de grupo (padrão: 1) |

**Nota:** Ao usar os modos "Primeiro Grupo" ou "Todos os Grupos", o parâmetro `group_index` especifica qual grupo de captura extrair. O grupo 0 representa a correspondência inteira, enquanto os grupos 1+ representam os grupos de captura numerados no seu padrão de regex.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | STRING | O texto extraído com base no modo e parâmetros selecionados |

---
**Source fingerprint (SHA-256):** `38e365d21bea966ed65bc78c184766330924fe75392cdb88c6978052037f5d5f`
