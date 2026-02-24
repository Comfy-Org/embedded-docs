> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGGuider/pt-BR.md)

O nó CFGGuider cria um sistema de orientação para controlar o processo de amostragem na geração de imagens. Ele recebe um modelo junto com entradas de condicionamento positivo e negativo e, em seguida, aplica uma escala de orientação livre de classificador para direcionar a geração em direção ao conteúdo desejado, evitando elementos indesejados. Este nó produz um objeto guia que pode ser usado por nós de amostragem para controlar a direção da geração de imagens.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | Obrigatório | - | - | O modelo a ser usado para orientação |
| `positive` | CONDITIONING | Obrigatório | - | - | O condicionamento positivo que orienta a geração em direção ao conteúdo desejado |
| `negative` | CONDITIONING | Obrigatório | - | - | O condicionamento negativo que direciona a geração para longe de conteúdo indesejado |
| `cfg` | FLOAT | Obrigatório | 8.0 | 0.0 - 100.0 | A escala de orientação livre de classificador que controla a intensidade com que o condicionamento influencia a geração |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `GUIDER` | GUIDER | Um objeto guia que pode ser passado para nós de amostragem para controlar o processo de geração |
