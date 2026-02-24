> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/pt-BR.md)

O nó ModelSamplingSD3 aplica os parâmetros de amostragem do Stable Diffusion 3 a um modelo. Ele modifica o comportamento de amostragem do modelo ajustando o parâmetro de deslocamento, que controla as características da distribuição de amostragem. O nó cria uma cópia modificada do modelo de entrada com a configuração de amostragem especificada aplicada.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo de entrada ao qual aplicar os parâmetros de amostragem SD3 |
| `shift` | FLOAT | Sim | 0.0 - 100.0 | Controla o parâmetro de deslocamento da amostragem (padrão: 3.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com os parâmetros de amostragem SD3 aplicados |
