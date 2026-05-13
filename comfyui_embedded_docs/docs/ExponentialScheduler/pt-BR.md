> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExponentialScheduler/pt-BR.md)

O nó `ExponentialScheduler` foi projetado para gerar uma sequência de valores sigma seguindo um agendamento exponencial para processos de amostragem por difusão. Ele oferece uma abordagem personalizável para controlar os níveis de ruído aplicados em cada etapa do processo de difusão, permitindo um ajuste fino do comportamento da amostragem.

## Entradas

| Parâmetro   | Tipo de Dado | Descrição                                                                                   |
|-------------|--------------|---------------------------------------------------------------------------------------------|
| `steps`     | INT          | Especifica o número de etapas no processo de difusão. Influencia o comprimento da sequência de sigma gerada e, consequentemente, a granularidade da aplicação do ruído. |
| `sigma_max` | FLOAT        | Define o valor máximo de sigma, estabelecendo o limite superior da intensidade do ruído no processo de difusão. Desempenha um papel crucial na determinação da faixa de níveis de ruído aplicados. |
| `sigma_min` | FLOAT        | Define o valor mínimo de sigma, estabelecendo o limite inferior da intensidade do ruído. Este parâmetro ajuda no ajuste fino do ponto inicial da aplicação do ruído. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição                                                                                   |
|-----------|--------------|---------------------------------------------------------------------------------------------|
| `sigmas`  | SIGMAS       | Uma sequência de valores sigma gerados de acordo com o agendamento exponencial. Esses valores são usados para controlar os níveis de ruído em cada etapa do processo de difusão. |