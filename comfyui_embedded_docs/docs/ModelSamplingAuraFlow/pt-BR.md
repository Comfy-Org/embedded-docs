> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/pt-BR.md)

O nó ModelSamplingAuraFlow aplica uma configuração de amostragem especializada a modelos de difusão, projetada especificamente para arquiteturas de modelo AuraFlow. Ele modifica o comportamento de amostragem do modelo aplicando um parâmetro de deslocamento que ajusta a distribuição de amostragem. Este nó herda da estrutura de amostragem de modelo SD3 e fornece controle refinado sobre o processo de amostragem.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo de difusão ao qual aplicar a configuração de amostragem AuraFlow |
| `shift` | FLOAT | Sim | 0.0 - 100.0 | O valor de deslocamento a ser aplicado à distribuição de amostragem (padrão: 1.73) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com a configuração de amostragem AuraFlow aplicada |
