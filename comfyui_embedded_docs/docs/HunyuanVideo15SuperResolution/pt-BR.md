# HunyuanVideo15SuperResolution

O nó HunyuanVideo15SuperResolution prepara dados de condicionamento para um processo de super-resolução de vídeo. Ele pega uma representação latente de um vídeo e, opcionalmente, uma imagem inicial, e os agrupa com um valor de aumento de ruído e dados opcionais de CLIP vision em um formato que um modelo pode usar para gerar uma saída de maior resolução.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | A entrada de condicionamento positivo a ser modificada com o latent concatenado e os dados de aumento de ruído. | CONDITIONING | Sim | N/A |
| `negative` | A entrada de condicionamento negativo a ser modificada com o latent concatenado e os dados de aumento de ruído. | CONDITIONING | Sim | N/A |
| `vae` | O VAE usado para codificar a `start_image` opcional. Obrigatório se `start_image` for fornecida. | VAE | Não | N/A |
| `start_image` | Uma imagem inicial opcional que orienta o processo de super-resolução. Se for fornecida, ela é ampliada, codificada com o `vae` e posicionada no início do latent de condicionamento. | IMAGE | Não | N/A |
| `clip_vision_output` | Embeddings opcionais de CLIP vision. Quando fornecidos, são adicionados tanto ao condicionamento positivo quanto ao negativo. | CLIP_VISION_OUTPUT | Não | N/A |
| `latent` | A representação latente do vídeo a ser incorporada ao condicionamento. | LATENT | Sim | N/A |
| `noise_augmentation` | A força do aumento de ruído a ser aplicada ao condicionamento (padrão: 0.70). Este é um parâmetro avançado. | FLOAT | Sim | 0.0 - 1.0 (step 0.01) |

**Nota:** Se você fornecer uma `start_image`, também deve conectar um `vae` para que ela seja codificada. A `start_image` é ampliada automaticamente para corresponder às dimensões implícitas no `latent` de entrada, e apenas os seus três primeiros canais de cor (RGB) são usados pelo VAE.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | O condicionamento positivo modificado, agora contendo o latent concatenado, o aumento de ruído e os dados opcionais de CLIP vision. | CONDITIONING |
| `negative` | O condicionamento negativo modificado, agora contendo o latent concatenado, o aumento de ruído e os dados opcionais de CLIP vision. | CONDITIONING |
| `latent` | O latent de entrada, repassado sem alterações. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c9e64092e78423f5e0dc43446a77240e09100242c25e4fccc91491049fe76be5`
