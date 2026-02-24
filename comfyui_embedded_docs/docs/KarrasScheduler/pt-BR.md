> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KarrasScheduler/pt-BR.md)

O nó KarrasScheduler é projetado para gerar uma sequência de níveis de ruído (sigmas) com base no agendamento de ruído de Karras et al. (2022). Este agendador é útil para controlar o processo de difusão em modelos generativos, permitindo ajustes refinados dos níveis de ruído aplicados em cada etapa do processo de geração.

## Entradas

| Parâmetro   | Tipo de Dados | Descrição                                                                                      |
|-------------|-------------|------------------------------------------------------------------------------------------------|
| `steps`     | INT         | Especifica o número de etapas no agendamento de ruído, afetando a granularidade da sequência de sigmas gerada. |
| `sigma_max` | FLOAT       | O valor máximo de sigma no agendamento de ruído, definindo o limite superior dos níveis de ruído.                    |
| `sigma_min` | FLOAT       | O valor mínimo de sigma no agendamento de ruído, definindo o limite inferior dos níveis de ruído.                    |
| `rho`       | FLOAT       | Um parâmetro que controla a forma da curva do agendamento de ruído, influenciando como os níveis de ruído progridem de sigma_min para sigma_max. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição                                                                 |
|-----------|-------------|-----------------------------------------------------------------------------|
| `sigmas`  | SIGMAS      | A sequência gerada de níveis de ruído (sigmas) seguindo o agendamento de ruído de Karras et al. (2022). |
