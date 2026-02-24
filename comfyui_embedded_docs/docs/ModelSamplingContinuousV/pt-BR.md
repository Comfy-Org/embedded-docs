> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/pt-BR.md)

O nó ModelSamplingContinuousV modifica o comportamento de amostragem de um modelo aplicando parâmetros de amostragem de predição V contínua. Ele cria um clone do modelo de entrada e o configura com definições personalizadas de faixa de sigma para um controle avançado da amostragem. Isso permite que os usuários ajustem finamente o processo de amostragem com valores de sigma mínimo e máximo específicos.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo de entrada a ser modificado com a amostragem de predição V contínua |
| `sampling` | STRING | Sim | "v_prediction" | O método de amostragem a ser aplicado (atualmente apenas a predição V é suportada) |
| `sigma_max` | FLOAT | Sim | 0.0 - 1000.0 | O valor máximo de sigma para a amostragem (padrão: 500.0) |
| `sigma_min` | FLOAT | Sim | 0.0 - 1000.0 | O valor mínimo de sigma para a amostragem (padrão: 0.03) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com a amostragem de predição V contínua aplicada |
