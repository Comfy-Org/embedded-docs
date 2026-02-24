> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/pt-BR.md)

O nó USOStyleReference aplica patches de referência de estilo a modelos usando características de imagem codificadas da saída de visão CLIP. Ele cria uma versão modificada do modelo de entrada incorporando informações de estilo extraídas de entradas visuais, permitindo capacidades de transferência de estilo ou geração baseada em referência.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo base ao qual aplicar o patch de referência de estilo |
| `model_patch` | MODEL_PATCH | Sim | - | O patch do modelo contendo informações de referência de estilo |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Sim | - | As características visuais codificadas extraídas do processamento de visão CLIP |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com os patches de referência de estilo aplicados |
