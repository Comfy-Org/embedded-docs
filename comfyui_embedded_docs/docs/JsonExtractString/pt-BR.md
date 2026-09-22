# Extrair String do JSON

O nó JsonExtractString examina uma string de texto em busca do primeiro objeto JSON válido e extrai o valor associado a uma chave específica, convertido em uma string. Qualquer texto antes ou depois do objeto JSON é ignorado, então o nó também funciona em blocos de código Markdown e em respostas de modelo que envolvem o JSON em texto adicional. Se nenhum objeto JSON válido for encontrado, se a chave não for encontrada ou se o valor for `null`, o nó retorna uma string vazia.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `json_string` | O texto no qual buscar um objeto JSON. Este campo aceita entrada multilinha e pode conter texto ao redor ou cercas de código Markdown. | STRING | Sim | N/A |
| `key` | A chave específica cujo valor você deseja extrair do objeto JSON. Este campo aceita apenas entrada de linha única. | STRING | Sim | N/A |

**Observação:** O nó extrai valores apenas de objetos JSON (dicionários). Ele tenta cada `{` na entrada em ordem e decodifica a partir da primeira posição que produz um objeto JSON válido, portanto texto inicial ou final é ignorado. Se nenhum objeto JSON puder ser decodificado ou a chave especificada não existir nele, a saída será uma string vazia. Se o valor associado à chave for `null`, o nó também retorna uma string vazia. Valores que não são strings são retornados como sua representação em string.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | O valor de string extraído do JSON para a chave especificada, ou uma string vazia se a extração falhar. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JsonExtractString/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ca697fd3bd2d4de764372470ad1102b345d9d60f6df1c151fa0573e85fab2382`
