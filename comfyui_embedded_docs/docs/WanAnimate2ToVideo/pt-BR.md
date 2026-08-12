# WanAnimate2ToVideo

O WanAnimate2ToVideo anima um personagem a partir de uma imagem de referência, transferindo as expressões faciais, o movimento corporal e os gestos das mãos de um vídeo de pose separado. Ele constrói os dados de condicionamento e um latente inicial que um amostrador de geração de vídeo usa para criar a animação.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `positive` | O condicionamento positivo para a geração de vídeo. | CONDITIONING | Sim | N/A |
| `negative` | O condicionamento negativo para a geração de vídeo. | CONDITIONING | Sim | N/A |
| `vae` | O VAE usado para codificar a imagem de referência e os quadros do vídeo no espaço latente. | VAE | Sim | N/A |
| `width` | Largura do vídeo de saída em pixels. (padrão: 832) | INT | Sim | 16 a MAX_RESOLUTION (passo 16) |
| `height` | Altura do vídeo de saída em pixels. (padrão: 480) | INT | Sim | 16 a MAX_RESOLUTION (passo 16) |
| `length` | Número de quadros a serem gerados. (padrão: 81) | INT | Sim | 1 a MAX_RESOLUTION (passo 4) |
| `batch_size` | Número de vídeos a serem gerados simultaneamente. (padrão: 1) | INT | Sim | 1 a 4096 |
| `reference_image` | O personagem a ser animado. Se omitido, uma imagem preta é usada. | IMAGE | Não | N/A |
| `pose_video` | O vídeo cujo movimento é transferido para o personagem de referência. Se tiver menos quadros que `length`, o último quadro é repetido para preencher os quadros ausentes. | IMAGE | Não | N/A |
| `clip_vision_output` | Visão CLIP da imagem de referência. | CLIP_VISION_OUTPUT | Não | N/A |
| `positive_pose` | Prompt para o ramo do vídeo de pose, descrevendo o movimento em vez do personagem. O padrão é `positive`. Usado tanto nas passagens cond quanto uncond. | CONDITIONING | Não | N/A |
| `clip_vision_output_pose` | Visão CLIP do primeiro quadro do vídeo de pose. O padrão é `clip_vision_output`. | CLIP_VISION_OUTPUT | Não | N/A |
| `continue_motion` | Sequência de movimento anterior para dar continuidade, visando consistência temporal. Apenas o último quadro dessa sequência é usado como quadro inicial do movimento. | IMAGE | Não | N/A |
| `video_frame_offset` | Quadros para avançar no vídeo de pose. Conecte à saída `video_frame_offset` do nó anterior ao estender. (padrão: 0) | INT | Sim | 0 a MAX_RESOLUTION |
| `pose_strength` | Escala a influência do vídeo de pose no movimento. 1.0 é o comportamento treinado; abaixo disso enfraquece a adesão, acima disso amplifica. 0.0 o silencia, mas não o remove completamente. (padrão: 1.0) | FLOAT | Sim | 0.00 a 10.00 (passo 0.01) |
| `pose_start_percent` | Percentual de amostragem em que a influência da pose começa. Fora dessa janela, o ramo de pose é totalmente ignorado, o que também acelera essas etapas. (padrão: 0.0) | FLOAT | Sim | 0.00 a 1.00 (passo 0.01) |
| `pose_end_percent` | Percentual de amostragem em que a influência da pose termina. O movimento é geralmente estabelecido no início, então, por exemplo, 0.7 pode afrouxar os detalhes finos enquanto mantém a coreografia. (padrão: 1.0) | FLOAT | Sim | 0.00 a 1.00 (passo 0.01) |
| `reference_image_strength` | Escala o quanto os quadros gerados atendem ao quadro latente da imagem de referência. Abaixo de 1.0 afrouxa a adesão à identidade/aparência (por exemplo, para permitir que o prompt reestilize), acima disso a fortalece contra desvios. (padrão: 1.0) | FLOAT | Sim | 0.00 a 10.00 (passo 0.01) |

**Notas de validação:**

- `pose_start_percent` não deve ser maior que `pose_end_percent`; caso contrário, o nó lança um ValueError.
- Se `pose_video` for fornecido, sua contagem de quadros deve ser maior que `video_frame_offset`; caso contrário, o nó lança um ValueError.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | Condicionamento positivo para a amostragem, com a imagem de referência, a máscara e os dados opcionais de pose anexados. | CONDITIONING |
| `negative` | Condicionamento negativo para a amostragem, com a mesma imagem de referência, a máscara e os dados opcionais de pose anexados. | CONDITIONING |
| `latent` | Latente inicial preenchido com zeros para o amostrador de vídeo; os primeiros `trim_latent` quadros devem ser removidos antes da decodificação. | LATENT |
| `trim_latent` | Número de quadros latentes que devem ser removidos antes da decodificação. | INT |
| `trim_image` | Número de quadros de imagem sobrepostos ao estender um vídeo. | INT |
| `video_frame_offset` | Quadros para avançar no vídeo de pose; equivale ao deslocamento de entrada ajustado mais o número de quadros gerados. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimate2ToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7e1f497983ab63a68e5ef5439b3ef4e9295f79f78530c9dc5de16a8238475f05`
