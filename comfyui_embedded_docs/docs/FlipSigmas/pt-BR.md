> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FlipSigmas/pt-BR.md)

O nó `FlipSigmas` é projetado para manipular a sequência de valores sigma usados em modelos de difusão, revertendo sua ordem e garantindo que o primeiro valor seja diferente de zero se originalmente fosse zero. Esta operação é crucial para adaptar os níveis de ruído em ordem inversa, facilitando o processo de geração em modelos que operam reduzindo gradualmente o ruído dos dados.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `sigmas`  | `SIGMAS`    | O parâmetro 'sigmas' representa a sequência de valores sigma a ser invertida. Esta sequência é crucial para controlar os níveis de ruído aplicados durante o processo de difusão, e invertê-la é essencial para o processo de geração reversa. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `sigmas`  | `SIGMAS`    | A saída é a sequência modificada de valores sigma, invertida e ajustada para garantir que o primeiro valor seja diferente de zero se originalmente fosse zero, pronta para uso em operações subsequentes do modelo de difusão. |
