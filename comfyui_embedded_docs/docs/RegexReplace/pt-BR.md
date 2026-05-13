> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexReplace/pt-BR.md)

O nó RegexReplace localiza e substitui texto em strings usando padrões de expressões regulares. Ele permite que você pesquise padrões de texto e os substitua por novo texto, com opções para controlar como a correspondência de padrões funciona, incluindo diferenciação entre maiúsculas e minúsculas, correspondência em várias linhas e limitação do número de substituições.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `string` | STRING | Sim | - | A string de texto de entrada para pesquisar e substituir |
| `regex_pattern` | STRING | Sim | - | O padrão de expressão regular para pesquisar na string de entrada |
| `replace` | STRING | Sim | - | O texto de substituição para substituir os padrões correspondentes |
| `case_insensitive` | BOOLEAN | Não | - | Quando ativado, faz com que a correspondência de padrões ignore diferenças entre maiúsculas e minúsculas (padrão: Verdadeiro) |
| `multiline` | BOOLEAN | Não | - | Quando ativado, altera o comportamento de ^ e $ para corresponder ao início/fim de cada linha, em vez de apenas ao início/fim de toda a string (padrão: Falso) |
| `dotall` | BOOLEAN | Não | - | Quando ativado, o caractere ponto (.) corresponderá a qualquer caractere, incluindo caracteres de nova linha. Quando desativado, os pontos não corresponderão a novas linhas (padrão: Falso) |
| `count` | INT | Não | 0-100 | Número máximo de substituições a serem feitas. Defina como 0 para substituir todas as ocorrências (padrão). Defina como 1 para substituir apenas a primeira correspondência, 2 para as duas primeiras correspondências, etc. (padrão: 0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | STRING | A string modificada com as substituições especificadas aplicadas |

---
**Source fingerprint (SHA-256):** `4a4d4b317ee23314a4ac26cf3b58a2cc904bfb8111608f88345c1014b801ea00`
