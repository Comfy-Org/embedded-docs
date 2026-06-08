O nó PolyexponentialScheduler foi projetado para gerar uma sequência de níveis de ruído (sigmas) com base em um agendamento de ruído poliexponencial. Este agendamento é uma função polinomial no logaritmo de sigma, permitindo uma progressão flexível e personalizável dos níveis de ruído ao longo do processo de difusão.

## Entradas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `steps` | Especifica o número de etapas no processo de difusão, afetando a granularidade dos níveis de ruído gerados. | INT |
| `sigma_max` | O nível máximo de ruído, definindo o limite superior do agendamento de ruído. | FLOAT |
| `sigma_min` | O nível mínimo de ruído, definindo o limite inferior do agendamento de ruído. | FLOAT |
| `rho` | Um parâmetro que controla a forma do agendamento de ruído poliexponencial, influenciando como os níveis de ruído progridem entre os valores mínimo e máximo. | FLOAT |

## Saídas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `sigmas` | A saída é uma sequência de níveis de ruído (sigmas) adaptada ao agendamento de ruído poliexponencial especificado. | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PolyexponentialScheduler/pt-BR.md)
