# WanHuMoImageToVideo

O nó WanHuMoImageToVideo converte imagens em sequências de vídeo gerando representações latentes para os quadros de vídeo. Ele processa entradas de condicionamento e pode incorporar imagens de referência e embeddings de áudio para influenciar a geração de vídeo. O nó gera dados de condicionamento modificados e representações latentes adequadas para síntese de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamento positivo que orienta a geração de vídeo para o conteúdo desejado | CONDITIONING | Sim | - |
| `negativo` | Entrada de condicionamento negativo que afasta a geração de vídeo de conteúdo indesejado | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar imagens de referência no espaço latente | VAE | Sim | - |
| `largura` | Largura dos quadros de vídeo de saída em pixels (padrão: 832, deve ser divisível por 16) | INT | Sim | 16 to MAX_RESOLUTION |
| `altura` | Altura dos quadros de vídeo de saída em pixels (padrão: 480, deve ser divisível por 16) | INT | Sim | 16 to MAX_RESOLUTION |
| `duração` | Número de quadros na sequência de vídeo gerada (padrão: 97, deve ser tal que (length - 1) seja divisível por 4) | INT | Sim | 1 to MAX_RESOLUTION |
| `tamanho_do_lote` | Número de sequências de vídeo a serem geradas simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `saída_do_codificador_de_áudio` | Dados opcionais de codificação de áudio que podem influenciar a geração de vídeo com base no conteúdo de áudio | AUDIOENCODEROUTPUT | Não | - |
| `imagem_de_referência` | Imagem de referência opcional usada para orientar o estilo e o conteúdo da geração de vídeo | IMAGE | Não | - |

**Nota:** Quando uma imagem de referência é fornecida, ela é codificada em um latent que é anexado ao condicionamento positivo, enquanto um latent preenchido com zeros do mesmo formato é anexado ao condicionamento negativo. Quando a saída do codificador de áudio é fornecida, os embeddings de áudio são interpolados e anexados ao condicionamento positivo, enquanto um embedding de áudio preenchido com zeros é anexado ao condicionamento negativo. Se as entradas opcionais forem omitidas, tensores substitutos preenchidos com zeros são usados tanto para os latents de referência quanto para os embeddings de áudio.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | Condicionamento positivo modificado com imagem de referência e/ou embeddings de áudio incorporados | CONDITIONING |
| `negativo` | Condicionamento negativo modificado com imagem de referência e/ou embeddings de áudio incorporados | CONDITIONING |
| `latente` | Representação latente para a sequência de vídeo, inicializada com zeros e dimensionada de acordo com as configurações de `width`, `height` e `length` | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `db674a4a00729a8715988030083e2858f958cd21de73bbbe4ed6d76f5f539419`
