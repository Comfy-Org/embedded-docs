> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingDiscrete/pt-BR.md)

Este nó foi projetado para modificar o comportamento de amostragem de um modelo aplicando uma estratégia de amostragem discreta. Ele permite a seleção de diferentes métodos de amostragem, como epsilon, v_prediction, lcm ou x0, e opcionalmente ajusta a estratégia de redução de ruído do modelo com base na configuração da razão de ruído zero-shot (zsnr).

## Entradas

| Parâmetro | Tipo de Dados | Python dtype     | Descrição |
|-----------|--------------|-------------------|-------------|
| `model`   | MODEL     | `torch.nn.Module` | O modelo ao qual a estratégia de amostragem discreta será aplicada. Este parâmetro é crucial, pois define o modelo base que passará pela modificação. |
| `sampling`| COMBO[STRING] | `str`           | Especifica o método de amostragem discreta a ser aplicado ao modelo. A escolha do método afeta a forma como o modelo gera amostras, oferecendo diferentes estratégias para a amostragem. |
| `zsnr`    | `BOOLEAN`   | `bool`           | Um sinalizador booleano que, quando ativado, ajusta a estratégia de redução de ruído do modelo com base na razão de ruído zero-shot. Isso pode influenciar a qualidade e as características das amostras geradas. |

## Saídas

| Parâmetro | Tipo de Dados | Python dtype     | Descrição |
|-----------|-------------|-------------------|-------------|
| `model`   | MODEL     | `torch.nn.Module` | O modelo modificado com a estratégia de amostragem discreta aplicada. Este modelo agora está equipado para gerar amostras usando o método e os ajustes especificados. |
