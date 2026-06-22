# WanAnimateToVideo

O nó WanAnimateToVideo gera conteúdo de vídeo combinando múltiplas entradas de condicionamento, incluindo referências de pose, expressões faciais e elementos de fundo. Ele processa várias entradas de vídeo para criar sequências animadas coerentes, mantendo a consistência temporal entre os quadros. O nó opera em operações de espaço latente e pode estender vídeos existentes continuando padrões de movimento.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | Condicionamento positivo para guiar a geração em direção ao conteúdo desejado | CONDITIONING | Sim | - |
| `negativo` | Condicionamento negativo para desviar a geração de conteúdo indesejado | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar e decodificar dados de imagem | VAE | Sim | - |
| `largura` | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `duração` | Número de quadros a serem gerados (padrão: 77, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | Número de vídeos a serem gerados simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `clip_vision_output` | Saída opcional do modelo de visão CLIP para condicionamento adicional | CLIP_VISION_OUTPUT | Não | - |
| `imagem_de_referência` | Imagem de referência usada como ponto de partida para a geração | IMAGE | Não | - |
| `vídeo_de_rosto` | Entrada de vídeo fornecendo orientação de expressão facial | IMAGE | Não | - |
| `vídeo_de_pose` | Entrada de vídeo fornecendo orientação de pose e movimento | IMAGE | Não | - |
| `continuar_movimento_máx_quadros` | Número máximo de quadros para continuar a partir do movimento anterior (padrão: 5, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `vídeo_de_fundo` | Vídeo de fundo para composição com o conteúdo gerado | IMAGE | Não | - |
| `máscara_de_personagem` | Máscara definindo regiões do personagem para processamento seletivo | MASK | Não | - |
| `continuar_movimento` | Sequência de movimento anterior para continuar, garantindo consistência temporal | IMAGE | Não | - |
| `deslocamento_quadro_vídeo` | A quantidade de quadros a avançar em todos os vídeos de entrada. Usado para gerar vídeos mais longos por partes. Conecte à saída `deslocamento_quadro_vídeo` do nó anterior para estender um vídeo. (padrão: 0, passo: 1) | INT | Sim | 0 a MAX_RESOLUTION |

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

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | Condicionamento positivo modificado com contexto adicional de vídeo, incluindo saída de visão CLIP, latente de vídeo de pose, pixels de vídeo facial, imagem latente concatenada e máscara concatenada | CONDITIONING |
| `negativo` | Condicionamento negativo modificado com contexto adicional de vídeo, incluindo saída de visão CLIP, latente de vídeo de pose, pixels de vídeo facial (invertidos), imagem latente concatenada e máscara concatenada | CONDITIONING |
| `latent` | Conteúdo de vídeo gerado em formato de espaço latente com formato [batch_size, 16, latent_length + trim_latent, latent_height, latent_width] | LATENT |
| `trim_latent` | Informação de corte no espaço latente indicando o número de quadros latentes a serem cortados do início (corresponde aos quadros latentes da imagem de referência) | INT |
| `trim_image` | Informação de corte no espaço de imagem para quadros de movimento de referência, indicando o número de quadros de imagem a serem cortados do início | INT |
| `deslocamento_quadro_vídeo` | Deslocamento de quadro atualizado para continuar a geração de vídeo em partes, calculado como o deslocamento anterior mais a duração gerada | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c2ca90f4963f629d51cdd7f4bdb67e01c32ce5ca7d916b1f992ccd220f57566c`
