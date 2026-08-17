# WanSoundImageToVideoExtend

O nó WanSoundImageToVideoExtend estende um latente de vídeo existente gerando quadros adicionais, opcionalmente guiado por áudio, uma imagem de referência e um vídeo de controle. Ele recebe um latente de vídeo inicial e produz uma sequência de vídeo mais longa, usando as dicas de condicionamento e áudio fornecidas para influenciar o novo conteúdo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `positive` | Prompts de condicionamento positivo que orientam o que o vídeo deve incluir | CONDITIONING | Sim | - |
| `negative` | Prompts de condicionamento negativo que especificam o que o vídeo deve evitar | CONDITIONING | Sim | - |
| `vae` | Autoencoder Variacional usado para codificar e decodificar quadros de vídeo | VAE | Sim | - |
| `length` | Número total de quadros a serem gerados para a sequência de vídeo (padrão: 77, passo: 4) | INT | Sim | 1 até MAX_RESOLUTION |
| `video_latent` | Representação latente de vídeo inicial que serve como ponto de partida para a extensão. A largura, a altura, o tamanho do lote e o offset de quadro são derivados deste latente. Os últimos 19 quadros deste latente também são usados como movimento de referência para a nova sequência. | LATENT | Sim | - |
| `audio_encoder_output` | Embeddings de áudio opcionais que podem influenciar a geração de vídeo com base nas características do som. Quando fornecidos, o áudio é interpolado e usado para criar um bucket de embeddings de áudio que é adicionado ao condicionamento. | AUDIO_ENCODER_OUTPUT | Não | - |
| `ref_image` | Imagem de referência opcional que fornece orientação visual para a geração de vídeo. A imagem é ampliada para corresponder às dimensões alvo e codificada em um latente, que é então adicionado ao condicionamento positivo e negativo. Apenas a primeira imagem do lote é usada. | IMAGE | Não | - |
| `control_video` | Vídeo de controle opcional que pode guiar o movimento e o estilo do vídeo gerado. O vídeo é ampliado, codificado e adicionado ao condicionamento positivo e negativo. O vídeo de controle é truncado para o `length` especificado. | IMAGE | Não | - |

Nota: Quando `audio_encoder_output` é fornecido, os embeddings de áudio são adicionados ao condicionamento positivo, enquanto o condicionamento negativo recebe os mesmos embeddings definidos como zero. O offset de quadro derivado de `video_latent` determina onde na sequência de áudio os novos quadros começam. Se a sequência de áudio não contiver quadros suficientes para cobrir a extensão solicitada, nenhum condicionamento de áudio é aplicado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | Condicionamento positivo processado com contexto de vídeo aplicado, incluindo embeddings de áudio, latentes de referência, movimento de referência e vídeo de controle, se fornecido | CONDITIONING |
| `negative` | Condicionamento negativo processado com contexto de vídeo aplicado, incluindo embeddings de áudio (zerados), latentes de referência, movimento de referência e vídeo de controle, se fornecido | CONDITIONING |
| `latent` | Representação latente de vídeo gerada contendo a sequência de vídeo estendida, inicializada como zeros com dimensões derivadas do `video_latent` de entrada e do `length` alvo | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/pt-BR.md)

---
**Source fingerprint (SHA-256):** `32b58aaba566f346a0388ba804fc92e7ad426bf2e9e7039e5fdb0bf6a746e972`
