> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CustomCombo/pt-BR.md)

O nó Custom Combo permite que você crie um menu suspenso personalizado com sua própria lista de opções de texto. É um nó focado no frontend que fornece uma representação no backend para garantir compatibilidade dentro do seu fluxo de trabalho. Quando você seleciona uma opção no menu suspenso, o nó emite esse texto como uma string.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `choice` | COMBO | Sim | Definido pelo usuário | A opção de texto selecionada no menu suspenso personalizado. A lista de opções disponíveis é definida pelo usuário na interface de frontend do nó. |

**Observação:** A validação para a entrada deste nó está intencionalmente desativada. Isso permite que você defina quaisquer opções de texto personalizadas que desejar no frontend, sem que o backend verifique se sua seleção é de uma lista predefinida.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | STRING | A string de texto da opção selecionada na caixa de combinação personalizada. |
