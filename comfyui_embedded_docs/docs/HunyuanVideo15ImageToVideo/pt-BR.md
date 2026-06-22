# HunyuanVideo15ImageToVideo

O nó HunyuanVideo15ImageToVideo prepara dados de condicionamento e espaço latente para geração de vídeo com base no modelo HunyuanVideo 1.5. Ele cria uma representação latente inicial para uma sequência de vídeo e pode opcionalmente integrar uma imagem inicial ou uma saída do CLIP vision para guiar o processo de geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | Os prompts de condicionamento positivo que descrevem o que o vídeo deve conter. | CONDITIONING | Sim | - |
| `negativo` | Os prompts de condicionamento negativo que descrevem o que o vídeo deve evitar. | CONDITIONING | Sim | - |
| `vae` | O modelo VAE (Autoencoder Variacional) usado para codificar a imagem inicial no espaço latente. | VAE | Sim | - |
| `largura` | A largura dos quadros do vídeo de saída em pixels. Deve ser divisível por 16. (padrão: 848) | INT | Não | 16 a MAX_RESOLUTION |
| `altura` | A altura dos quadros do vídeo de saída em pixels. Deve ser divisível por 16. (padrão: 480) | INT | Não | 16 a MAX_RESOLUTION |
| `duração` | O número total de quadros na sequência de vídeo. Deve ser múltiplo de 4. (padrão: 33) | INT | Não | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | O número de sequências de vídeo a serem geradas em um único lote. (padrão: 1) | INT | Não | 1 a 4096 |
| `imagem_inicial` | Uma imagem inicial opcional para iniciar a geração do vídeo. Se fornecida, é codificada e usada para condicionar os primeiros quadros. Apenas os primeiros `duração` quadros da imagem são utilizados. | IMAGE | Não | - |
| `clip_vision_output` | Embeddings opcionais do CLIP vision para fornecer condicionamento visual adicional para a geração. | CLIP_VISION_OUTPUT | Não | - |

**Observação:** Quando uma `start_image` é fornecida, ela é automaticamente redimensionada para corresponder à `width` e `height` especificadas usando interpolação bilinear. Os primeiros `length` quadros do lote de imagens são utilizados. A imagem codificada é então adicionada tanto ao condicionamento `positive` quanto ao `negative` como uma `concat_latent_image` com uma `concat_mask` correspondente. A máscara é definida como 0.0 para os quadros cobertos pela imagem inicial e 1.0 para os quadros restantes.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | O condicionamento positivo modificado, que agora pode incluir a imagem inicial codificada ou a saída do CLIP vision. | CONDITIONING |
| `negativo` | O condicionamento negativo modificado, que agora pode incluir a imagem inicial codificada ou a saída do CLIP vision. | CONDITIONING |
| `latent` | Um tensor latente vazio com dimensões configuradas para o tamanho do lote, comprimento do vídeo, largura e altura especificados. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2f41bbb080672683fb1755be575f08c79ca03e324df66953eb40631581197d47`
