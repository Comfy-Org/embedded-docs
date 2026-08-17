# WanSoundImageToVideo

O nó WanSoundImageToVideo prepara a geração de vídeos a partir de imagens, com condicionamento de áudio opcional. Ele recebe prompts de condicionamento positivo e negativo juntamente com um modelo VAE para construir as entradas de condicionamento e um tensor latente vazio, podendo incorporar imagens de referência, codificação de áudio, vídeos de controle e referências de movimento para guiar o processo de geração do vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positive` | Prompts de condicionamento positivo que orientam qual conteúdo deve aparecer no vídeo gerado | CONDITIONING | Sim | - |
| `negative` | Prompts de condicionamento negativo que especificam qual conteúdo deve ser evitado no vídeo gerado | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar e decodificar as representações latentes do vídeo | VAE | Sim | - |
| `width` | Largura do vídeo de saída em pixels (padrão: 832, deve ser divisível por 16) | INT | Sim | 16 a MAX_RESOLUTION (passo: 16) |
| `height` | Altura do vídeo de saída em pixels (padrão: 480, deve ser divisível por 16) | INT | Sim | 16 a MAX_RESOLUTION (passo: 16) |
| `length` | Número de quadros no vídeo gerado (padrão: 77, deve ser divisível por 4) | INT | Sim | 1 a MAX_RESOLUTION (passo: 4) |
| `batch_size` | Número de vídeos a serem gerados simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `audio_encoder_output` | Codificação de áudio opcional que pode influenciar a geração do vídeo com base nas características do som. Quando fornecida, as características de áudio são interpoladas e usadas para condicionar a geração do vídeo. | AUDIOENCODEROUTPUT | Não | - |
| `ref_image` | Imagem de referência opcional que fornece orientação visual para o conteúdo do vídeo. A imagem é redimensionada para corresponder à largura e à altura especificadas e, em seguida, codificada em uma representação latente. Apenas a primeira imagem do lote de entrada é usada. | IMAGE | Não | - |
| `control_video` | Vídeo de controle opcional que orienta o movimento e a estrutura do vídeo gerado. O vídeo é redimensionado e codificado e, em seguida, usado para condicionar a saída. Apenas os primeiros `length` quadros são usados. | IMAGE | Não | - |
| `ref_motion` | Referência de movimento opcional que fornece orientação para os padrões de movimento no vídeo. Se a entrada tiver mais de 73 quadros, apenas os últimos 73 serão usados. Se forem fornecidos menos de 73 quadros, a sequência é preenchida com quadros neutros. | IMAGE | Não | - |

**Observação:** As entradas opcionais (`audio_encoder_output`, `ref_image`, `control_video`, `ref_motion`) podem ser usadas de forma independente ou combinadas. O condicionamento por vídeo de controle é sempre aplicado; quando nenhum `control_video` é fornecido, um vídeo de controle vazio (zero) é usado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento positivo processado e modificado para a geração de vídeo. Quando as entradas opcionais correspondentes são fornecidas, ele inclui embeddings de áudio, latentes de referência, referências de movimento e condicionamento por vídeo de controle. | CONDITIONING |
| `negative` | Condicionamento negativo processado e modificado para a geração de vídeo. Quando as entradas opcionais correspondentes são fornecidas, ele inclui embeddings de áudio (definidos como zero), latentes de referência, referências de movimento e condicionamento por vídeo de controle. | CONDITIONING |
| `latent` | Tensor latente vazio que serve como ponto de partida para a geração do vídeo. O latente tem formato [batch_size, 16, latent_t, height/8, width/8], em que latent_t = ((length - 1) // 4) + 1. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b1148cd00d8999dd6842e3c2fb13655fda8f20d5befed975a6d1652688b2807c`
