> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/pt-BR.md)

O nó HunyuanVideo15ImageToVideo prepara dados de condicionamento e espaço latente para geração de vídeo com base no modelo HunyuanVideo 1.5. Ele cria uma representação latente inicial para uma sequência de vídeo e pode opcionalmente integrar uma imagem inicial ou uma saída do CLIP vision para guiar o processo de geração.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `positivo` | CONDITIONING | Sim | - | Os prompts de condicionamento positivo que descrevem o que o vídeo deve conter. |
| `negativo` | CONDITIONING | Sim | - | Os prompts de condicionamento negativo que descrevem o que o vídeo deve evitar. |
| `vae` | VAE | Sim | - | O modelo VAE (Autoencoder Variacional) usado para codificar a imagem inicial no espaço latente. |
| `largura` | INT | Não | 16 a MAX_RESOLUTION | A largura dos quadros do vídeo de saída em pixels. Deve ser divisível por 16. (padrão: 848) |
| `altura` | INT | Não | 16 a MAX_RESOLUTION | A altura dos quadros do vídeo de saída em pixels. Deve ser divisível por 16. (padrão: 480) |
| `duração` | INT | Não | 1 a MAX_RESOLUTION | O número total de quadros na sequência de vídeo. Deve ser múltiplo de 4. (padrão: 33) |
| `tamanho_do_lote` | INT | Não | 1 a 4096 | O número de sequências de vídeo a serem geradas em um único lote. (padrão: 1) |
| `imagem_inicial` | IMAGE | Não | - | Uma imagem inicial opcional para iniciar a geração do vídeo. Se fornecida, é codificada e usada para condicionar os primeiros quadros. Apenas os primeiros `duração` quadros da imagem são utilizados. |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Não | - | Embeddings opcionais do CLIP vision para fornecer condicionamento visual adicional para a geração. |

**Observação:** Quando uma `start_image` é fornecida, ela é automaticamente redimensionada para corresponder à `width` e `height` especificadas usando interpolação bilinear. Os primeiros `length` quadros do lote de imagens são utilizados. A imagem codificada é então adicionada tanto ao condicionamento `positive` quanto ao `negative` como uma `concat_latent_image` com uma `concat_mask` correspondente. A máscara é definida como 0.0 para os quadros cobertos pela imagem inicial e 1.0 para os quadros restantes.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `positivo` | CONDITIONING | O condicionamento positivo modificado, que agora pode incluir a imagem inicial codificada ou a saída do CLIP vision. |
| `negativo` | CONDITIONING | O condicionamento negativo modificado, que agora pode incluir a imagem inicial codificada ou a saída do CLIP vision. |
| `latent` | LATENT | Um tensor latente vazio com dimensões configuradas para o tamanho do lote, comprimento do vídeo, largura e altura especificados. |

---
**Source fingerprint (SHA-256):** `2f41bbb080672683fb1755be575f08c79ca03e324df66953eb40631581197d47`
