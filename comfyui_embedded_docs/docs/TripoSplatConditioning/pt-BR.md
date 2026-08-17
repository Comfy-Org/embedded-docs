# Condicionamento TripoSplat

Este nó codifica uma imagem de entrada usando o codificador de visão DINOv3 e o VAE do Flux2 para criar dados de condicionamento positivo e negativo para o modelo TripoSplat. Ele também gera um alvo de ruído de tamanho fixo (uma sequência latente mais token de câmera) que serve como ponto de partida para o KSampler.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `clip_vision` | Codificador de imagem DINOv3 ViT-H/16+ | CLIP_VISION | Sim | - |
| `vae` | VAE do Flux2 | VAE | Sim | - |
| `image` | A imagem de entrada a ser codificada | IMAGE | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | Dados de condicionamento positivo contendo as características de imagem do DINOv3 e o latente do VAE Flux2 da imagem de entrada | CONDITIONING |
| `negative` | Dados de condicionamento negativo contendo características DINOv3 preenchidas com zeros e latente do VAE Flux2 preenchido com zeros | CONDITIONING |
| `latent` | O alvo de ruído de tamanho fixo (latente + câmera) para o KSampler | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `59ebeef272d125a2cc2045f4ff54f99268b1273d0a1fd46f7462e6d312f3a805`
