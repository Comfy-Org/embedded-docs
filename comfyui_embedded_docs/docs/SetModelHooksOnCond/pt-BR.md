> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetModelHooksOnCond/pt-BR.md)

Este nó anexa ganchos personalizados aos dados de condicionamento, permitindo que você intercepte e modifique o processo de condicionamento durante a execução do modelo. Ele recebe um conjunto de ganchos e os aplica aos dados de condicionamento fornecidos, possibilitando uma personalização avançada do fluxo de trabalho de geração de texto para imagem. O condicionamento modificado com os ganchos anexados é então retornado para uso nas etapas subsequentes de processamento.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | Sim | - | Os dados de condicionamento aos quais os ganchos serão anexados |
| `hooks` | HOOKS | Sim | - | As definições dos ganchos que serão aplicadas aos dados de condicionamento |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | Os dados de condicionamento modificados com os ganchos anexados |
