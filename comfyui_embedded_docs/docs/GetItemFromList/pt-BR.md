# GetItemFromList

Este nó retorna um único item de uma lista, selecionado por sua posição. Você fornece a lista e o número do índice do item desejado, e o nó retorna esse item. Isso o torna útil para escolher um elemento específico de um grupo de valores, como uma imagem específica de um lote.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `list` | A lista de valores da qual selecionar. Como este nó está marcado como recebendo uma entrada de lista, o valor conectado é tratado como um grupo de itens. | Qualquer tipo | Sim | Qualquer lista de valores |
| `index` | A posição do item a retornar. O valor começa em 0, então `0` retorna o primeiro item, `1` retorna o segundo item, e assim por diante (padrão: 0). | INT | Sim | Qualquer índice inteiro |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `OUTPUT` | O item único localizado no `index` fornecido dentro da `list` fornecida. | Qualquer tipo |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetItemFromList/pt-BR.md)

---
**Source fingerprint (SHA-256):** `11c1c90fed0e29f1110b4c1dda64d60797aff38d7f3af69f76b74e94fe94e976`
