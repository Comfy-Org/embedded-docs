> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringReplace/pt-BR.md)

O nó StringReplace realiza operações de substituição de texto em strings de entrada. Ele busca por uma substring especificada dentro do texto de entrada e substitui todas as ocorrências por uma substring diferente. Este nó retorna a string modificada com todas as substituições aplicadas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `string` | STRING | Sim | - | A string de texto de entrada onde as substituições serão realizadas |
| `encontrar` | STRING | Sim | - | A substring a ser procurada dentro do texto de entrada |
| `substituir` | STRING | Sim | - | O texto de substituição que substituirá todas as ocorrências encontradas |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | STRING | A string modificada com todas as ocorrências do texto `encontrar` substituídas pelo texto `substituir` |

---
**Source fingerprint (SHA-256):** `72159dba72261efe9df283c1ea3f789651eade923efdaeb108bacc1d0da663f8`
