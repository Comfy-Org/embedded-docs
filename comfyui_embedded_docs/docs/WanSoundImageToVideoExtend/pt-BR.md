> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/pt-BR.md)

O nó WanSoundImageToVideoExtend estende a geração de imagem para vídeo incorporando condicionamento de áudio e imagens de referência. Ele recebe condicionamentos positivo e negativo juntamente com dados latentes de vídeo e incorporações de áudio opcionais para gerar sequências de vídeo estendidas. O nó processa essas entradas para criar saídas de vídeo coerentes que podem ser sincronizadas com pistas de áudio.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | Prompts de condicionamento positivo que orientam o que o vídeo deve incluir |
| `negative` | CONDITIONING | Sim | - | Prompts de condicionamento negativo que especificam o que o vídeo deve evitar |
| `vae` | VAE | Sim | - | Autoencoder Variacional usado para codificar e decodificar quadros do vídeo |
| `length` | INT | Sim | 1 a MAX_RESOLUTION | Número de quadros a serem gerados para a sequência de vídeo (padrão: 77, passo: 4) |
| `video_latent` | LATENT | Sim | - | Representação latente de vídeo inicial que serve como ponto de partida para a extensão |
| `audio_encoder_output` | AUDIOENCODEROUTPUT | Não | - | Incorporações de áudio opcionais que podem influenciar a geração do vídeo com base nas características do som |
| `ref_image` | IMAGE | Não | - | Imagem de referência opcional que fornece orientação visual para a geração do vídeo |
| `control_video` | IMAGE | Não | - | Vídeo de controle opcional que pode orientar o movimento e o estilo do vídeo gerado |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamento positivo processado com o contexto de vídeo aplicado |
| `negative` | CONDITIONING | Condicionamento negativo processado com o contexto de vídeo aplicado |
| `latent` | LATENT | Representação latente de vídeo gerada contendo a sequência de vídeo estendida |
