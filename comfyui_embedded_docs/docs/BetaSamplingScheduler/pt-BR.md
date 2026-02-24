> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BetaSamplingScheduler/pt-BR.md)

O nó BetaSamplingScheduler gera uma sequência de níveis de ruído (sigmas) para o processo de amostragem usando um algoritmo de agendamento beta. Ele recebe um modelo e parâmetros de configuração para criar um cronograma de ruído personalizado que controla o processo de remoção de ruído durante a geração de imagem. Este agendador permite o ajuste fino da trajetória de redução de ruído através dos parâmetros alfa e beta.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | Obrigatório | - | - | O modelo usado para amostragem, que fornece o objeto de amostragem do modelo |
| `steps` | INT | Obrigatório | 20 | 1-10000 | O número de etapas de amostragem para as quais gerar os sigmas |
| `alpha` | FLOAT | Obrigatório | 0.6 | 0.0-50.0 | Parâmetro alfa para o agendador beta, controlando a curva de agendamento |
| `beta` | FLOAT | Obrigatório | 0.6 | 0.0-50.0 | Parâmetro beta para o agendador beta, controlando a curva de agendamento |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `SIGMAS` | SIGMAS | Uma sequência de níveis de ruído (sigmas) usados para o processo de amostragem |
