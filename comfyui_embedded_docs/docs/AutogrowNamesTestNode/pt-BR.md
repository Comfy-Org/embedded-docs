> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/pt-BR.md)

Este nó é um teste para o recurso de entrada Autogrow. Ele aceita um número dinâmico de entradas do tipo FLOAT, cada uma rotulada com um nome específico, e combina seus valores em uma única string separada por vírgulas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `autogrow` | FLOAT | Sim | N/A | Um grupo de entrada dinâmico. Você pode adicionar múltiplas entradas do tipo FLOAT, cada uma com um nome predefinido da lista: "a", "b" ou "c". O nó aceitará qualquer combinação dessas entradas nomeadas. |

**Observação:** A entrada `autogrow` é dinâmica. Você pode adicionar ou remover entradas individuais do tipo FLOAT (nomeadas como "a", "b" ou "c") conforme necessário para o seu fluxo de trabalho. O nó processa todos os valores fornecidos.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | STRING | Uma única string contendo os valores de todas as entradas FLOAT fornecidas, unidos por vírgulas. |
