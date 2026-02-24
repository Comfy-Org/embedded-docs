> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/pt-BR.md)

O nó WanAnimateToVideo gera conteúdo de vídeo combinando múltiplas entradas de condicionamento, incluindo referências de pose, expressões faciais e elementos de fundo. Ele processa várias entradas de vídeo para criar sequências animadas coerentes, mantendo a consistência temporal entre os quadros. O nó lida com operações no espaço latente e pode estender vídeos existentes continuando os padrões de movimento.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | Condicionamento positivo para guiar a geração em direção ao conteúdo desejado |
| `negative` | CONDITIONING | Sim | - | Condicionamento negativo para direcionar a geração para longe de conteúdo indesejado |
| `vae` | VAE | Sim | - | Modelo VAE usado para codificar e decodificar dados de imagem |
| `width` | INT | Não | 16 a MAX_RESOLUTION | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) |
| `height` | INT | Não | 16 a MAX_RESOLUTION | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) |
| `length` | INT | Não | 1 a MAX_RESOLUTION | Número de quadros a serem gerados (padrão: 77, passo: 4) |
| `batch_size` | INT | Não | 1 a 4096 | Número de vídeos a serem gerados simultaneamente (padrão: 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Não | - | Saída opcional do modelo de visão CLIP para condicionamento adicional |
| `reference_image` | IMAGE | Não | - | Imagem de referência usada como ponto de partida para a geração |
| `face_video` | IMAGE | Não | - | Entrada de vídeo fornecendo orientação de expressão facial |
| `pose_video` | IMAGE | Não | - | Entrada de vídeo fornecendo orientação de pose e movimento |
| `continue_motion_max_frames` | INT | Não | 1 a MAX_RESOLUTION | Número máximo de quadros para continuar a partir do movimento anterior (padrão: 5, passo: 4) |
| `background_video` | IMAGE | Não | - | Vídeo de fundo para composição com o conteúdo gerado |
| `character_mask` | MASK | Não | - | Máscara que define regiões do personagem para processamento seletivo |
| `continue_motion` | IMAGE | Não | - | Sequência de movimento anterior para continuar, visando consistência temporal |
| `video_frame_offset` | INT | Não | 0 a MAX_RESOLUTION | A quantidade de quadros para avançar em todos os vídeos de entrada. Usado para gerar vídeos mais longos por partes. Conecte à saída `video_frame_offset` do nó anterior para estender um vídeo. (padrão: 0, passo: 1) |

**Restrições dos Parâmetros:**

- Quando `pose_video` é fornecido e a lógica `trim_to_pose_video` está ativa, o comprimento da saída será ajustado para corresponder à duração do vídeo de pose.
- `face_video` é redimensionado automaticamente para a resolução 512x512 durante o processamento.
- Os quadros de `continue_motion` são limitados pelo parâmetro `continue_motion_max_frames`.
- Os vídeos de entrada (`face_video`, `pose_video`, `background_video`, `character_mask`) são deslocados pelo valor de `video_frame_offset` antes do processamento.
- Se `character_mask` contiver apenas um quadro, ele será repetido em todos os quadros.
- Quando `clip_vision_output` é fornecido, ele é aplicado tanto ao condicionamento positivo quanto ao negativo.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamento positivo modificado com contexto adicional de vídeo |
| `negative` | CONDITIONING | Condicionamento negativo modificado com contexto adicional de vídeo |
| `latent` | LATENT | Conteúdo de vídeo gerado no formato de espaço latente |
| `trim_latent` | INT | Informação de corte do espaço latente para processamento subsequente |
| `trim_image` | INT | Informação de corte do espaço de imagem para quadros de movimento de referência |
| `video_frame_offset` | INT | Deslocamento de quadro atualizado para continuar a geração de vídeo em partes |
