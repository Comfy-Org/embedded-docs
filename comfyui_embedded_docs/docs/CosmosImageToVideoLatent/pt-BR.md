# CosmosImageToVideoLatent

O nó CosmosImageToVideoLatent cria uma representação latente de vídeo a partir de imagens de entrada. Ele constrói um latente de vídeo vazio com a largura, a altura e o número de quadros solicitados e, em seguida, opcionalmente codifica uma imagem inicial nos primeiros quadros e/ou uma imagem final nos últimos quadros. Quando imagens são fornecidas, ele também gera uma máscara de ruído para que os quadros codificados permaneçam fixos durante a geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `vae` | O modelo VAE usado para codificar as imagens no espaço latente de vídeo. | VAE | Sim | - |
| `largura` | A largura do vídeo de saída em pixels (padrão: 1280). | INT | Sim | 16 a MAX_RESOLUTION (passo: 16) |
| `altura` | A altura do vídeo de saída em pixels (padrão: 704). | INT | Sim | 16 a MAX_RESOLUTION (passo: 16) |
| `comprimento` | O número total de quadros no vídeo (padrão: 121). | INT | Sim | 1 a MAX_RESOLUTION (passo: 8) |
| `tamanho_do_lote` | O número de latentes de vídeo a serem gerados (padrão: 1). | INT | Sim | 1 a 4096 |
| `imagem_inicial` | Imagem ou sequência de imagens opcional para codificar no início do vídeo. | IMAGE | Não | - |
| `imagem_final` | Imagem ou sequência de imagens opcional para codificar no final do vídeo. | IMAGE | Não | - |

**Observação:**
- Quando nem `start_image` nem `end_image` são fornecidos, o nó retorna um latente vazio sem máscara de ruído.
- Quando `start_image` é fornecido, ele é codificado nos primeiros quadros do latente, e esses quadros são marcados com valor 0 na máscara de ruído (preservados). Quando `end_image` é fornecido, ele é codificado nos últimos quadros, e esses quadros são marcados com valor 0 na máscara de ruído. Os quadros restantes mantêm valor 1 na máscara.
- O latente tem 16 canais e suas dimensões espaciais são `height / 8` por `width / 8`. O número de quadros latentes é `((length - 1) // 8) + 1`.
- `batch_size` repete o latente e, quando presente, a máscara de ruído.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `latent` | O latente de vídeo gerado contendo as imagens inicial e/ou final opcionalmente codificadas e, quando imagens são fornecidas, uma máscara de ruído correspondente com valor 0 nos quadros preservados. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0b06ccfcb14c27c81eeebbbff519da1e187970d4cfc19c8796fc3da20688245c`
