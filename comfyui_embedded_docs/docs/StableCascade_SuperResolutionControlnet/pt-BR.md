O nó **StableCascade_SuperResolutionControlnet** prepara entradas para o processamento de super-resolução do Stable Cascade. Ele recebe uma imagem de entrada e a codifica usando um VAE para criar a entrada do controlnet, enquanto também gera representações latentes placeholder para o estágio C e o estágio B do pipeline do Stable Cascade.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `imagem` | A imagem de entrada a ser processada para super-resolução | IMAGE | Sim | - |
| `vae` | O modelo VAE usado para codificar a imagem de entrada | VAE | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `controlnet_input` | A representação da imagem codificada, adequada para entrada do controlnet | IMAGE |
| `stage_c` | Representação latente placeholder para o estágio C do processamento Stable Cascade | LATENT |
| `stage_b` | Representação latente placeholder para o estágio B do processamento Stable Cascade | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/pt-BR.md)

---
**Source fingerprint (SHA-256):** `78b6e5a02c48ac37a205ef9d8532a3aca19134de4ec7be98b2ee55969dab7b53`
