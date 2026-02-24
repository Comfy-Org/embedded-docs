> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/pt-BR.md)

O nó HunyuanVideo15ImageToVideo prepara dados de condicionamento e espaço latente para geração de vídeo baseada no modelo HunyuanVideo 1.5. Ele cria uma representação latente inicial para uma sequência de vídeo e pode, opcionalmente, integrar uma imagem inicial ou uma saída de visão CLIP para orientar o processo de geração.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | Os prompts de condicionamento positivo que descrevem o que o vídeo deve conter. |
| `negative` | CONDITIONING | Sim | - | Os prompts de condicionamento negativo que descrevem o que o vídeo deve evitar. |
| `vae` | VAE | Sim | - | O modelo VAE (Variational Autoencoder) usado para codificar a imagem inicial no espaço latente. |
| `width` | INT | Não | 16 até MAX_RESOLUTION | A largura dos quadros do vídeo de saída em pixels. Deve ser divisível por 16. (padrão: 848) |
| `height` | INT | Não | 16 até MAX_RESOLUTION | A altura dos quadros do vídeo de saída em pixels. Deve ser divisível por 16. (padrão: 480) |
| `length` | INT | Não | 1 até MAX_RESOLUTION | O número total de quadros na sequência de vídeo. (padrão: 33) |
| `batch_size` | INT | Não | 1 até 4096 | O número de sequências de vídeo a serem geradas em um único lote. (padrão: 1) |
| `start_image` | IMAGE | Não | - | Uma imagem inicial opcional para iniciar a geração do vídeo. Se fornecida, ela é codificada e usada para condicionar os primeiros quadros. |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Não | - | Embeddings de visão CLIP opcionais para fornecer condicionamento visual adicional para a geração. |

**Observação:** Quando uma `start_image` é fornecida, ela é redimensionada automaticamente para corresponder à `width` e `height` especificadas usando interpolação bilinear. Os primeiros `length` quadros do lote de imagens são usados. A imagem codificada é então adicionada tanto ao condicionamento `positive` quanto ao `negative` como um `concat_latent_image` com uma `concat_mask` correspondente.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | O condicionamento positivo modificado, que agora pode incluir a imagem inicial codificada ou a saída de visão CLIP. |
| `negative` | CONDITIONING | O condicionamento negativo modificado, que agora pode incluir a imagem inicial codificada ou a saída de visão CLIP. |
| `latent` | LATENT | Um tensor latente vazio com dimensões configuradas para o tamanho do lote, duração do vídeo, largura e altura especificados. |
