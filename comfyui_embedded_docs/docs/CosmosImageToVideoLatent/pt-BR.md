# CosmosImageToVideoLatent

O nó CosmosImageToVideoLatent cria um latent de vídeo para geração de imagem para vídeo. Ele começa com um latent em branco e pode opcionalmente codificar uma imagem inicial e/ou uma imagem final nos primeiros ou últimos quadros da sequência de vídeo. Quando imagens são fornecidas, ele também gera uma máscara de ruído que marca os quadros codificados como fixos durante a geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `vae` | O modelo VAE usado para codificar as imagens de entrada no espaço latente | VAE | Sim | - |
| `width` | A largura do vídeo de saída em pixels (padrão: 1280) | INT | Sim | 16 a MAX_RESOLUTION (passo 16) |
| `height` | A altura do vídeo de saída em pixels (padrão: 704) | INT | Sim | 16 a MAX_RESOLUTION (passo 16) |
| `length` | O número de quadros na sequência de vídeo (padrão: 121) | INT | Sim | 1 a MAX_RESOLUTION (passo 8) |
| `batch_size` | O número de latents de vídeo a serem gerados no lote de saída (padrão: 1) | INT | Sim | 1 a 4096 |
| `start_image` | Imagem opcional ou sequência de imagens para codificar no início da sequência de vídeo | IMAGE | Não | - |
| `end_image` | Imagem opcional ou sequência de imagens para codificar no final da sequência de vídeo | IMAGE | Não | - |

**Nota:** Quando nem `start_image` nem `end_image` são fornecidos, o nó retorna um latent em branco sem máscara de ruído. Quando pelo menos uma imagem é fornecida, uma `noise_mask` é incluída: os quadros latentes codificados a partir das imagens fornecidas têm valor de máscara 0 (mantidos fixos), enquanto os quadros restantes têm valor de máscara 1 (a serem gerados). As imagens são redimensionadas para a `width` e `height` alvo antes da codificação, e o número de quadros obtidos de uma imagem de entrada é igual à sua dimensão de lote, até um máximo de `length`. O latent tem 16 canais, dimensões espaciais `width / 8` e `height / 8`, e `((length - 1) // 8) + 1` quadros. Quando imagens são fornecidas, o latent e sua máscara de ruído são repetidos `batch_size` vezes para formar o lote de saída.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `latent` | Um LATENT contendo o latent de vídeo `samples` e, quando `start_image` ou `end_image` é fornecido, uma `noise_mask` que marca os quadros codificados como fixos | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0b06ccfcb14c27c81eeebbbff519da1e187970d4cfc19c8796fc3da20688245c`
