> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexReplace/pt-BR.md)

O nó RegexReplace localiza e substitui texto em strings usando padrões de expressões regulares. Ele permite que você busque por padrões de texto e os substitua por novos textos, com opções para controlar como a correspondência de padrões funciona, incluindo sensibilidade a maiúsculas/minúsculas, correspondência em múltiplas linhas e limitar o número de substituições.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Sim | - | A string de texto de entrada na qual será feita a busca e substituição |
| `regex_pattern` | STRING | Sim | - | O padrão de expressão regular a ser buscado na string de entrada |
| `replace` | STRING | Sim | - | O texto de substituição para ser colocado no lugar dos padrões correspondidos |
| `case_insensitive` | BOOLEAN | Não | - | Quando ativado, faz a correspondência de padrões ignorar diferenças entre maiúsculas e minúsculas (padrão: Verdadeiro) |
| `multiline` | BOOLEAN | Não | - | Quando ativado, altera o comportamento de ^ e $ para corresponder ao início/fim de cada linha, em vez de apenas ao início/fim de toda a string (padrão: Falso) |
| `dotall` | BOOLEAN | Não | - | Quando ativado, o caractere ponto (.) corresponderá a qualquer caractere, incluindo caracteres de nova linha. Quando desativado, pontos não correspondem a novas linhas (padrão: Falso) |
| `count` | INT | Não | 0-100 | Número máximo de substituições a serem feitas. Defina como 0 para substituir todas as ocorrências (padrão). Defina como 1 para substituir apenas a primeira correspondência, 2 para as duas primeiras, etc. (padrão: 0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | STRING | A string modificada com as substituições especificadas aplicadas |
