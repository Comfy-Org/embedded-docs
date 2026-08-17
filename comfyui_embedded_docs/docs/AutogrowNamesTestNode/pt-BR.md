# AutogrowNamesTestNode

Este nó é um teste para o recurso de entrada Autogrow. Ele recebe um número dinâmico de entradas float, cada uma rotulada com um nome específico, e combina seus valores em uma única string separada por vírgulas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `autogrow` | Um grupo de entradas dinâmico. Você pode adicionar várias entradas float, cada uma com um nome predefinido da lista: "a", "b" ou "c". O nó aceitará qualquer combinação dessas entradas nomeadas. | FLOAT | Sim | N/A |

**Observação:** A entrada `autogrow` é dinâmica. Você pode adicionar ou remover entradas float individuais (chamadas "a", "b" ou "c") conforme necessário para seu fluxo de trabalho. O nó processa todos os valores fornecidos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | Uma única string contendo os valores de todas as entradas float fornecidas, unidos por vírgulas. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `dac384c9486ac645d0d292fc891603cbfa6d362baa0a1e939c43257bbc0b06a0`
