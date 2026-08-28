# HunyuanVideo15SuperResolution

O nó HunyuanVideo15SuperResolution prepara dados de condicionamento para um processo de super-resolução de vídeo. Ele recebe uma representação latente de um vídeo e, opcionalmente, uma imagem inicial, e os empacota junto com aumento de ruído e dados de visão do CLIP em um formato que pode ser usado por um modelo para gerar uma saída de maior resolução.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | O condicionamento positivo a ser modificado com dados latentes e de aumento. | CONDITIONING | Sim | N/A |
| `negativo` | O condicionamento negativo a ser modificado com dados latentes e de aumento. | CONDITIONING | Sim | N/A |
| `vae` | O VAE usado para codificar a `start_image` opcional. Obrigatório se `start_image` for fornecida. | VAE | Não | N/A |
| `imagem_inicial` | Uma imagem inicial opcional para guiar a super-resolução. Se fornecida, ela é ampliada e codificada no latente de condicionamento. | IMAGE | Não | N/A |
| `clip_vision_output` | Embeddings de visão do CLIP opcionais para adicionar ao condicionamento. | CLIP_VISION_OUTPUT | Não | N/A |
| `latente` | A representação latente de vídeo de entrada que é incorporada ao condicionamento. | LATENT | Sim | N/A |
| `aumento_de_ruído` | A intensidade do aumento de ruído a ser aplicada ao condicionamento (padrão: 0.70). Este é um parâmetro avançado. | FLOAT | Não | 0.0 - 1.0 (step 0.01) |

**Nota:** Se você fornecer uma `start_image`, você também deve conectar um `vae` para que ela possa ser codificada. A `start_image` é automaticamente ampliada para 16 vezes as dimensões espaciais (largura e altura) do `latent` de entrada, em seguida, codificada e colocada no latente de condicionamento. Apenas os canais RGB da `start_image` são usados para codificação.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positivo` | O condicionamento positivo modificado, agora contendo o latente concatenado, o aumento de ruído e os dados opcionais de visão do CLIP. | CONDITIONING |
| `negativo` | O condicionamento negativo modificado, agora contendo o latente concatenado, o aumento de ruído e os dados opcionais de visão do CLIP. | CONDITIONING |
| `latente` | O latente de entrada é repassado inalterado. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c9e64092e78423f5e0dc43446a77240e09100242c25e4fccc91491049fe76be5`
