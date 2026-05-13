> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/pt-BR.md)

O nó **StableCascade_SuperResolutionControlnet** prepara entradas para o processamento de super-resolução do Stable Cascade. Ele recebe uma imagem de entrada e a codifica usando um VAE para criar a entrada do controlnet, enquanto também gera representações latentes placeholder para o estágio C e o estágio B do pipeline do Stable Cascade.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `imagem` | IMAGE | Sim | - | A imagem de entrada a ser processada para super-resolução |
| `vae` | VAE | Sim | - | O modelo VAE usado para codificar a imagem de entrada |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `controlnet_input` | IMAGE | A representação da imagem codificada, adequada para entrada do controlnet |
| `stage_c` | LATENT | Representação latente placeholder para o estágio C do processamento Stable Cascade |
| `stage_b` | LATENT | Representação latente placeholder para o estágio B do processamento Stable Cascade |

---
**Source fingerprint (SHA-256):** `78b6e5a02c48ac37a205ef9d8532a3aca19134de4ec7be98b2ee55969dab7b53`
