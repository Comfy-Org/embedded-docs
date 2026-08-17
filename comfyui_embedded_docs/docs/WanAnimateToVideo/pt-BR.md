# WanAnimateToVideo

Este nó experimental prepara a geração de vídeos Wan combinando uma imagem de referência com vídeos opcionais de pose, rosto e fundo. Ele constrói dados de condicionamento e um tensor de vídeo latente vazio para a geração subsequente, e retorna informações de deslocamento de quadros que ajudam a estender vídeos existentes em partes.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | Condicionamento positivo para guiar a geração em direção ao conteúdo desejado. | CONDITIONING | Sim | - |
| `negative` | Condicionamento negativo para afastar a geração de conteúdo indesejado. | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar e decodificar dados de imagem. | VAE | Sim | - |
| `width` | Largura do vídeo de saída em pixels (padrão: 832, passo: 16). | INT | Sim | 16 a MAX_RESOLUTION |
| `height` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16). | INT | Sim | 16 a MAX_RESOLUTION |
| `length` | Número de quadros a gerar (padrão: 77, passo: 4). | INT | Sim | 1 a MAX_RESOLUTION |
| `batch_size` | Número de vídeos a gerar em um único lote (padrão: 1). | INT | Sim | 1 a 4096 |
| `clip_vision_output` | Saída opcional do modelo de visão CLIP usada como condicionamento adicional tanto para o condicionamento positivo quanto para o negativo. | CLIP_VISION_OUTPUT | Não | - |
| `reference_image` | Imagem de referência usada como ponto de partida para a geração. Se não for fornecida, uma imagem preta (toda zerada) é usada. | IMAGE | Não | - |
| `face_video` | Vídeo que fornece orientação de expressão facial. Quando processado, é redimensionado para 512x512 e normalizado no intervalo de -1.0 a 1.0. | IMAGE | Não | - |
| `pose_video` | Vídeo que fornece orientação de pose e movimento. Se for mais curto que `length`, ele é preenchido com seu último quadro. | IMAGE | Não | - |
| `continue_motion_max_frames` | Número máximo de quadros para continuar a partir de um movimento anterior. Somente os últimos `continue_motion_max_frames` quadros de `continue_motion` são usados (padrão: 5, passo: 4). | INT | Sim | 1 a MAX_RESOLUTION |
| `background_video` | Vídeo de fundo para compor com o conteúdo gerado. | IMAGE | Não | - |
| `character_mask` | Máscara que define regiões do personagem para processamento seletivo. Se a máscara tiver apenas um quadro, ela é repetida em todos os quadros. | MASK | Não | - |
| `continue_motion` | Sequência de movimento anterior usada para manter a consistência temporal ao estender um vídeo. Apenas os últimos `continue_motion_max_frames` quadros são usados. | IMAGE | Não | - |
| `video_frame_offset` | A quantidade de quadros a avançar em todos os vídeos de entrada. Usado para gerar vídeos mais longos em partes. Conecte à saída `video_frame_offset` do nó anterior para estender um vídeo. (padrão: 0, passo: 1) | INT | Sim | 0 a MAX_RESOLUTION |

**Restrições de parâmetros:**

- Quando `pose_video` é fornecido, um vídeo de pose mais curto é preenchido com seu último quadro para corresponder a `length`. O código-fonte contém um sinalizador `trim_to_pose_video`, atualmente desabilitado, que, em vez disso, encurtaria a saída para corresponder ao comprimento do vídeo de pose.
- `face_video` é redimensionado para 512x512 e normalizado no intervalo de -1.0 a 1.0.
- `continue_motion` é limitado aos últimos `continue_motion_max_frames` quadros. Quando `continue_motion` é usado, `video_frame_offset` é reduzido pelo número de quadros utilizados, mas nunca fica abaixo de 0.
- Os vídeos de entrada (`face_video`, `pose_video`, `background_video`, `character_mask`) são deslocados por `video_frame_offset`. Se o deslocamento for maior ou igual ao comprimento deles, a entrada é ignorada, exceto para um `character_mask` com um único quadro, que é sempre repetido.
- Quando `clip_vision_output` é fornecido, ele é aplicado tanto ao condicionamento positivo quanto ao negativo.
- Se `reference_image` não for fornecido, uma imagem preta (toda zerada) é usada como referência.
- Se `continue_motion` não for fornecido, quadros cinza com valor de pixel 0.5 são usados para a parte de movimento.
- `width` e `height` usam um passo de 16; as dimensões latentes correspondentes são `width / 8` e `height / 8`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento positivo modificado que sempre inclui a imagem latente concatenada e a máscara concatenada. Se `clip_vision_output`, `pose_video` ou `face_video` forem fornecidos, seus valores também são adicionados. | CONDITIONING |
| `negative` | Condicionamento negativo modificado que sempre inclui a imagem latente concatenada e a máscara concatenada. Se `clip_vision_output`, `pose_video` ou `face_video` forem fornecidos, seus valores também são adicionados; os pixels do vídeo de rosto são definidos como -1.0. | CONDITIONING |
| `latent` | Tensor latente vazio inicializado com zeros, com formato `[batch_size, 16, latent_length + trim_latent, latent_height, latent_width]`. | LATENT |
| `trim_latent` | Número de quadros latentes a remover do início, correspondente aos quadros latentes da imagem de referência. | INT |
| `trim_image` | Número de quadros de imagem a remover do início, correspondente aos quadros de movimento de referência. | INT |
| `video_frame_offset` | Deslocamento de quadros atualizado para geração de vídeo em partes, igual ao deslocamento de entrada ajustado mais o comprimento gerado. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a95bae4c7ae4ddc8a95bc9dafa2ca920b1d2166802615189537dce16949bfc03`
