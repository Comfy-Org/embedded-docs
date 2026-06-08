# Aplicar Condicionamento SeedVR2

Este nó constrói condicionamentos positivo e negativo a partir de um latente VAE para uso com o modelo SeedVR2. Ele prepara os dados de condicionamento que orientam o processo de geração de imagem ou vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `model` | O modelo SeedVR2. | MODEL | Sim | - |
| `vae_conditioning` | O latente VAE para construir o condicionamento. | LATENT | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `model` | O modelo SeedVR2. | MODEL |
| `positive` | O condicionamento positivo para orientar a geração. | CONDITIONING |
| `negative` | O condicionamento negativo para orientar a geração. | CONDITIONING |
| `latent` | As amostras latentes processadas. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8f99c0e712c5c6fc76261d6d72c5c08b7202c77827ecf2549240fc530c1b65bd`
