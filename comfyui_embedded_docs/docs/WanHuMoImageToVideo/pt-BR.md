# WanHuMoImageToVideo

O nó WanHuMoImageToVideo prepara os dados de condicionamento e o espaço latente para a geração de imagem para vídeo. Ele cria um tensor de vídeo latente vazio, opcionalmente codifica uma imagem de referência com o VAE e, opcionalmente, converte a saída do codificador de áudio em condicionamento temporizado para o vídeo. O nó gera fluxos de condicionamento positivo e negativo, além de um tensor latente para amostragem posterior do vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | Entrada de condicionamento positivo que orienta a geração de vídeo para o conteúdo desejado. | CONDITIONING | Sim | - |
| `negative` | Entrada de condicionamento negativo que afasta a geração de vídeo de conteúdo indesejado. | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar a imagem de referência no espaço latente. | VAE | Sim | - |
| `width` | Largura dos quadros do vídeo de saída em pixels (padrão: 832; deve ser divisível por 16). | INT | Sim | 16 a MAX_RESOLUTION (passo 16) |
| `height` | Altura dos quadros do vídeo de saída em pixels (padrão: 480; deve ser divisível por 16). | INT | Sim | 16 a MAX_RESOLUTION (passo 16) |
| `length` | Número de quadros na sequência de vídeo gerada (padrão: 97; deve satisfazer `(length - 1)` divisível por 4). | INT | Sim | 1 a MAX_RESOLUTION (passo 4) |
| `batch_size` | Número de sequências de vídeo para gerar simultaneamente (padrão: 1). | INT | Sim | 1 a 4096 |
| `audio_encoder_output` | Saída opcional do codificador de áudio usada para influenciar a geração de vídeo com base no conteúdo de áudio. | AUDIO_ENCODER_OUTPUT | Não | - |
| `ref_image` | Imagem de referência opcional usada para orientar o estilo e o conteúdo da geração de vídeo. | IMAGE | Não | - |

**Nota:** Quando `ref_image` é fornecida, ela é redimensionada para `width` x `height`, codificada com o `vae` e adicionada tanto ao condicionamento positivo quanto ao negativo como um latente de referência. Quando nenhuma imagem de referência é fornecida, são usados latentes de referência nulos. Quando `audio_encoder_output` é fornecida, suas incorporações de áudio são processadas e adicionadas a ambos os fluxos de condicionamento como uma incorporação de áudio; caso contrário, uma incorporação de áudio nula é usada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positive` | Condicionamento positivo com informações do latente de referência e da incorporação de áudio adicionadas. | CONDITIONING |
| `negative` | Condicionamento negativo com informações do latente de referência e da incorporação de áudio adicionadas. | CONDITIONING |
| `latent` | Tensor latente que representa a sequência de vídeo, inicializado com zeros de acordo com `batch_size`, `length`, `height` e `width`. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `db674a4a00729a8715988030083e2858f958cd21de73bbbe4ed6d76f5f539419`
