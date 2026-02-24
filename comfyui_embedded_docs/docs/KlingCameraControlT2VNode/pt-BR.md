> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlT2VNode/pt-BR.md)

O nó Kling Text to Video Camera Control transforma texto em vídeos cinematográficos com movimentos de câmera profissionais que simulam cinematografia do mundo real. Este nó permite controlar ações da câmera virtual, incluindo zoom, rotação, panorâmica, inclinação e visão em primeira pessoa, mantendo o foco no seu texto original. A duração, o modo e o nome do modelo são fixos, pois o controle de câmera só é suportado no modo pro com o modelo kling-v1-5 e duração de 5 segundos.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | Prompt de texto positivo |
| `negative_prompt` | STRING | Sim | - | Prompt de texto negativo |
| `cfg_scale` | FLOAT | Não | 0.0-1.0 | Controla o quanto a saída segue o prompt (padrão: 0.75) |
| `aspect_ratio` | COMBO | Não | "16:9"<br>"9:16"<br>"1:1"<br>"21:9"<br>"3:4"<br>"4:3" | A proporção de tela para o vídeo gerado (padrão: "16:9") |
| `camera_control` | CAMERA_CONTROL | Não | - | Pode ser criado usando o nó Kling Camera Controls. Controla o movimento e a ação da câmera durante a geração do vídeo. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo gerado com efeitos de controle de câmera |
| `video_id` | STRING | O identificador único para o vídeo gerado |
| `duration` | STRING | A duração do vídeo gerado |
