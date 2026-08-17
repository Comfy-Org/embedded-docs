# AutogrowPrefixTestNode

O `AutogrowPrefixTestNode` é um nó lógico projetado para testar o recurso de entrada autogrow. Ele aceita um número dinâmico de entradas float, combina seus valores em uma string separada por vírgulas e fornece essa string como saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `autogrow` | Um grupo de entrada dinâmico que aceita valores float. O grupo pode conter entre 1 e 10 entradas float, e o nó processa todos os valores fornecidos. | FLOAT | Sim | 1 a 10 entradas |

**Nota:** A entrada `autogrow` é uma entrada dinâmica especial que pode ser expandida para adicionar mais entradas float até o máximo de 10. O mínimo é 1 entrada. Os valores `min` e `max` neste nó definem o número permitido de entradas no grupo, e não o intervalo de valores de cada float individual.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | Uma única string contendo todos os valores float de entrada, separados por vírgulas. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9b815f59961a4c661815f44b9c78e15e9084db1e4be89d502b9d92438f18e70b`
