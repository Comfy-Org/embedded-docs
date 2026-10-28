# MiniMax H3 Latent Upscale With Model

O nó MiniMax H3 Latent Upscale With Model redimensiona a parte de vídeo de um latente do MiniMax H3 para uma largura e altura alvo usando um modelo de upscale de latente. O latente de áudio segue intacto, então o clipe mantém seu som, e não é necessária reamostragem. Use-o após a amostragem do MiniMax H3 e antes da decodificação do H3 VAE quando o clipe deve sair maior.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo de upscale de latente, geralmente carregado com Load Latent Upscale Model. Precisa ser um upscaler de latente com convolução 3D do MiniMax H3. | LATENT_UPSCALE_MODEL | Sim | - |
| `samples` | Latente do MiniMax H3 a ser redimensionado. Um latente aninhado mantém sua parte de áudio como está. | LATENT | Sim | - |
| `width` | Largura alvo do vídeo em pixels. O latente é redimensionado para `width / 16` colunas, então o valor é arredondado para baixo para um múltiplo de 16. (padrão: 2560) | INT | Sim | 32 a 16384 (passo 32) |
| `height` | Altura alvo do vídeo em pixels, também arredondada para baixo para um múltiplo de 16. (padrão: 1440) | INT | Sim | 32 a 16384 (passo 32) |

Quando o tamanho solicitado já corresponde ao latente, o latente de entrada é retornado sem alterações. O latente de saída não carrega `noise_mask`, então um latente parcialmente mascarado perde sua máscara. A rede executa suas convoluções 3D em fatias temporais, o que mantém o uso de memória em clipes longos próximo ao de uma única fatia.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `LATENT` | O latente redimensionado, pronto para a decodificação do H3 VAE. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3LatentUpscaleWithModel/pt-BR.md)

---
**Source fingerprint (SHA-256):** `cd659baace5a21620033dd3470b854cccbada01d09545a2f61273b949c3a004b`
