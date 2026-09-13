# CosmosPredict2ImageToVideoLatent

Cria latentes de vídeo para o fluxo de trabalho de imagem para vídeo do Cosmos Predict2. O nó pode produzir um latente de vídeo vazio com determinado tamanho e comprimento, ou inserir imagens inicial e/ou final codificadas na sequência para que esses quadros sejam preservados durante a geração. Qualquer imagem fornecida é redimensionada para os `width` e `height` solicitados e codificada com o VAE fornecido antes de ser posicionada no início e/ou no final da sequência latente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `vae` | O modelo VAE usado para codificar as imagens inicial e final no espaço latente | VAE | Sim | - |
| `width` | Largura do vídeo de saída em pixels (padrão: 848, deve ser múltiplo de 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `height` | Altura do vídeo de saída em pixels (padrão: 480, deve ser múltiplo de 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `length` | Número de quadros na sequência de vídeo (padrão: 93) | INT | Sim | 1 a MAX_RESOLUTION |
| `batch_size` | Número de sequências de vídeo a gerar (padrão: 1) | INT | Sim | 1 a 4096 |
| `start_image` | Imagem inicial opcional para a sequência de vídeo | IMAGE | Não | - |
| `end_image` | Imagem final opcional para a sequência de vídeo | IMAGE | Não | - |

**Nota:** Quando nem `start_image` nem `end_image` forem fornecidos, o nó simplesmente retorna um latente vazio do tamanho e comprimento solicitados. Quando uma ou ambas as imagens forem fornecidas, elas são redimensionadas para `width` e `height`, codificadas com o `vae` e posicionadas no início e/ou no final da sequência latente. As regiões correspondentes são marcadas na máscara de ruído para que sejam preservadas durante a geração. Os latentes codificados são convertidos com o formato de latente Wan 2.1, e o latente e a máscara resultantes são repetidos `batch_size` vezes.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `LATENT` | O latente de vídeo gerado contendo `samples` (a sequência de latente de vídeo) e, quando pelo menos um entre `start_image` ou `end_image` for fornecido, um `noise_mask` que marca os quadros que devem ser preservados durante a geração | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `842bd2b8cda438e7b938439d4eba280478939e3302dc1846d52595d40082ff05`
