> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/pt-BR.md)

O nó WanHuMoImageToVideo converte imagens em sequências de vídeo gerando representações latentes para os quadros do vídeo. Ele processa entradas de condicionamento e pode incorporar imagens de referência e embeddings de áudio para influenciar a geração do vídeo. O nó produz dados de condicionamento modificados e representações latentes adequadas para a síntese de vídeo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | Entrada de condicionamento positivo que orienta a geração do vídeo em direção ao conteúdo desejado |
| `negative` | CONDITIONING | Sim | - | Entrada de condicionamento negativo que direciona a geração do vídeo para longe de conteúdo indesejado |
| `vae` | VAE | Sim | - | Modelo VAE usado para codificar imagens de referência no espaço latente |
| `width` | INT | Sim | 16 a MAX_RESOLUTION | Largura dos quadros do vídeo de saída em pixels (padrão: 832, deve ser divisível por 16) |
| `height` | INT | Sim | 16 a MAX_RESOLUTION | Altura dos quadros do vídeo de saída em pixels (padrão: 480, deve ser divisível por 16) |
| `length` | INT | Sim | 1 a MAX_RESOLUTION | Número de quadros na sequência de vídeo gerada (padrão: 97) |
| `batch_size` | INT | Sim | 1 a 4096 | Número de sequências de vídeo a serem geradas simultaneamente (padrão: 1) |
| `audio_encoder_output` | AUDIOENCODEROUTPUT | Não | - | Dados opcionais de codificação de áudio que podem influenciar a geração de vídeo com base no conteúdo de áudio |
| `ref_image` | IMAGE | Não | - | Imagem de referência opcional usada para orientar o estilo e o conteúdo da geração do vídeo |

**Observação:** Quando uma imagem de referência é fornecida, ela é codificada e adicionada tanto ao condicionamento positivo quanto ao negativo. Quando a saída do codificador de áudio é fornecida, ela é processada e incorporada aos dados de condicionamento.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamento positivo modificado com a imagem de referência e/ou embeddings de áudio incorporados |
| `negative` | CONDITIONING | Condicionamento negativo modificado com a imagem de referência e/ou embeddings de áudio incorporados |
| `latent` | LATENT | Representação latente gerada contendo os dados da sequência de vídeo |
