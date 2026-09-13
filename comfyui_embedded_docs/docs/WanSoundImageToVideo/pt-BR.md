# WanSoundImageToVideo

O nó WanSoundImageToVideo prepara condicionamento e um tensor latente de vídeo vazio para a geração de vídeo com som do Wan. Opcionalmente, ele pode incorporar codificação de áudio, uma imagem de referência, um vídeo de controle e uma referência de movimento para guiar o vídeo gerado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | Prompts de condicionamento positivo que orientam qual conteúdo deve aparecer no vídeo gerado | CONDITIONING | Sim | - |
| `negative` | Prompts de condicionamento negativo que especificam qual conteúdo deve ser evitado no vídeo gerado | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar imagens de referência, referências de movimento e quadros do vídeo de controle em representações latentes | VAE | Sim | - |
| `width` | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `height` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `length` | Número de quadros no vídeo gerado (padrão: 77, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `batch_size` | Número de vídeos a serem gerados simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `audio_encoder_output` | Codificação de áudio opcional que pode influenciar a geração do vídeo com base nas características do som. Quando fornecido, os recursos de áudio são interpolados e usados para condicionar a geração do vídeo. | AUDIO_ENCODER_OUTPUT | Não | - |
| `ref_image` | Imagem de referência opcional que fornece orientação visual para o conteúdo do vídeo. A imagem é ampliada para corresponder à largura e altura especificadas e, em seguida, codificada em uma representação latente. Apenas a primeira imagem da entrada é usada como referência. | IMAGE | Não | - |
| `control_video` | Vídeo de controle opcional que orienta o movimento e a estrutura do vídeo gerado. O vídeo é ampliado e codificado, depois usado para condicionar a saída. Apenas os primeiros `length` quadros são usados. | IMAGE | Não | - |
| `ref_motion` | Referência de movimento opcional que fornece orientação para padrões de movimento no vídeo. Se a entrada tiver mais de 73 quadros, apenas os últimos 73 são usados. Se menos de 73 quadros forem fornecidos, a sequência é preenchida com quadros neutros. | IMAGE | Não | - |

Nota: Todas as entradas opcionais podem ser usadas de forma independente ou em conjunto. O nó modifica o condicionamento `positive` e `negative` fornecidos com base em quais entradas opcionais estão conectadas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento positivo processado que foi modificado para geração de vídeo, incluindo embeddings de áudio, latentes de referência, referências de movimento e condicionamento do vídeo de controle quando as entradas opcionais correspondentes são fornecidas | CONDITIONING |
| `negative` | Condicionamento negativo processado que foi modificado para geração de vídeo, incluindo embeddings de áudio (definidos como zero), latentes de referência, referências de movimento e condicionamento do vídeo de controle quando as entradas opcionais correspondentes são fornecidas | CONDITIONING |
| `latent` | Tensor latente de vídeo vazio usado como ponto de partida para a geração. O tensor latente tem formato `[batch_size, 16, latent_t, height/8, width/8]`, onde `latent_t` é calculado como `((length - 1) // 4) + 1`. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b1148cd00d8999dd6842e3c2fb13655fda8f20d5befed975a6d1652688b2807c`
