> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/pt-BR.md)

O nó FluxKontextMultiReferenceLatentMethod modifica os dados de condicionamento definindo um método específico para os latentes de referência. Ele anexa o método escolhido à entrada de condicionamento, o que afeta como os latentes de referência são processados nas etapas subsequentes de geração. Este nó está marcado como experimental e faz parte do sistema de condicionamento Flux.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | Sim | - | Os dados de condicionamento a serem modificados com o método de latentes de referência |
| `reference_latents_method` | STRING | Sim | `"offset"`<br>`"index"`<br>`"uxo/uno"` | O método a ser usado para o processamento dos latentes de referência. Se "uxo" ou "uso" for selecionado, será convertido para "uxo" |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | Os dados de condicionamento modificados com o método de latentes de referência aplicado |
