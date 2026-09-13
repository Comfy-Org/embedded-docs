# AutogrowNamesTestNode

Este nó é um teste para o recurso de entrada Autogrow. Ele aceita um grupo dinâmico de entradas do tipo float, cada uma com um nome predefinido, e combina seus valores em uma única string separada por vírgulas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `autogrow` | Um grupo de entrada dinâmico. Você pode adicionar múltiplas entradas float, cada uma com um nome predefinido da lista: "a", "b" ou "c". O nó aceita qualquer combinação dessas entradas nomeadas. | FLOAT | Sim | Slots nomeados: `a`, `b`, `c` |

**Nota:** A entrada `autogrow` é dinâmica. Entradas float individuais chamadas "a", "b" e "c" podem ser adicionadas ou removidas conforme necessário. Todos os valores fornecidos são processados pelo nó.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | Uma única string contendo os valores de todas as entradas float fornecidas, unidos por vírgulas. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `dac384c9486ac645d0d292fc891603cbfa6d362baa0a1e939c43257bbc0b06a0`
