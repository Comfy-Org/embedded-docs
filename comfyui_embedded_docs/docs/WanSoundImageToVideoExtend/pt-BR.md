# WanSoundImageToVideoExtend

O nó WanSoundImageToVideoExtend estende um latent de vídeo existente ao gerar quadros adicionais, opcionalmente guiado por áudio, uma imagem de referência e um vídeo de controle. Ele recebe um latent de vídeo inicial e produz uma sequência de vídeo mais longa, usando os sinais de condicionamento e áudio fornecidos para influenciar o novo conteúdo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | Prompts de condicionamento positivos que orientam o que o vídeo deve incluir | CONDITIONING | Sim | - |
| `negativo` | Prompts de condicionamento negativos que especificam o que o vídeo deve evitar | CONDITIONING | Sim | - |
| `vae` | Autoencoder Variacional usado para codificar a imagem de referência e o vídeo de controle no espaço latente | VAE | Sim | - |
| `comprimento` | Número total de quadros a serem gerados para a sequência de vídeo (padrão: 77, passo: 4) | INT | Sim | 1 to MAX_RESOLUTION |
| `latente de vídeo` | Latent de vídeo inicial que serve como ponto de partida para a extensão. A largura, a altura, o tamanho do lote e o deslocamento de quadros da saída são derivados deste latent. Seus últimos 19 quadros são usados como condicionamento de movimento de referência. | LATENT | Sim | - |
| `saída do codificador de áudio` | Embeddings de áudio opcionais que podem influenciar a geração de vídeo com base nas características do som. Quando fornecidos, o áudio é interpolado e convertido em um bucket de embeddings de áudio que é adicionado ao condicionamento. | AUDIOENCODEROUTPUT | Não | - |
| `imagem de referência` | Imagem de referência opcional que fornece orientação visual para a geração do vídeo. A imagem é ampliada para corresponder às dimensões alvo e codificada em um latent, que é então adicionado ao condicionamento positivo e negativo. Apenas a primeira imagem do lote é usada. | IMAGE | Não | - |
| `vídeo de controle` | Vídeo de controle opcional que orienta o movimento e a estrutura do vídeo gerado. O vídeo é ampliado, codificado e adicionado ao condicionamento positivo e negativo. O vídeo de controle é truncado para o `length` especificado. | IMAGE | Não | - |

Nota: O latent de saída é inicializado com zeros e as dimensões alvo. O `video_latent` de entrada não é copiado para esta saída; seus últimos 19 quadros são usados como movimento de referência.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positivo` | Condicionamento positivo processado com contexto de vídeo aplicado, incluindo embeddings de áudio, latents de referência, movimento de referência e vídeo de controle, se fornecido | CONDITIONING |
| `negativo` | Condicionamento negativo processado com contexto de vídeo aplicado, incluindo embeddings de áudio (zerados), latents de referência, movimento de referência e vídeo de controle, se fornecido | CONDITIONING |
| `latente` | Representação latente de vídeo da sequência estendida, inicializada com zeros e com dimensões derivadas do `video_latent` de entrada e do `length` alvo | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/pt-BR.md)

---
**Source fingerprint (SHA-256):** `32b58aaba566f346a0388ba804fc92e7ad426bf2e9e7039e5fdb0bf6a746e972`
