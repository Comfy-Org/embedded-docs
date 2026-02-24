> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/pt-BR.md)

O nó ModelSamplingLTXV aplica parâmetros de amostragem avançados a um modelo com base na contagem de tokens. Ele calcula um valor de deslocamento usando uma interpolação linear entre os valores de deslocamento base e máximo, onde o cálculo depende do número de tokens no latente de entrada. Em seguida, o nó cria uma configuração de amostragem de modelo especializada e a aplica ao modelo de entrada.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo de entrada ao qual aplicar os parâmetros de amostragem |
| `max_shift` | FLOAT | Não | 0.0 a 100.0 | O valor de deslocamento máximo usado no cálculo (padrão: 2.05) |
| `base_shift` | FLOAT | Não | 0.0 a 100.0 | O valor de deslocamento base usado no cálculo (padrão: 0.95) |
| `latent` | LATENT | Não | - | Entrada latente opcional usada para determinar a contagem de tokens para o cálculo do deslocamento |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com os parâmetros de amostragem aplicados |
