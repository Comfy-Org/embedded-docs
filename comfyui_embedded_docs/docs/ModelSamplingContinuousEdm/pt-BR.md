> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousEDM/pt-BR.md)

Este nó foi projetado para aprimorar as capacidades de amostragem de um modelo, integrando técnicas contínuas de amostragem EDM (Modelos de Difusão Baseados em Energia). Ele permite o ajuste dinâmico dos níveis de ruído durante o processo de amostragem do modelo, oferecendo um controle mais refinado sobre a qualidade e a diversidade da geração.

## Entradas

| Parâmetro   | Tipo de Dado | Tipo Python        | Descrição |
|-------------|--------------|----------------------|-------------|
| `model`     | `MODEL`     | `torch.nn.Module`   | O modelo a ser aprimorado com capacidades contínuas de amostragem EDM. Serve como base para a aplicação das técnicas avançadas de amostragem. |
| `sampling`  | COMBO[STRING] | `str`             | Especifica o tipo de amostragem a ser aplicado: 'eps' para amostragem épsilon ou 'v_prediction' para predição de velocidade, influenciando o comportamento do modelo durante o processo de amostragem. |
| `sigma_max` | `FLOAT`     | `float`             | O valor máximo de sigma para o nível de ruído, permitindo o controle do limite superior no processo de injeção de ruído durante a amostragem. |
| `sigma_min` | `FLOAT`     | `float`             | O valor mínimo de sigma para o nível de ruído, definindo o limite inferior para a injeção de ruído, afetando assim a precisão da amostragem do modelo. |

## Saídas

| Parâmetro | Tipo de Dado | Tipo Python        | Descrição |
|-----------|-------------|----------------------|-------------|
| `model`   | MODEL     | `torch.nn.Module`   | O modelo aprimorado com capacidades contínuas de amostragem EDM integradas, pronto para uso em tarefas de geração. |