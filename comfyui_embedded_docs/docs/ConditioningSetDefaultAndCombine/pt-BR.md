> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetDefaultAndCombine/pt-BR.md)

Este nó combina dados de condicionamento com dados de condicionamento padrão usando um sistema baseado em hooks. Ele recebe uma entrada de condicionamento primária e uma entrada de condicionamento padrão, e então as mescla de acordo com a configuração de hook especificada. O resultado é uma única saída de condicionamento que incorpora ambas as fontes.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `cond` | CONDITIONING | Obrigatório | - | - | A entrada de condicionamento primária a ser processada |
| `cond_DEFAULT` | CONDITIONING | Obrigatório | - | - | Os dados de condicionamento padrão a serem combinados com o condicionamento primário |
| `hooks` | HOOKS | Opcional | - | - | Configuração opcional de hooks que controla como os dados de condicionamento são processados e combinados |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Os dados de condicionamento combinados resultantes da fusão das entradas de condicionamento primária e padrão |
