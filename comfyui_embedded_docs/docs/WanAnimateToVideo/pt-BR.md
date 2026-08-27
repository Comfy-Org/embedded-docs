# WanAnimateToVideo

WanAnimateToVideo prepara dados de condicionamento e um latente inicial para gerar vídeos animados com Wan, usando entradas como imagem de referência, pose, rosto, fundo e movimento opcional de uma parte anterior. Ele também suporta a geração de vídeos mais longos em partes, lendo e atualizando um valor de `video_frame_offset`. Este nó está marcado como experimental.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | Condicionamento positivo para guiar a geração em direção ao conteúdo desejado. | CONDITIONING | Sim | - |
| `negativo` | Condicionamento negativo para afastar a geração de conteúdo indesejado. | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar as entradas de imagem e vídeo no espaço latente. | VAE | Sim | - |
| `largura` | Largura do vídeo gerado em pixels (padrão: 832, passo: 16). | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura do vídeo gerado em pixels (padrão: 480, passo: 16). | INT | Sim | 16 a MAX_RESOLUTION |
| `duração` | Número de quadros a gerar (padrão: 77, passo: 4). | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | Número de vídeos a gerar em um lote (padrão: 1). | INT | Sim | 1 a 4096 |
| `clip_vision_output` | Saída de visão do CLIP opcional adicionada ao condicionamento positivo e negativo. | CLIP_VISION_OUTPUT | Não | - |
| `imagem_de_referência` | Imagem de referência usada como ponto de partida da aparência do vídeo gerado. Se não for fornecida, uma imagem preta é usada. | IMAGE | Não | - |
| `vídeo_de_rosto` | Entrada de vídeo que fornece orientação de expressão facial. Ela é redimensionada para 512x512 e escalada internamente para o intervalo de -1.0 a 1.0. | IMAGE | Não | - |
| `vídeo_de_pose` | Entrada de vídeo que fornece orientação de pose e movimento. | IMAGE | Não | - |
| `continuar_movimento_máx_quadros` | Número máximo de quadros reaproveitados de uma sequência de movimento anterior (padrão: 5, passo: 4). | INT | Sim | 1 a MAX_RESOLUTION |
| `vídeo_de_fundo` | Vídeo de fundo usado para preencher as partes dos quadros que não contêm o personagem. | IMAGE | Não | - |
| `máscara_de_personagem` | Máscara que define as regiões do personagem, usada para separar o personagem do fundo. | MASK | Não | - |
| `continuar_movimento` | Quadros de movimento anteriores a partir dos quais continuar, mantendo a consistência temporal com partes geradas anteriormente. | IMAGE | Não | - |
| `deslocamento_quadro_vídeo` | A quantidade de quadros a deslocar em todos os vídeos de entrada. Usado para gerar vídeos mais longos por partes. Conecte à saída video_frame_offset do nó anterior para estender um vídeo. (padrão: 0, passo: 1) | INT | Sim | 0 a MAX_RESOLUTION |

**Restrições dos parâmetros:**

- Quando `continue_motion` é fornecido, apenas os últimos `continue_motion_max_frames` quadros dele são usados.
- As entradas (`face_video`, `pose_video`, `background_video`, `character_mask`) são deslocadas por `video_frame_offset` antes do uso. Se o deslocamento for maior ou igual à contagem de quadros da entrada, essa entrada será ignorada, exceto por uma `character_mask` de um único quadro.
- Se `character_mask` tiver apenas um quadro, esse quadro será repetido para todos os quadros da saída.
- Quando `pose_video` for mais curto que `length`, seu último quadro é repetido para preencher os quadros restantes; o comprimento da saída não é alterado.
- Se `clip_vision_output` for fornecido, ele será adicionado ao condicionamento positivo e negativo.
- Se `reference_image` não for fornecida, uma imagem preta (todos os valores zero) é usada como referência padrão.
- Se `continue_motion` não for fornecido, os quadros de movimento iniciais são preenchidos com quadros em cinza constante (intensidade 0.5).
- Quando `continue_motion` é usado, `video_frame_offset` é reduzido pelo número de quadros reaproveitados antes que o deslocamento da próxima parte seja calculado, para que quadros sobrepostos não sejam processados duas vezes.
- `background_video` preenche os quadros de movimento após a porção de movimento de referência; ele não substitui a imagem de referência nem os quadros reaproveitados de `continue_motion`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positivo` | Condicionamento positivo modificado com contexto adicional de vídeo, incluindo saída de visão do CLIP, latente do vídeo de pose, pixels do vídeo de rosto, imagem latente concatenada e máscara concatenada. | CONDITIONING |
| `negativo` | Condicionamento negativo modificado com contexto adicional de vídeo, incluindo saída de visão do CLIP, latente do vídeo de pose, pixels de rosto em branco, imagem latente concatenada e máscara concatenada. | CONDITIONING |
| `latente` | Tensor latente inicial (com todas as amostras zeradas) para o vídeo gerado, com o formato `[batch_size, 16, latent_length + trim_latent, latent_height, latent_width]`. | LATENT |
| `latente_recortado` | Número de quadros latentes a remover do início do latente, correspondendo aos quadros da imagem de referência. | INT |
| `imagem_recortada` | Número de quadros de imagem a remover do início, correspondendo aos quadros de movimento de referência. | INT |
| `deslocamento_quadro_vídeo` | Deslocamento de quadro atualizado para usar na próxima parte, com base no deslocamento de entrada e no número de quadros processados. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a95bae4c7ae4ddc8a95bc9dafa2ca920b1d2166802615189537dce16949bfc03`
