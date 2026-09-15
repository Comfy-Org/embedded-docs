# Condicionamento TripoSplat

Este nó codifica uma imagem de entrada com o codificador de imagem DINOv3 e o VAE Flux2 para produzir dados de condicionamento positivo e negativo para o modelo TripoSplat. Ele também cria um alvo de ruído de tamanho fixo (latent + dados de câmera) que serve como ponto de partida para o KSampler.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `clip_vision` | Codificador de imagem DINOv3 ViT-H/16+ | CLIP_VISION | Sim | - |
| `vae` | VAE Flux2 | VAE | Sim | - |
| `imagem` | A imagem de entrada a ser codificada | IMAGE | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-----------|-----------|
| `positive` | Dados de condicionamento positivo contendo a sequência de características do DINOv3 e o latent do VAE Flux2 carregado como um latent de referência | CONDITIONING |
| `negative` | Dados de condicionamento negativo contendo características do DINOv3 preenchidas com zeros e um latent de referência do VAE Flux2 preenchido com zeros | CONDITIONING |
| `latent` | O alvo de ruído de tamanho fixo (latent + câmera) para o KSampler. O latent é uma sequência de shape-code de formato constante (8192 x 16) emparelhada com um único token de câmera (1 x 5) | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `59ebeef272d125a2cc2045f4ff54f99268b1273d0a1fd46f7462e6d312f3a805`
