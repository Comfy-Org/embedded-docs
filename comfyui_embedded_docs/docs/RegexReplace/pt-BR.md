# Substituir por Regex

O nó RegexReplace localiza e substitui texto em strings usando padrões de expressões regulares. Ele permite que você pesquise padrões de texto e os substitua por novo texto, com opções para controlar como a correspondência de padrões funciona, incluindo diferenciação entre maiúsculas e minúsculas, correspondência em várias linhas e limitação do número de substituições.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `string` | A string de texto de entrada para pesquisar e substituir | STRING | Sim | - |
| `regex_pattern` | O padrão de expressão regular para pesquisar na string de entrada | STRING | Sim | - |
| `substituir` | O texto de substituição para substituir os padrões correspondentes | STRING | Sim | - |
| `ignorar_maiusculas_minusculas` | Quando ativado, faz com que a correspondência de padrões ignore diferenças entre maiúsculas e minúsculas (padrão: Verdadeiro) | BOOLEAN | Não | - |
| `multilinha` | Quando ativado, altera o comportamento de ^ e $ para corresponder ao início/fim de cada linha, em vez de apenas ao início/fim de toda a string (padrão: Falso) | BOOLEAN | Não | - |
| `dotall` | Quando ativado, o caractere ponto (.) corresponderá a qualquer caractere, incluindo caracteres de nova linha. Quando desativado, os pontos não corresponderão a novas linhas (padrão: Falso) | BOOLEAN | Não | - |
| `quantidade` | Número máximo de substituições a serem feitas. Defina como 0 para substituir todas as ocorrências (padrão). Defina como 1 para substituir apenas a primeira correspondência, 2 para as duas primeiras correspondências, etc. (padrão: 0) | INT | Não | 0-100 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A string modificada com as substituições especificadas aplicadas | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexReplace/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4a4d4b317ee23314a4ac26cf3b58a2cc904bfb8111608f88345c1014b801ea00`
