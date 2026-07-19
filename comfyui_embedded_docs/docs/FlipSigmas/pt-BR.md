# FlipSigmas

O nó `FlipSigmas` foi projetado para manipular a sequência de valores sigma usados em modelos de difusão, invertendo sua ordem e garantindo que o primeiro valor seja diferente de zero, caso originalmente seja zero. Essa operação é crucial para adaptar os níveis de ruído em ordem inversa, facilitando o processo de geração em modelos que operam reduzindo gradualmente o ruído dos dados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sigmas` | O parâmetro 'sigmas' representa a sequência de valores sigma a ser invertida. Essa sequência é crucial para controlar os níveis de ruído aplicados durante o processo de difusão, e sua inversão é essencial para o processo de geração reversa. | `SIGMAS` |

## Saídas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sigmas` | A saída é a sequência modificada de valores sigma, invertida e ajustada para garantir que o primeiro valor seja diferente de zero, caso originalmente seja zero, pronta para uso em operações subsequentes do modelo de difusão. | `SIGMAS` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FlipSigmas/pt-BR.md)
