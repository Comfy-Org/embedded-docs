Este nó foi projetado para aprimorar as capacidades de amostragem de um modelo, integrando técnicas contínuas de amostragem EDM (Modelos de Difusão Baseados em Energia). Ele permite o ajuste dinâmico dos níveis de ruído durante o processo de amostragem do modelo, oferecendo um controle mais refinado sobre a qualidade e a diversidade da geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Tipo Python |
| --- | --- | --- | --- |
| `modelo` | O modelo a ser aprimorado com capacidades contínuas de amostragem EDM. Serve como base para a aplicação das técnicas avançadas de amostragem. | `MODEL` | `torch.nn.Module` |
| `amostragem` | Especifica o tipo de amostragem a ser aplicado: 'eps' para amostragem épsilon ou 'v_prediction' para predição de velocidade, influenciando o comportamento do modelo durante o processo de amostragem. | COMBO[STRING] | `str` |
| `sigma_máx` | O valor máximo de sigma para o nível de ruído, permitindo o controle do limite superior no processo de injeção de ruído durante a amostragem. | `FLOAT` | `float` |
| `sigma_mín` | O valor mínimo de sigma para o nível de ruído, definindo o limite inferior para a injeção de ruído, afetando assim a precisão da amostragem do modelo. | `FLOAT` | `float` |

## Saídas

| Parâmetro | Descrição | Tipo de Dado | Tipo Python |
| --- | --- | --- | --- |
| `modelo` | O modelo aprimorado com capacidades contínuas de amostragem EDM integradas, pronto para uso em tarefas de geração. | MODEL | `torch.nn.Module` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousEDM/pt-BR.md)
