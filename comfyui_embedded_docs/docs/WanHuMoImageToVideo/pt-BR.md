O nó WanHuImagemParaVideo converte imagens em sequências de vídeo gerando representações latentes para os quadros do vídeo. Ele processa entradas de condicionamento e pode incorporar imagens de referência e embeddings de áudio para influenciar a geração do vídeo. O nó produz dados de condicionamento modificados e representações latentes adequadas para síntese de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamento positivo que guia a geração do vídeo em direção ao conteúdo desejado | CONDITIONING | Sim | - |
| `negativo` | Entrada de condicionamento negativo que direciona a geração do vídeo para longe de conteúdo indesejado | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar imagens de referência no espaço latente | VAE | Sim | - |
| `largura` | Largura dos quadros do vídeo de saída em pixels (padrão: 832, deve ser divisível por 16) | INT | Sim | 16 a RESOLUÇÃO_MÁXIMA |
| `altura` | Altura dos quadros do vídeo de saída em pixels (padrão: 480, deve ser divisível por 16) | INT | Sim | 16 a RESOLUÇÃO_MÁXIMA |
| `duração` | Número de quadros na sequência de vídeo gerada (padrão: 97, deve ser tal que (comprimento - 1) seja divisível por 4) | INT | Sim | 1 a RESOLUÇÃO_MÁXIMA |
| `tamanho_do_lote` | Número de sequências de vídeo a serem geradas simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `saída_do_codificador_de_áudio` | Dados opcionais de codificação de áudio que podem influenciar a geração do vídeo com base no conteúdo de áudio | SAÍDA_CODIFICADOR_ÁUDIO | Não | - |
| `imagem_de_referência` | Imagem de referência opcional usada para guiar o estilo e o conteúdo da geração do vídeo | IMAGEM | Não | - |

**Nota:** Quando uma imagem de referência é fornecida, ela é codificada e adicionada tanto ao condicionamento positivo quanto ao negativo. Quando a saída do codificador de áudio é fornecida, ela é processada e incorporada aos dados de condicionamento. Se nenhum dos dois for fornecido, tensores placeholder preenchidos com zeros são usados tanto para os latentes de referência quanto para os embeddings de áudio.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | Condicionamento positivo modificado com imagem de referência e/ou embeddings de áudio incorporados | CONDITIONING |
| `negativo` | Condicionamento negativo modificado com imagem de referência e/ou embeddings de áudio incorporados | CONDITIONING |
| `latent` | Representação latente gerada contendo os dados da sequência de vídeo | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6301671d04748ce80c561a65df80c7ca146b91bcce8851872df40211af29fd39`
