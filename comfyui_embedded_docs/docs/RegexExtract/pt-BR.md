O nó RegexExtract busca padrões em texto usando expressões regulares. Ele pode encontrar a primeira correspondência, todas as correspondências, grupos específicos das correspondências ou todos os grupos em múltiplas correspondências. O nó suporta várias flags de regex para sensibilidade a maiúsculas/minúsculas, correspondência multilinha e comportamento dotall.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `string` | O texto de entrada para buscar padrões | STRING | Sim | - |
| `regex_pattern` | O padrão de expressão regular a ser buscado | STRING | Sim | - |
| `modo` | O modo de extração determina quais partes das correspondências são retornadas (padrão: "Primeira Correspondência") | COMBO | Sim | "Primeira Correspondência"<br>"Todas as Correspondências"<br>"Primeiro Grupo"<br>"Todos os Grupos" |
| `ignorar_maiusculas_minusculas` | Se deve ignorar maiúsculas/minúsculas ao corresponder (padrão: Verdadeiro) | BOOLEAN | Não | - |
| `multilinha` | Se deve tratar a string como múltiplas linhas (padrão: Falso) | BOOLEAN | Não | - |
| `dotall` | Se o ponto (.) corresponde a quebras de linha (padrão: Falso) | BOOLEAN | Não | - |
| `indice_grupo` | O índice do grupo de captura a extrair ao usar modos de grupo (padrão: 1) | INT | Não | 0-100 |

**Nota:** Ao usar os modos "Primeiro Grupo" ou "Todos os Grupos", o parâmetro `group_index` especifica qual grupo de captura extrair. O grupo 0 representa a correspondência inteira, enquanto os grupos 1+ representam os grupos de captura numerados no seu padrão de regex.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O texto extraído com base no modo e parâmetros selecionados | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexExtract/pt-BR.md)

---
**Source fingerprint (SHA-256):** `38e365d21bea966ed65bc78c184766330924fe75392cdb88c6978052037f5d5f`
