> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VPScheduler/pt-BR.md)

O nó VPScheduler foi projetado para gerar uma sequência de níveis de ruído (sigmas) com base no método de agendamento de Preservação de Variância (VP). Essa sequência é crucial para orientar o processo de remoção de ruído em modelos de difusão, permitindo a geração controlada de imagens ou outros tipos de dados.

## Entradas

| Parâmetro   | Tipo de Dado | Descrição                                                                                                                                      |
|-------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| `steps`     | INT           | Especifica o número de etapas no processo de difusão, afetando a granularidade dos níveis de ruído gerados.                              |
| `beta_d`    | FLOAT         | Determina a distribuição geral do nível de ruído, influenciando a variância dos níveis de ruído gerados.                                 |
| `beta_min`  | FLOAT         | Define o limite mínimo para o nível de ruído, garantindo que o ruído não fique abaixo de um determinado patamar.                              |
| `eps_s`     | FLOAT         | Ajusta o valor épsilon inicial, refinando o nível de ruído inicial no processo de difusão.                                    |

## Saídas

| Parâmetro   | Tipo de Dado | Descrição                                                                                   |
|-------------|---------------|---------------------------------------------------------------------------------------------|
| `sigmas`    | SIGMAS        | Uma sequência de níveis de ruído (sigmas) gerada com base no método de agendamento VP, usada para orientar o processo de remoção de ruído em modelos de difusão. |