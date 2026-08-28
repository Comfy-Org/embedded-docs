# HunyuanVideo15ImageToVideo

O nó HunyuanVideo15ImageToVideo prepara dados de condicionamento e espaço latente para geração de vídeo com base no modelo HunyuanVideo 1.5. Ele cria uma representação latente inicial para uma sequência de vídeo e pode opcionalmente integrar uma imagem inicial ou uma saída de visão do CLIP para orientar o processo de geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | Os prompts de condicionamento positivos que descrevem o que o vídeo deve conter. | CONDITIONING | Sim | - |
| `negativo` | Os prompts de condicionamento negativos que descrevem o que o vídeo deve evitar. | CONDITIONING | Sim | - |
| `vae` | O modelo VAE (Autoencoder Variacional) usado para codificar a imagem inicial no espaço latente. | VAE | Sim | - |
| `largura` | A largura dos quadros de vídeo de saída em pixels. Deve ser divisível por 16. (padrão: 848) | INT | Sim | 16 to MAX_RESOLUTION, step: 16 |
| `altura` | A altura dos quadros de vídeo de saída em pixels. Deve ser divisível por 16. (padrão: 480) | INT | Sim | 16 to MAX_RESOLUTION, step: 16 |
| `duração` | O número total de quadros na sequência de vídeo. Os valores aumentam em passos de 4 a partir de 1 (1, 5, 9, 13, ...). (padrão: 33) | INT | Sim | 1 to MAX_RESOLUTION, step: 4 |
| `tamanho_do_lote` | O número de sequências de vídeo a serem geradas em um único lote. (padrão: 1) | INT | Sim | 1 a 4096 |
| `imagem_inicial` | Uma imagem inicial opcional para inicializar a geração de vídeo. Se fornecida, ela é codificada e usada para condicionar os primeiros quadros. Apenas os primeiros `length` quadros da imagem são usados. | IMAGE | Não | - |
| `clip_vision_output` | Embeddings de visão CLIP opcionais para fornecer condicionamento visual adicional para a geração. | CLIP_VISION_OUTPUT | Não | - |

**Nota:** Quando uma `start_image` é fornecida, ela é automaticamente redimensionada para corresponder à `width` e `height` especificadas usando interpolação bilinear. Os primeiros `length` quadros do lote de imagens são usados, e apenas os 3 primeiros canais de cores de cada quadro são codificados. A imagem codificada é então adicionada tanto ao condicionamento `positive` quanto ao `negative` como um `concat_latent_image` com um `concat_mask` correspondente. A máscara é definida como 0.0 para os quadros cobertos pela imagem inicial e 1.0 para os quadros restantes. Quando um `clip_vision_output` é fornecido, ele também é adicionado tanto ao condicionamento `positive` quanto ao `negative`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positivo` | O condicionamento positivo modificado, que agora pode incluir a imagem inicial codificada ou a saída de visão do CLIP. | CONDITIONING |
| `negativo` | O condicionamento negativo modificado, que agora pode incluir a imagem inicial codificada ou a saída de visão do CLIP. | CONDITIONING |
| `latente` | Um tensor latente vazio com dimensões configuradas para o tamanho do lote, comprimento do vídeo, largura e altura especificados. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `dbedf7f378ae9613c8f47fe9876a4576c815055b4cdb6bf687b7575fcd7ea80a`
