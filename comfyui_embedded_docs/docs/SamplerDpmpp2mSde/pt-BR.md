> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDpmpp2mSde/pt-BR.md)

Este nó foi projetado para gerar um amostrador para o modelo DPMPP_2M_SDE, permitindo a criação de amostras com base em tipos de solucionador, níveis de ruído e preferências de dispositivo de computação especificados. Ele abstrai as complexidades da configuração do amostrador, fornecendo uma interface simplificada para gerar amostras com configurações personalizadas.

## Entradas

| Parâmetro       | Tipo de Dados | Descrição                                                                 |
|-----------------|---------------|---------------------------------------------------------------------------|
| `solver_type`   | COMBO[STRING] | Especifica o tipo de solucionador a ser usado no processo de amostragem, oferecendo opções entre 'midpoint' e 'heun'. Esta escolha influencia o método de integração numérica aplicado durante a amostragem. |
| `eta`           | `FLOAT`       | Determina o tamanho do passo na integração numérica, afetando a granularidade do processo de amostragem. Um valor mais alto indica um tamanho de passo maior. |
| `s_noise`       | `FLOAT`       | Controla o nível de ruído introduzido durante o processo de amostragem, influenciando a variabilidade das amostras geradas. |
| `noise_device`  | COMBO[STRING] | Indica o dispositivo de computação ('gpu' ou 'cpu') no qual o processo de geração de ruído é executado, afetando o desempenho e a eficiência. |

## Saídas

| Parâmetro       | Tipo de Dados | Descrição                                                                 |
|-----------------|---------------|---------------------------------------------------------------------------|
| `sampler`       | `SAMPLER`     | A saída é um amostrador configurado de acordo com os parâmetros especificados, pronto para gerar amostras. |
