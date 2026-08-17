# Aplicar Condicionamento SeedVR2

Este nó constrói condicionamentos positivo e negativo a partir de um latent de VAE para uso com o modelo SeedVR2. Ele adiciona um canal de máscara ao latent e então o combina com os embeddings de condicionamento positivo e negativo integrados do modelo para produzir os valores de condicionamento necessários para a amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `model` | O modelo SeedVR2. | MODEL | Sim | - |
| `vae_conditioning` | O latent de VAE a partir do qual o condicionamento é construído. Nome de exibição: latent. | LATENT | Sim | - |

O latent `vae_conditioning` deve ser um tensor 5-D no layout channel-first do Comfy (B, C, T, H, W) com o número de canais esperado pelo VAE do SeedVR2. Latents com layout channel-last são rejeitados com erro. A entrada `model` deve ser um modelo SeedVR2 válido com a estrutura interna esperada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `positive` | O condicionamento positivo para a amostragem. | CONDITIONING |
| `negative` | O condicionamento negativo para a amostragem. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `28e508bdd776e2e3f5f2f93bfc29a1a1d1c34a11dbdc7f421d197ddbfa85f0f5`
