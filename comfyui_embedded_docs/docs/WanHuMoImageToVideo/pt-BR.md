# WanHuMoImageToVideo

O nó WanHuMoImageToVideo prepara dados de condicionamento e um vídeo latente vazio para o pipeline de geração de vídeo Wan HuMo. Ele pode anexar uma imagem de referência e embeddings de áudio às entradas de condicionamento positivo e negativo, e cria um latente preenchido com zeros dimensionado a partir da largura, altura, comprimento e tamanho do lote solicitados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamento positivo que orienta a geração de vídeo em direção ao conteúdo desejado. | CONDITIONING | Sim | - |
| `negativo` | Entrada de condicionamento negativo que desvia a geração de vídeo do conteúdo indesejado. | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar imagens de referência no espaço latente. | VAE | Sim | - |
| `largura` | Largura dos quadros do vídeo de saída em pixels. Padrão: 832. | INT | Sim | 16 a MAX_RESOLUTION, passo 16 |
| `altura` | Altura dos quadros do vídeo de saída em pixels. Padrão: 480. | INT | Sim | 16 a MAX_RESOLUTION, passo 16 |
| `duração` | Número de quadros na sequência de vídeo gerada. Padrão: 97. | INT | Sim | 1 a MAX_RESOLUTION, passo 4 |
| `tamanho_do_lote` | Número de sequências de vídeo a serem geradas simultaneamente. Padrão: 1. | INT | Sim | 1 a 4096 |
| `saída_do_codificador_de_áudio` | Dados opcionais de codificação de áudio que podem influenciar a geração de vídeo com base no conteúdo de áudio. | AUDIOENCODEROUTPUT | Não | - |
| `imagem_de_referência` | Imagem de referência opcional usada para orientar o estilo e o conteúdo da geração de vídeo. Apenas a primeira imagem do lote é usada. | IMAGE | Não | - |

**Nota:** Quando uma imagem de referência é fornecida, a primeira imagem do lote é ampliada para a `width` e a `height` solicitadas usando interpolação bilinear e codificada com o VAE. Esse latente de referência é anexado ao condicionamento positivo, enquanto um latente preenchido com zeros com a mesma forma é anexado ao condicionamento negativo. Quando `audio_encoder_output` é fornecido, os embeddings de áudio são interpolados e anexados ao condicionamento positivo, enquanto um embedding de áudio preenchido com zeros é anexado ao condicionamento negativo. Se qualquer uma das entradas opcionais for omitida, tensores de espaço reservado preenchidos com zeros são usados: um latente de referência preenchido com zeros com shape `[batch_size, 16, 1, height // 8, width // 8]` e/ou embeddings de áudio preenchidos com zeros com shape `[batch_size, latent_t + 1, 8, 5, 1280]`, onde `latent_t = ((length - 1) // 4) + 1`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento positivo modificado com imagem de referência e/ou embeddings de áudio incorporados. | CONDITIONING |
| `negative` | Condicionamento negativo modificado com imagem de referência e/ou embeddings de áudio incorporados. | CONDITIONING |
| `latent` | Representação latente inicializada com zeros para a sequência de vídeo, dimensionada de acordo com `width`, `height`, `length` e `batch_size`. Shape: `[batch_size, 16, latent_t, height // 8, width // 8]`, onde `latent_t = ((length - 1) // 4) + 1`. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `db674a4a00729a8715988030083e2858f958cd21de73bbbe4ed6d76f5f539419`
