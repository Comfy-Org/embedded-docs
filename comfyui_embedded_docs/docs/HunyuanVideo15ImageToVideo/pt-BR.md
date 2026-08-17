# HunyuanVideo15ImageToVideo

O nó HunyuanVideo15ImageToVideo prepara dados de condicionamento e espaço latente para a geração de vídeos com base no modelo HunyuanVideo 1.5. Ele cria uma representação latente inicial para uma sequência de vídeo e pode, opcionalmente, integrar uma imagem inicial ou uma saída do CLIP vision para orientar o processo de geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positive` | Os prompts de condicionamento positivo que descrevem o que o vídeo deve conter. | CONDITIONING | Sim | - |
| `negative` | Os prompts de condicionamento negativo que descrevem o que o vídeo deve evitar. | CONDITIONING | Sim | - |
| `vae` | O modelo VAE (Autoencoder Variacional) usado para codificar a imagem inicial no espaço latente. | VAE | Sim | - |
| `width` | A largura dos quadros de vídeo de saída em pixels. Deve ser divisível por 16. (padrão: 848) | INT | Sim | 16 to MAX_RESOLUTION, step: 16 |
| `height` | A altura dos quadros de vídeo de saída em pixels. Deve ser divisível por 16. (padrão: 480) | INT | Sim | 16 to MAX_RESOLUTION, step: 16 |
| `length` | O número total de quadros na sequência de vídeo. O valor aumenta em passos de 4. (padrão: 33) | INT | Sim | 1 to MAX_RESOLUTION, step: 4 |
| `batch_size` | O número de sequências de vídeo a serem geradas em um único lote. (padrão: 1) | INT | Sim | 1 to 4096 |
| `start_image` | Uma imagem inicial opcional para inicializar a geração do vídeo. Se fornecida, ela é codificada e usada para condicionar os primeiros quadros. Apenas os primeiros `length` quadros da imagem são usados. | IMAGE | Não | - |
| `clip_vision_output` | Embeddings CLIP vision opcionais para fornecer condicionamento visual adicional para a geração. | CLIP_VISION_OUTPUT | Não | - |

**Nota:** Quando uma `start_image` é fornecida, ela é automaticamente redimensionada para corresponder à `width` e `height` especificadas usando interpolação bilinear, e apenas seus canais RGB são usados. Os primeiros `length` quadros do lote de imagens são usados. A imagem codificada é então adicionada tanto ao condicionamento `positive` quanto ao `negative` como um `concat_latent_image` com um `concat_mask` correspondente. A máscara é definida como 0.0 para os quadros cobertos pela imagem inicial e 1.0 para os quadros restantes. Quando um `clip_vision_output` é fornecido, ele também é adicionado tanto ao condicionamento `positive` quanto ao `negative`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | O condicionamento positivo modificado, que agora pode incluir a imagem inicial codificada ou a saída do CLIP vision. | CONDITIONING |
| `negative` | O condicionamento negativo modificado, que agora pode incluir a imagem inicial codificada ou a saída do CLIP vision. | CONDITIONING |
| `latent` | Um tensor latente vazio com dimensões configuradas para o tamanho do lote, comprimento do vídeo, largura e altura especificados. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `dbedf7f378ae9613c8f47fe9876a4576c815055b4cdb6bf687b7575fcd7ea80a`
