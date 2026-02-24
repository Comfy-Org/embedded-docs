> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/pt-BR.md)

O nó SamplingPercentToSigma converte um valor percentual de amostragem em um valor sigma correspondente usando os parâmetros de amostragem do modelo. Ele recebe um valor percentual entre 0.0 e 1.0 e o mapeia para o valor sigma apropriado no cronograma de ruído do modelo, com opções para retornar o sigma calculado ou os valores sigma máximo/mínimo reais nos limites.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo que contém os parâmetros de amostragem usados para a conversão |
| `sampling_percent` | FLOAT | Sim | 0.0 a 1.0 | A porcentagem de amostragem a ser convertida para sigma (padrão: 0.0) |
| `return_actual_sigma` | BOOLEAN | Sim | - | Retorna o valor sigma real em vez do valor usado para verificações de intervalo. Isso afeta apenas os resultados em 0.0 e 1.0. (padrão: False) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `sigma_value` | FLOAT | O valor sigma convertido correspondente à porcentagem de amostragem de entrada |
