> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/pt-BR.md)

O AutogrowPrefixTestNode é um nó de lógica projetado para testar o recurso de entrada de crescimento automático. Ele aceita um número dinâmico de entradas do tipo float, combina seus valores em uma string separada por vírgulas e retorna essa string.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `autogrow` | AUTOGROW | Sim | 1 a 10 entradas | Um grupo de entrada dinâmico que pode aceitar entre 1 e 10 valores do tipo float. Cada entrada no grupo é do tipo FLOAT. |

**Observação:** A entrada `autogrow` é uma entrada dinâmica especial. Você pode adicionar várias entradas float a este grupo, até um máximo de 10. O nó processará todos os valores fornecidos.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | STRING | Uma única string contendo todos os valores float de entrada, separados por vírgulas. |
