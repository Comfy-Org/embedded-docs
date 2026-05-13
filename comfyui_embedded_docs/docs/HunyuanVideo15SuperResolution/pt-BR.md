> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/pt-BR.md)

O nó HunyuanVideo15SuperResolution prepara dados de condicionamento para um processo de super-resolução de vídeo. Ele recebe uma representação latente de um vídeo e, opcionalmente, uma imagem inicial, e os organiza junto com aumento de ruído e dados de visão CLIP em um formato que pode ser usado por um modelo para gerar uma saída de resolução mais alta.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `positivo` | CONDITIONING | Sim | N/A | A entrada de condicionamento positiva a ser modificada com dados latentes e de aumento. |
| `negativo` | CONDITIONING | Sim | N/A | A entrada de condicionamento negativa a ser modificada com dados latentes e de aumento. |
| `vae` | VAE | Não | N/A | O VAE usado para codificar a `imagem_inicial` opcional. Necessário se `imagem_inicial` for fornecida. |
| `imagem_inicial` | IMAGE | Não | N/A | Uma imagem inicial opcional para guiar a super-resolução. Se fornecida, será redimensionada e codificada no latente de condicionamento. |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Não | N/A | Embeddings de visão CLIP opcionais para adicionar ao condicionamento. |
| `latente` | LATENT | Sim | N/A | A representação latente de vídeo de entrada que será incorporada ao condicionamento. |
| `aumento_de_ruído` | FLOAT | Não | 0.0 - 1.0 | A intensidade do aumento de ruído a ser aplicado ao condicionamento (padrão: 0.70). |

**Observação:** Se você fornecer uma `start_image`, também deverá conectar um `vae` para que ela seja codificada. A `start_image` será automaticamente redimensionada para corresponder às dimensões implícitas pelo `latent` de entrada.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `positivo` | CONDITIONING | O condicionamento positivo modificado, agora contendo o latente concatenado, aumento de ruído e dados opcionais de visão CLIP. |
| `negativo` | CONDITIONING | O condicionamento negativo modificado, agora contendo o latente concatenado, aumento de ruído e dados opcionais de visão CLIP. |
| `latente` | LATENT | O latente de entrada é transmitido inalterado. |

---
**Source fingerprint (SHA-256):** `f913327a81d034997fa8a485ca4b3691f75ba1d3c5c6e2e73ab107021b58a52a`
