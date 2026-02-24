> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/pt-BR.md)

O nó WanMoveTrackToVideo prepara dados de condicionamento e do espaço latente para geração de vídeo, incorporando informações opcionais de rastreamento de movimento. Ele codifica uma sequência de imagem inicial em uma representação latente e pode mesclar dados posicionais de trilhas de objetos para orientar o movimento no vídeo gerado. O nó produz condicionamentos positivo e negativo modificados, juntamente com um tensor latente vazio pronto para um modelo de vídeo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | A entrada de condicionamento positivo a ser modificada. |
| `negative` | CONDITIONING | Sim | - | A entrada de condicionamento negativo a ser modificada. |
| `vae` | VAE | Sim | - | O modelo VAE usado para codificar a imagem inicial no espaço latente. |
| `tracks` | TRACKS | Não | - | Dados opcionais de rastreamento de movimento contendo caminhos de objetos. |
| `strength` | FLOAT | Não | 0.0 - 100.0 | Intensidade do condicionamento por trilha. (padrão: 1.0) |
| `width` | INT | Não | 16 - MAX_RESOLUTION | A largura do vídeo de saída. Deve ser divisível por 16. (padrão: 832) |
| `height` | INT | Não | 16 - MAX_RESOLUTION | A altura do vídeo de saída. Deve ser divisível por 16. (padrão: 480) |
| `length` | INT | Não | 1 - MAX_RESOLUTION | O número de quadros na sequência de vídeo. (padrão: 81) |
| `batch_size` | INT | Não | 1 - 4096 | O tamanho do lote para a saída latente. (padrão: 1) |
| `start_image` | IMAGE | Sim | - | A imagem inicial ou sequência de imagens a ser codificada. |
| `clip_vision_output` | CLIPVISIONOUTPUT | Não | - | Saída opcional do modelo de visão CLIP para adicionar ao condicionamento. |

**Observação:** O parâmetro `strength` só tem efeito quando `tracks` são fornecidos. Se `tracks` não forem fornecidos ou `strength` for 0.0, o condicionamento por trilha não é aplicado. A `start_image` é usada para criar uma imagem latente e uma máscara para o condicionamento; se não for fornecida, o nó apenas repassa o condicionamento e gera um latente vazio.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | O condicionamento positivo modificado, potencialmente contendo `concat_latent_image`, `concat_mask` e `clip_vision_output`. |
| `negative` | CONDITIONING | O condicionamento negativo modificado, potencialmente contendo `concat_latent_image`, `concat_mask` e `clip_vision_output`. |
| `latent` | LATENT | Um tensor latente vazio com dimensões moldadas pelas entradas `batch_size`, `length`, `height` e `width`. |
