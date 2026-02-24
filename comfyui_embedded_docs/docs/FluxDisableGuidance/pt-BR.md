> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/pt-BR.md)

Este nó desabilita completamente a funcionalidade de incorporação de orientação (guidance) para modelos Flux e similares. Ele recebe dados de condicionamento como entrada e remove o componente de orientação definindo-o como None, efetivamente desativando o condicionamento baseado em orientação para o processo de geração.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | Sim | - | Os dados de condicionamento a serem processados e dos quais a orientação será removida |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | Os dados de condicionamento modificados, com a orientação desabilitada |
