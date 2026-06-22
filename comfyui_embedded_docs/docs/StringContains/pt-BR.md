# Contém

O nó StringContains verifica se uma determinada string contém uma substring especificada. Ele pode realizar essa verificação com correspondência sensível a maiúsculas/minúsculas ou insensível, retornando um resultado booleano indicando se a substring foi encontrada dentro da string principal.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `string` | A string de texto principal a ser pesquisada | STRING | Sim | - |
| `substring` | O texto a ser procurado dentro da string principal | STRING | Sim | - |
| `diferenciar_maiusculas_minusculas` | Determina se a pesquisa deve ser sensível a maiúsculas/minúsculas (padrão: verdadeiro) | BOOLEAN | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `contains` | Retorna verdadeiro se a substring for encontrada na string, falso caso contrário | BOOLEAN |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringContains/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ef7329ca8586e0f894306d93835490edb948a346db1e0cb011e4da5a6fe44202`
