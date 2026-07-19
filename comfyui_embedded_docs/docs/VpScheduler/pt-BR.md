# VPScheduler

O nó VPScheduler foi projetado para gerar uma sequência de níveis de ruído (sigmas) com base no método de agendamento de Preservação de Variância (VP). Essa sequência é crucial para orientar o processo de remoção de ruído em modelos de difusão, permitindo a geração controlada de imagens ou outros tipos de dados.

## Entradas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `etapas` | Especifica o número de etapas no processo de difusão, afetando a granularidade dos níveis de ruído gerados. | INT |
| `beta_d` | Determina a distribuição geral do nível de ruído, influenciando a variância dos níveis de ruído gerados. | FLOAT |
| `beta_min` | Define o limite mínimo para o nível de ruído, garantindo que o ruído não fique abaixo de um determinado patamar. | FLOAT |
| `eps_s` | Ajusta o valor épsilon inicial, refinando o nível de ruído inicial no processo de difusão. | FLOAT |

## Saídas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `sigmas` | Uma sequência de níveis de ruído (sigmas) gerada com base no método de agendamento VP, usada para orientar o processo de remoção de ruído em modelos de difusão. | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VPScheduler/pt-BR.md)
