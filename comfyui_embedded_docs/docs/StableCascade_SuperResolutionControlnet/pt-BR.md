# StableCascade_SuperResolutionControlnet

O nó StableCascade_SuperResolutionControlnet prepara entradas para o processamento de super-resolução do Stable Cascade. Ele recebe uma imagem de entrada e a codifica usando uma VAE para criar a entrada do controlnet, enquanto também gera representações latentes provisórias (preenchidas com zeros) para os estágios C e B do pipeline do Stable Cascade.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Range |
| --- | --- | --- | --- | --- |
| `imagem` | A imagem de entrada a ser processada para super-resolução. Apenas os 3 primeiros canais de cor (RGB) da imagem são usados para codificação. | IMAGE | Sim | - |
| `vae` | O modelo VAE usado para codificar a imagem de entrada | VAE | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `controlnet_input` | A representação da imagem codificada pela VAE, adequada para entrada no controlnet | IMAGE |
| `stage_c` | Representação latente provisória (preenchida com zeros) para o estágio C do processamento do Stable Cascade, com 16 canais e dimensões baseadas no tamanho da imagem de entrada dividido por 16 | LATENT |
| `stage_b` | Representação latente provisória (preenchida com zeros) para o estágio B do processamento do Stable Cascade, com 4 canais e dimensões baseadas no tamanho da imagem de entrada dividido por 2 | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d9eff373ac7736f2e2f9788d1b43c04bb3212422aa1703d1d58ac512ce476925`
