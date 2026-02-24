> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ScaleROPE/pt-BR.md)

O nó ScaleROPE permite modificar o Embedding de Posição Rotacional (ROPE) de um modelo aplicando fatores de escala e deslocamento separados aos seus componentes X, Y e T (tempo). Este é um nó experimental avançado usado para ajustar o comportamento de codificação posicional do modelo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo cujos parâmetros ROPE serão modificados. |
| `scale_x` | FLOAT | Não | 0.0 - 100.0 | O fator de escala a ser aplicado ao componente X do ROPE (padrão: 1.0). |
| `shift_x` | FLOAT | Não | -256.0 - 256.0 | O valor de deslocamento a ser aplicado ao componente X do ROPE (padrão: 0.0). |
| `scale_y` | FLOAT | Não | 0.0 - 100.0 | O fator de escala a ser aplicado ao componente Y do ROPE (padrão: 1.0). |
| `shift_y` | FLOAT | Não | -256.0 - 256.0 | O valor de deslocamento a ser aplicado ao componente Y do ROPE (padrão: 0.0). |
| `scale_t` | FLOAT | Não | 0.0 - 100.0 | O fator de escala a ser aplicado ao componente T (tempo) do ROPE (padrão: 1.0). |
| `shift_t` | FLOAT | Não | -256.0 - 256.0 | O valor de deslocamento a ser aplicado ao componente T (tempo) do ROPE (padrão: 0.0). |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo com os novos parâmetros de escala e deslocamento do ROPE aplicados. |
