# WanMoveTrackToVideo

O nó WanMoveTrackToVideo prepara dados de condicionamento e espaço latente para geração de vídeo, incorporando informações opcionais de rastreamento de movimento. Ele codifica uma sequência de imagens iniciais em uma representação latente e pode mesclar dados posicionais de rastros de objetos para guiar o movimento no vídeo gerado. O nó gera condicionamentos positivo e negativo modificados, juntamente com um tensor latente vazio pronto para um modelo de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | A entrada de condicionamento positivo a ser modificada. | CONDITIONING | Sim | - |
| `negativo` | A entrada de condicionamento negativo a ser modificada. | CONDITIONING | Sim | - |
| `vae` | O modelo VAE usado para codificar a imagem inicial no espaço latente. | VAE | Sim | - |
| `trilhas` | Dados opcionais de rastreamento de movimento contendo caminhos de objetos. | TRACKS | Não | - |
| `força` | Intensidade do condicionamento do rastro. (padrão: 1,0) | FLOAT | Não | 0,0 - 100,0 |
| `largura` | A largura do vídeo de saída. Deve ser divisível por 16. (padrão: 832) | INT | Não | 16 - RESOLUÇÃO_MÁXIMA |
| `altura` | A altura do vídeo de saída. Deve ser divisível por 16. (padrão: 480) | INT | Não | 16 - RESOLUÇÃO_MÁXIMA |
| `comprimento` | O número de quadros na sequência de vídeo. (padrão: 81) | INT | Não | 1 - RESOLUÇÃO_MÁXIMA |
| `tamanho_do_lote` | O tamanho do lote para a saída latente. (padrão: 1) | INT | Não | 1 - 4096 |
| `imagem_inicial` | A imagem ou sequência de imagens inicial a ser codificada. | IMAGE | Sim | - |
| `clip_vision_output` | Saída opcional do modelo de visão CLIP para adicionar ao condicionamento. | CLIPVISIONOUTPUT | Não | - |

**Observação:** O parâmetro `strength` só tem efeito quando `tracks` são fornecidos. Se `tracks` não forem fornecidos ou `strength` for 0,0, o condicionamento do rastro não é aplicado. A `start_image` é usada para criar uma imagem latente e uma máscara para o condicionamento; se não for fornecida, o nó apenas repassa o condicionamento e gera um latente vazio.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | O condicionamento positivo modificado, potencialmente contendo `concat_latent_image`, `concat_mask` e `clip_vision_output`. | CONDITIONING |
| `negativo` | O condicionamento negativo modificado, potencialmente contendo `concat_latent_image`, `concat_mask` e `clip_vision_output`. | CONDITIONING |
| `latent` | Um tensor latente vazio com dimensões definidas pelas entradas `tamanho_do_lote`, `comprimento`, `altura` e `largura`. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9677addf5b94b42efd3015f51380c1fa9b16d4a5105cc7f24de0be34c0042bbc`
