# WanMoveTrackToVideo

O nó WanMoveTrackToVideo prepara dados de conditioning e latent para geração de vídeo. Ele codifica uma sequência de imagem inicial no espaço latente usando um VAE e pode opcionalmente incorporar informações de rastreamento de movimento para guiar o movimento de objetos no vídeo gerado. O nó gera conditioning positivo e negativo modificados, juntamente com um tensor latente vazio pronto para um modelo de geração de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | A entrada de conditioning positivo a ser modificada. | CONDITIONING | Sim | - |
| `negative` | A entrada de conditioning negativo a ser modificada. | CONDITIONING | Sim | - |
| `vae` | O modelo VAE usado para codificar a imagem inicial no espaço latente. | VAE | Sim | - |
| `tracks` | Dados opcionais de rastreamento de movimento contendo caminhos de objetos. | TRACKS | Não | - |
| `strength` | Força do conditioning de rastreamento. Só tem efeito quando `tracks` é fornecido e o valor é maior que 0.0. (padrão: 1.0) | FLOAT | Sim | 0.0 - 100.0 |
| `width` | A largura do vídeo de saída. Defina em incrementos de 16. (padrão: 832) | INT | Sim | 16 - MAX_RESOLUTION |
| `height` | A altura do vídeo de saída. Defina em incrementos de 16. (padrão: 480) | INT | Sim | 16 - MAX_RESOLUTION |
| `length` | O número de quadros na sequência de vídeo. Defina em incrementos de 4. (padrão: 81) | INT | Sim | 1 - MAX_RESOLUTION |
| `batch_size` | O tamanho do lote para a saída latente. (padrão: 1) | INT | Sim | 1 - 4096 |
| `start_image` | A imagem inicial ou sequência de imagens a ser codificada com o VAE. | IMAGE | Sim | - |
| `clip_vision_output` | Saída opcional do modelo de visão CLIP para adicionar ao conditioning. | CLIP_VISION_OUTPUT | Não | - |

Nota: O movimento baseado em rastreamento é aplicado somente quando `tracks` é fornecido e `strength` é maior que 0.0. Caso contrário, o conditioning recebe a imagem inicial codificada sem modificações. O `start_image` é usado para criar uma imagem latente e uma máscara para o conditioning; se não estiver disponível, o nó apenas repassa o conditioning e gera um latent vazio.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | O conditioning positivo modificado, potencialmente contendo `concat_latent_image`, `concat_mask` e `clip_vision_output`. | CONDITIONING |
| `negative` | O conditioning negativo modificado, potencialmente contendo `concat_latent_image`, `concat_mask` e `clip_vision_output`. | CONDITIONING |
| `latent` | Um tensor latente vazio com dimensões moldadas pelas entradas `batch_size`, `length`, `height` e `width`. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b02a1a359d349a0136d84ed77a510c46cb2c8b565650ed54d5fca6c87cd0ab1f`
