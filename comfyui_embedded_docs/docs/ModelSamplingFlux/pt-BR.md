> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/pt-BR.md)

O nó ModelSamplingFlux aplica a amostragem do modelo Flux a um determinado modelo, calculando um parâmetro de deslocamento com base nas dimensões da imagem. Ele cria uma configuração de amostragem especializada que ajusta o comportamento do modelo de acordo com os parâmetros especificados de largura, altura e deslocamento, retornando o modelo modificado com as novas configurações de amostragem aplicadas.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo ao qual aplicar a amostragem Flux |
| `max_shift` | FLOAT | Sim | 0.0 - 100.0 | Valor máximo de deslocamento para o cálculo da amostragem (padrão: 1.15) |
| `base_shift` | FLOAT | Sim | 0.0 - 100.0 | Valor base de deslocamento para o cálculo da amostragem (padrão: 0.5) |
| `width` | INT | Sim | 16 - MAX_RESOLUTION | Largura da imagem alvo em pixels (padrão: 1024) |
| `height` | INT | Sim | 16 - MAX_RESOLUTION | Altura da imagem alvo em pixels (padrão: 1024) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com a configuração de amostragem Flux aplicada |
