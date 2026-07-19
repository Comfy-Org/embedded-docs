# AutogrowNamesTestNode

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/en.md)

Este nó é um teste para a funcionalidade de entrada Autogrow. Ele recebe um número dinâmico de entradas do tipo float, cada uma rotulada com um nome específico, e combina seus valores em uma única string separada por vírgulas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `autogrow` | Um grupo de entrada dinâmico. Você pode adicionar várias entradas float, cada uma com um nome predefinido da lista: "a", "b" ou "c". O nó aceitará qualquer combinação dessas entradas nomeadas. | FLOAT | Sim | N/A |

**Nota:** A entrada `autogrow` é dinâmica. Você pode adicionar ou remover entradas float individuais (nomeadas como "a", "b" ou "c") conforme necessário para seu fluxo de trabalho. O nó processa todos os valores fornecidos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | Uma única string contendo os valores de todas as entradas float fornecidas, unidos por vírgulas. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `33e8b2e2c369d06979415c31ef2623cff55d98ecf49137c5cafbeba7cc3b0451`
