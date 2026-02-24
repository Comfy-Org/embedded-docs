> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlI2VNode/pt-BR.md)

O nó Kling Image to Video Camera Control transforma imagens estáticas em vídeos cinematográficos com movimentos de câmera profissionais. Este nó especializado de imagem para vídeo permite que você controle ações de câmera virtuais, incluindo zoom, rotação, panorâmica, inclinação e visão em primeira pessoa, mantendo o foco na sua imagem original. O controle de câmera atualmente é suportado apenas no modo pro com o modelo kling-v1-5 e duração de 5 segundos.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `start_frame` | IMAGE | Sim | - | Imagem de Referência - URL ou string codificada em Base64, não pode exceder 10MB, resolução não inferior a 300*300px, proporção de aspecto entre 1:2.5 ~ 2.5:1. Base64 não deve incluir o prefixo data:image. |
| `prompt` | STRING | Sim | - | Prompt de texto positivo |
| `negative_prompt` | STRING | Sim | - | Prompt de texto negativo |
| `cfg_scale` | FLOAT | Não | 0.0-1.0 | Controla a força da orientação do texto (padrão: 0.75) |
| `aspect_ratio` | COMBO | Não | Múltiplas opções disponíveis | Seleção da proporção de aspecto do vídeo (padrão: 16:9) |
| `camera_control` | CAMERA_CONTROL | Sim | - | Pode ser criado usando o nó Kling Camera Controls. Controla o movimento e a ação da câmera durante a geração do vídeo. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | A saída de vídeo gerada |
| `video_id` | STRING | Identificador único para o vídeo gerado |
| `duration` | STRING | Duração do vídeo gerado |
