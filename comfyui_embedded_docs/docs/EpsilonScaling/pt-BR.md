Implementa o método de Escalonamento Epsilon (Epsilon Scaling) do artigo de pesquisa "Elucidating the Exposure Bias in Diffusion Models." Este método melhora a qualidade das amostras ao escalonar o ruído previsto durante o processo de amostragem. Ele utiliza um agendamento uniforme para mitigar o viés de exposição em modelos de difusão.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo ao qual aplicar o escalonamento epsilon | MODEL | Sim | - |
| `scaling_factor` | O fator usado para escalonar o ruído previsto (padrão: 1.005) | FLOAT | Não | 0.5 - 1.5 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo com o escalonamento epsilon aplicado | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EpsilonScaling/pt-BR.md)
