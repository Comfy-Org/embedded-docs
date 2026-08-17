# WanDancerVideo

WanDancerVideo prepara os dados de condicionamento e um tensor latent vazio para a geração de vídeos com o modelo WanDancer. Ele recebe condicionamento positivo e negativo e, opcionalmente, combina-os com uma imagem inicial, uma máscara, embeddings de visão do CLIP e recursos de áudio para controlar o vídeo gerado.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positive` | O condicionamento positivo para guiar a geração de vídeo. | CONDITIONING | Sim |  |
| `negative` | O condicionamento negativo para guiar a geração de vídeo. | CONDITIONING | Sim |  |
| `vae` | O VAE usado para codificar a imagem inicial no espaço latente. | VAE | Sim |  |
| `width` | A largura do vídeo gerado em pixels (padrão: 480). | INT | Sim | 16 a MAX_RESOLUTION (passo: 16) |
| `height` | A altura do vídeo gerado em pixels (padrão: 832). | INT | Sim | 16 a MAX_RESOLUTION (passo: 16) |
| `length` | O número de quadros no vídeo gerado. Deve permanecer 149 para o WanDancer (padrão: 149). | INT | Sim | 1 a MAX_RESOLUTION (passo: 4) |
| `clip_vision_output` | Os embeddings de visão do CLIP para o primeiro quadro. | CLIP_VISION_OUTPUT | Não |  |
| `clip_vision_output_ref` | Os embeddings de visão do CLIP para a imagem de referência. | CLIP_VISION_OUTPUT | Não |  |
| `start_image` | A(s) imagem(ns) inicial(is) a ser(em) codificada(s), pode ser qualquer número de quadros. | IMAGE | Não |  |
| `mask` | Máscara de condicionamento de imagem para a(s) imagem(ns) inicial(is). O branco é mantido, o preto é gerado. Usada para as gerações locais. | MASK | Não |  |
| `audio_encoder_output` | A saída de um codificador de áudio, fornecendo recursos de áudio, FPS e escala de injeção de áudio para geração condicionada por áudio. | AUDIO_ENCODER_OUTPUT | Não |  |

**Nota sobre Restrições dos Parâmetros:**
- Quando `start_image` é fornecida, ela é redimensionada para `width` × `height`, limitada a `length` quadros e codificada em um latent que é anexado a ambos os condicionamentos juntamente com uma máscara de concatenação.
- `mask` só tem efeito quando `start_image` também é fornecida. Na máscara, as áreas brancas são mantidas e as áreas pretas são geradas. Quando `mask` não é fornecida, a área da imagem inicial é usada como guia de condicionamento e os quadros restantes são gerados.
- `clip_vision_output_ref` é aplicado somente quando `clip_vision_output` é fornecido.
- `audio_encoder_output` anexa recursos de áudio, FPS e uma escala de injeção de áudio (padrão 1.0) a ambos os condicionamentos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positive` | O condicionamento positivo com quaisquer dados adicionais (latent de concatenação, visão do CLIP, áudio) anexados. | CONDITIONING |
| `negative` | O condicionamento negativo com quaisquer dados adicionais (latent de concatenação, visão do CLIP, áudio) anexados. | CONDITIONING |
| `latent` | Um tensor latent vazio com dimensões correspondentes ao comprimento, altura e largura de vídeo especificados. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `086a0ec361cf7f7ae7ce9505b55d31d92b025c6c7c9cde192009e6664011ad05`
