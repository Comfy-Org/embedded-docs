# WanDancerVideo

O nó WanDancerVideo prepara os dados de condicionamento e um tensor latente vazio para a geração de vídeo com o modelo WanDancer. Ele anexa imagens iniciais opcionais, máscaras, embeddings de visão do CLIP e recursos de áudio ao condicionamento positivo e negativo para que possam guiar o vídeo gerado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | O condicionamento positivo para guiar a geração de vídeo. | CONDITIONING | Sim |  |
| `negativo` | O condicionamento negativo para guiar a geração de vídeo. | CONDITIONING | Sim |  |
| `vae` | O VAE usado para codificar a imagem inicial no espaço latente. | VAE | Sim |  |
| `largura` | A largura do vídeo gerado em pixels (padrão: 480). | INT | Sim | 16 to MAX_RESOLUTION (step: 16) |
| `altura` | A altura do vídeo gerado em pixels (padrão: 832). | INT | Sim | 16 to MAX_RESOLUTION (step: 16) |
| `duração` | O número de quadros no vídeo gerado. Deve permanecer 149 para WanDancer (padrão: 149). | INT | Sim | 1 to MAX_RESOLUTION (step: 4) |
| `clip_vision_output` | Os embeddings de visão do CLIP para o primeiro quadro. | CLIP_VISION_OUTPUT | Não |  |
| `clip_vision_output_ref` | Os embeddings de visão do CLIP para a imagem de referência. | CLIP_VISION_OUTPUT | Não |  |
| `imagem_inicial` | A(s) imagem(ns) inicial(is) a ser(em) codificada(s), pode ser qualquer número de quadros. | IMAGE | Não |  |
| `máscara` | Máscara de condicionamento de imagem para a(s) imagem(ns) inicial(is). O branco é mantido, o preto é gerado. Usada para as gerações locais. | MASK | Não |  |
| `audio_encoder_output` | Uma saída de codificador de áudio que fornece recursos de áudio, taxa de quadros e valores de escala de injeção, que são anexados ao condicionamento quando fornecida. | AUDIO_ENCODER_OUTPUT | Não |  |

### Notas sobre o Comportamento dos Parâmetros

- `start_image` é opcional. Quando fornecida, ela é redimensionada para `width` e `height`, codificada pelo `vae` e anexada tanto ao condicionamento positivo quanto ao negativo. Se `start_image` tiver mais quadros do que `length`, os quadros extras são descartados. Se tiver menos quadros, os quadros ausentes são preenchidos com valores zero.
- `mask` só tem efeito quando `start_image` também é fornecida. As áreas brancas são mantidas e as áreas pretas são geradas.
- `clip_vision_output_ref` só tem efeito quando `clip_vision_output` também é fornecida.
- `audio_encoder_output`, quando fornecida, anexa embeddings de áudio, taxa de quadros e escala de injeção tanto ao condicionamento positivo quanto ao negativo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positivo` | O condicionamento positivo com quaisquer dados de latente da imagem inicial, máscara, visão do CLIP ou áudio anexados. | CONDITIONING |
| `negativo` | O condicionamento negativo com quaisquer dados de latente da imagem inicial, máscara, visão do CLIP ou áudio anexados. | CONDITIONING |
| `latente` | Um tensor latente vazio dimensionado para o comprimento, a altura e a largura do vídeo solicitado. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `086a0ec361cf7f7ae7ce9505b55d31d92b025c6c7c9cde192009e6664011ad05`
