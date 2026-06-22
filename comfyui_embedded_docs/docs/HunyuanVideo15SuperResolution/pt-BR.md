# HunyuanVideo15SuperResolution

O nó HunyuanVideo15SuperResolution prepara dados de condicionamento para um processo de super-resolução de vídeo. Ele recebe uma representação latente de um vídeo e, opcionalmente, uma imagem inicial, e os organiza junto com aumento de ruído e dados de visão CLIP em um formato que pode ser usado por um modelo para gerar uma saída de resolução mais alta.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | A entrada de condicionamento positiva a ser modificada com dados latentes e de aumento. | CONDITIONING | Sim | N/A |
| `negativo` | A entrada de condicionamento negativa a ser modificada com dados latentes e de aumento. | CONDITIONING | Sim | N/A |
| `vae` | O VAE usado para codificar a `imagem_inicial` opcional. Necessário se `imagem_inicial` for fornecida. | VAE | Não | N/A |
| `imagem_inicial` | Uma imagem inicial opcional para guiar a super-resolução. Se fornecida, será redimensionada e codificada no latente de condicionamento. | IMAGE | Não | N/A |
| `clip_vision_output` | Embeddings de visão CLIP opcionais para adicionar ao condicionamento. | CLIP_VISION_OUTPUT | Não | N/A |
| `latente` | A representação latente de vídeo de entrada que será incorporada ao condicionamento. | LATENT | Sim | N/A |
| `aumento_de_ruído` | A intensidade do aumento de ruído a ser aplicado ao condicionamento (padrão: 0.70). | FLOAT | Não | 0.0 - 1.0 |

**Observação:** Se você fornecer uma `start_image`, também deverá conectar um `vae` para que ela seja codificada. A `start_image` será automaticamente redimensionada para corresponder às dimensões implícitas pelo `latent` de entrada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | O condicionamento positivo modificado, agora contendo o latente concatenado, aumento de ruído e dados opcionais de visão CLIP. | CONDITIONING |
| `negativo` | O condicionamento negativo modificado, agora contendo o latente concatenado, aumento de ruído e dados opcionais de visão CLIP. | CONDITIONING |
| `latente` | O latente de entrada é transmitido inalterado. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f913327a81d034997fa8a485ca4b3691f75ba1d3c5c6e2e73ab107021b58a52a`
