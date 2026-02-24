> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/pt-BR.md)

O nó ModelSamplingStableCascade aplica a amostragem estável em cascata a um modelo, ajustando os parâmetros de amostragem com um valor de deslocamento. Ele cria uma versão modificada do modelo de entrada com uma configuração de amostragem personalizada para geração estável em cascata.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo de entrada ao qual será aplicada a amostragem estável em cascata |
| `shift` | FLOAT | Sim | 0.0 - 100.0 | O valor de deslocamento a ser aplicado aos parâmetros de amostragem (padrão: 2.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com a amostragem estável em cascata aplicada |
