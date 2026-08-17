# Wan22ImageToVideoLatent

O nó Wan22ImageToVideoLatent prepara a entrada latente usada para a geração de vídeos Wan 2.2. Ele cria um latente de vídeo vazio com a largura, a altura e o número de quadros especificados e, quando uma imagem inicial é fornecida, codifica essa imagem nos primeiros quadros do latente. Ele também gera uma máscara de ruído que indica quais quadros já estão preenchidos pela imagem e quais ainda precisam ser gerados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `vae` | O modelo VAE usado para codificar a imagem inicial no espaço latente | VAE | Sim | - |
| `width` | A largura do vídeo de saída em pixels (padrão: 1280, passo: 32) | INT | Sim | 32 a MAX_RESOLUTION |
| `height` | A altura do vídeo de saída em pixels (padrão: 704, passo: 32) | INT | Sim | 32 a MAX_RESOLUTION |
| `length` | O número de quadros no vídeo (padrão: 49, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `batch_size` | O número de latentes de vídeo a serem gerados em paralelo (padrão: 1) | INT | Sim | 1 a 4096 |
| `start_image` | Imagem ou sequência de imagens opcional colocada nos primeiros quadros do latente de vídeo. Apenas os primeiros `length` quadros são usados. A imagem é redimensionada para `width` x `height` com reamostragem bilinear e corte central antes de ser codificada pelo VAE. | IMAGE | Não | - |

**Nota:** As dimensões espaciais do latente são `width / 16` e `height / 16`, portanto `width` e `height` devem ser divisíveis por 16. A dimensão temporal do latente é calculada como `((length - 1) // 4) + 1` e possui 48 canais. Quando um `start_image` é fornecido, a imagem codificada preenche os primeiros quadros do latente e a `noise_mask` é definida como 0 para esses quadros e 1 para os quadros restantes, o que indica ao amostrador para manter os quadros da imagem inalterados e gerar o restante. Quando nenhum `start_image` é fornecido, o latente é preenchido com zeros e nenhuma máscara de ruído é incluída.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `LATENT` | O latente de vídeo gerado, repetido `batch_size` vezes. Quando um `start_image` é fornecido, ele também contém uma `noise_mask` que marca os quadros codificados pela imagem (0) e os quadros a gerar (1). | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3d05980641eeef2e86df7a845aa8b2bd703882db98fe71adef2746ab34a9d717`
