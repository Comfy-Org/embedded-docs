> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexExtract/pt-BR.md)

O nó RegexExtract busca por padrões em texto usando expressões regulares. Ele pode encontrar a primeira correspondência, todas as correspondências, grupos específicos das correspondências ou todos os grupos entre múltiplas correspondências. O nó suporta várias flags de regex para sensibilidade a maiúsculas/minúsculas, correspondência em múltiplas linhas e comportamento dotall.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Sim | - | O texto de entrada no qual buscar os padrões |
| `regex_pattern` | STRING | Sim | - | O padrão de expressão regular a ser buscado |
| `mode` | COMBO | Sim | "First Match"<br>"All Matches"<br>"First Group"<br>"All Groups" | O modo de extração determina quais partes das correspondências são retornadas |
| `case_insensitive` | BOOLEAN | Não | - | Se deve ignorar maiúsculas/minúsculas ao fazer a correspondência (padrão: Verdadeiro) |
| `multiline` | BOOLEAN | Não | - | Se deve tratar a string como múltiplas linhas (padrão: Falso) |
| `dotall` | BOOLEAN | Não | - | Se o ponto (.) deve corresponder a quebras de linha (padrão: Falso) |
| `group_index` | INT | Não | 0-100 | O índice do grupo de captura a extrair ao usar os modos de grupo (padrão: 1) |

**Observação:** Ao usar os modos "First Group" ou "All Groups", o parâmetro `group_index` especifica qual grupo de captura extrair. O grupo 0 representa a correspondência inteira, enquanto os grupos 1+ representam os grupos de captura numerados no seu padrão de regex.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | STRING | O texto extraído com base no modo e parâmetros selecionados |
