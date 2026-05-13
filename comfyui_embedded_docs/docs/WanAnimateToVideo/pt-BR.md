> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/pt-BR.md)

O nó WanAnimateToVideo gera conteúdo de vídeo combinando múltiplas entradas de condicionamento, incluindo referências de pose, expressões faciais e elementos de fundo. Ele processa várias entradas de vídeo para criar sequências animadas coerentes, mantendo a consistência temporal entre os quadros. O nó opera em operações de espaço latente e pode estender vídeos existentes continuando padrões de movimento.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positivo` | CONDITIONING | Sim | - | Condicionamento positivo para guiar a geração em direção ao conteúdo desejado |
| `negativo` | CONDITIONING | Sim | - | Condicionamento negativo para desviar a geração de conteúdo indesejado |
| `vae` | VAE | Sim | - | Modelo VAE usado para codificar e decodificar dados de imagem |
| `largura` | INT | Sim | 16 a MAX_RESOLUTION | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) |
| `altura` | INT | Sim | 16 a MAX_RESOLUTION | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) |
| `duração` | INT | Sim | 1 a MAX_RESOLUTION | Número de quadros a serem gerados (padrão: 77, passo: 4) |
| `tamanho_do_lote` | INT | Sim | 1 a 4096 | Número de vídeos a serem gerados simultaneamente (padrão: 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Não | - | Saída opcional do modelo de visão CLIP para condicionamento adicional |
| `imagem_de_referência` | IMAGE | Não | - | Imagem de referência usada como ponto de partida para a geração |
| `vídeo_de_rosto` | IMAGE | Não | - | Entrada de vídeo fornecendo orientação de expressão facial |
| `vídeo_de_pose` | IMAGE | Não | - | Entrada de vídeo fornecendo orientação de pose e movimento |
| `continuar_movimento_máx_quadros` | INT | Sim | 1 a MAX_RESOLUTION | Número máximo de quadros para continuar a partir do movimento anterior (padrão: 5, passo: 4) |
| `vídeo_de_fundo` | IMAGE | Não | - | Vídeo de fundo para composição com o conteúdo gerado |
| `máscara_de_personagem` | MASK | Não | - | Máscara definindo regiões do personagem para processamento seletivo |
| `continuar_movimento` | IMAGE | Não | - | Sequência de movimento anterior para continuar, garantindo consistência temporal |
| `deslocamento_quadro_vídeo` | INT | Sim | 0 a MAX_RESOLUTION | A quantidade de quadros a avançar em todos os vídeos de entrada. Usado para gerar vídeos mais longos por partes. Conecte à saída `deslocamento_quadro_vídeo` do nó anterior para estender um vídeo. (padrão: 0, passo: 1) |

**Restrições dos Parâmetros:**

- Quando `pose_video` é fornecido, a duração da saída será ajustada para corresponder à duração do vídeo de pose se a lógica `trim_to_pose_video` estiver ativa (atualmente definida como `False` no código-fonte)
- `face_video` é redimensionado automaticamente para resolução 512x512 e normalizado para uma faixa de -1,0 a 1,0 quando processado
- Os quadros de `continue_motion` são limitados pelo parâmetro `continue_motion_max_frames`; apenas os últimos `continue_motion_max_frames` quadros da entrada são usados
- Os vídeos de entrada (`face_video`, `pose_video`, `background_video`, `character_mask`) são deslocados por `video_frame_offset` antes do processamento; se o deslocamento exceder a duração do vídeo, a entrada é ignorada
- Se `character_mask` contiver apenas um quadro, ele será repetido em todos os quadros
- Quando `clip_vision_output` é fornecido, ele é aplicado tanto ao condicionamento positivo quanto ao negativo
- Se `reference_image` não for fornecida, uma imagem preta (todos zeros) é usada como referência padrão
- Se `continue_motion` não for fornecido, os quadros iniciais são preenchidos com ruído cinza (intensidade 0,5)

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `positivo` | CONDITIONING | Condicionamento positivo modificado com contexto adicional de vídeo, incluindo saída de visão CLIP, latente de vídeo de pose, pixels de vídeo facial, imagem latente concatenada e máscara concatenada |
| `negativo` | CONDITIONING | Condicionamento negativo modificado com contexto adicional de vídeo, incluindo saída de visão CLIP, latente de vídeo de pose, pixels de vídeo facial (invertidos), imagem latente concatenada e máscara concatenada |
| `latent` | LATENT | Conteúdo de vídeo gerado em formato de espaço latente com formato [batch_size, 16, latent_length + trim_latent, latent_height, latent_width] |
| `trim_latent` | INT | Informação de corte no espaço latente indicando o número de quadros latentes a serem cortados do início (corresponde aos quadros latentes da imagem de referência) |
| `trim_image` | INT | Informação de corte no espaço de imagem para quadros de movimento de referência, indicando o número de quadros de imagem a serem cortados do início |
| `deslocamento_quadro_vídeo` | INT | Deslocamento de quadro atualizado para continuar a geração de vídeo em partes, calculado como o deslocamento anterior mais a duração gerada |

---
**Source fingerprint (SHA-256):** `c2ca90f4963f629d51cdd7f4bdb67e01c32ce5ca7d916b1f992ccd220f57566c`
