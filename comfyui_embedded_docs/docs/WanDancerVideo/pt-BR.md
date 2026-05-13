> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/pt-BR.md)

O nó WanDancerVideo prepara dados de condicionamento e um tensor latente vazio para geração de vídeo com o modelo WanDancer. Ele combina condicionamentos positivo e negativo com entradas opcionais, como imagem inicial, máscara, embeddings de visão CLIP e recursos de áudio para controlar o vídeo gerado.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `positive` | CONDITIONING | Sim | | O condicionamento positivo para guiar a geração do vídeo. |
| `negative` | CONDITIONING | Sim | | O condicionamento negativo para guiar a geração do vídeo. |
| `vae` | VAE | Sim | | O VAE usado para codificar a imagem inicial no espaço latente. |
| `width` | INT | Sim | 16 a MAX_RESOLUTION (passo: 16) | A largura do vídeo gerado em pixels (padrão: 480). |
| `height` | INT | Sim | 16 a MAX_RESOLUTION (passo: 16) | A altura do vídeo gerado em pixels (padrão: 832). |
| `length` | INT | Sim | 1 a MAX_RESOLUTION (passo: 4) | O número de quadros no vídeo gerado. Deve permanecer 149 para WanDancer (padrão: 149). |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Não | | Os embeddings de visão CLIP para o primeiro quadro. |
| `clip_vision_output_ref` | CLIP_VISION_OUTPUT | Não | | Os embeddings de visão CLIP para a imagem de referência. |
| `start_image` | IMAGE | Não | | A(s) imagem(ns) inicial(is) a serem codificadas. Pode ser qualquer número de quadros, até o `length` especificado. |
| `mask` | MASK | Não | | Máscara de condicionamento de imagem para a(s) imagem(ns) inicial(is). Áreas brancas são mantidas, áreas pretas são geradas. Usada para gerações locais. |
| `audio_encoder_output` | AUDIO_ENCODER_OUTPUT | Não | | A saída de um codificador de áudio, fornecendo recursos de áudio, fps e escala de injeção para geração condicionada por áudio. |

**Observação sobre Restrições de Parâmetros:**
- As entradas `start_image` e `mask` são opcionais, mas podem ser usadas juntas. Quando `start_image` é fornecida, ela é codificada e concatenada com o latente. Se `mask` também for fornecida, ela controla quais partes da imagem inicial são mantidas (branco) e quais são regeneradas (preto). Se `mask` não for fornecida, toda a área da imagem inicial é usada como guia de condicionamento.
- As entradas `clip_vision_output` e `clip_vision_output_ref` são opcionais e podem ser usadas juntas para fornecer contexto visual para o primeiro quadro e uma imagem de referência.
- A entrada `audio_encoder_output` é opcional e fornece recursos de áudio para geração condicionada por áudio.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `positive` | CONDITIONING | O condicionamento positivo com quaisquer dados adicionais (latente concatenado, visão CLIP, áudio) anexados. |
| `negative` | CONDITIONING | O condicionamento negativo com quaisquer dados adicionais (latente concatenado, visão CLIP, áudio) anexados. |
| `latent` | LATENT | Um tensor latente vazio com dimensões correspondentes ao comprimento, altura e largura do vídeo especificados. |

---
**Source fingerprint (SHA-256):** `7ab1b4662eb8d780295ea3a3e3139c64d81e03a979a293a481f82deaf1fc2f7e`
