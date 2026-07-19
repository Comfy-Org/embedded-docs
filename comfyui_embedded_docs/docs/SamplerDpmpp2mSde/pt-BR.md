# SamplerDpmpp2mSde

Este nó foi projetado para gerar um amostrador para o modelo DPMPP_2M_SDE, permitindo a criação de amostras com base em tipos de solucionador especificados, níveis de ruído e preferências de dispositivo computacional. Ele abstrai as complexidades da configuração do amostrador, fornecendo uma interface simplificada para gerar amostras com configurações personalizadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `solver_type` | Especifica o tipo de solucionador a ser usado no processo de amostragem, oferecendo opções entre 'midpoint' e 'heun'. Esta escolha influencia o método de integração numérica aplicado durante a amostragem. | COMBO[STRING] |
| `eta` | Determina o tamanho do passo na integração numérica, afetando a granularidade do processo de amostragem. Um valor maior indica um tamanho de passo maior. | `FLOAT` |
| `s_noise` | Controla o nível de ruído introduzido durante o processo de amostragem, influenciando a variabilidade das amostras geradas. | `FLOAT` |
| `noise_device` | Indica o dispositivo computacional ('gpu' ou 'cpu') no qual o processo de geração de ruído é executado, afetando o desempenho e a eficiência. | COMBO[STRING] |

## Saídas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `sampler` | A saída é um amostrador configurado de acordo com os parâmetros especificados, pronto para gerar amostras. | `SAMPLER` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDpmpp2mSde/pt-BR.md)
