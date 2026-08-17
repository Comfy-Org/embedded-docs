# StableCascade_SuperResolutionControlnet

O nó StableCascade_SuperResolutionControlnet prepara as entradas para o processamento de super-resolução do Stable Cascade. Ele recebe uma imagem de entrada e a codifica usando um VAE para criar a entrada do controlnet, além de gerar representações latentes de espaço reservado para o estágio C e o estágio B do pipeline Stable Cascade.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `image` | A imagem de entrada a ser processada para super-resolução | IMAGE | Sim | - |
| `vae` | O modelo VAE usado para codificar a imagem de entrada | VAE | Sim | - |

Observação: Somente os três primeiros canais de cor da imagem de entrada são usados durante a codificação com o VAE.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `controlnet_input` | A representação de imagem codificada, adequada para entrada do controlnet | IMAGE |
| `stage_c` | Representação latente de espaço reservado para o estágio C do processamento Stable Cascade, com dimensões baseadas no tamanho da imagem de entrada dividido por 16 | LATENT |
| `stage_b` | Representação latente de espaço reservado para o estágio B do processamento Stable Cascade, com dimensões baseadas no tamanho da imagem de entrada dividido por 2 | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d9eff373ac7736f2e2f9788d1b43c04bb3212422aa1703d1d58ac512ce476925`
