> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/pt-BR.md)

O nó WanSCAILToVideo prepara o condicionamento e um espaço latente vazio para geração de vídeos. Ele processa entradas opcionais como imagens de referência, vídeos de pose e saídas do CLIP vision, incorporando-as no condicionamento positivo e negativo para um modelo de vídeo. O nó gera o condicionamento modificado e um tensor latente em branco com as dimensões de vídeo especificadas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `positive` | CONDITIONING | Sim | - | A entrada de condicionamento positivo. |
| `negative` | CONDITIONING | Sim | - | A entrada de condicionamento negativo. |
| `vae` | VAE | Sim | - | O modelo VAE usado para codificar imagens e quadros de vídeo. |
| `width` | INT | Sim | 32 a MAX_RESOLUTION | A largura do vídeo de saída em pixels (padrão: 512). Deve ser divisível por 8. |
| `height` | INT | Sim | 32 a MAX_RESOLUTION | A altura do vídeo de saída em pixels (padrão: 896). Deve ser divisível por 8. |
| `length` | INT | Sim | 1 a MAX_RESOLUTION | O número de quadros no vídeo (padrão: 81). Deve ser divisível por 4. |
| `batch_size` | INT | Sim | 1 a 4096 | O número de vídeos a serem gerados em um lote (padrão: 1). |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Não | - | Saída opcional do CLIP vision para condicionamento. |
| `reference_image` | IMAGE | Não | - | Uma imagem de referência opcional para condicionamento. |
| `pose_video` | IMAGE | Não | - | Vídeo usado para condicionamento de pose. Será redimensionado para metade da resolução do vídeo principal. |
| `pose_strength` | FLOAT | Sim | 0.0 a 10.0 | Intensidade do latente de pose (padrão: 1.0). |
| `pose_start` | FLOAT | Sim | 0.0 a 1.0 | Etapa inicial para usar o condicionamento de pose (padrão: 0.0). |
| `pose_end` | FLOAT | Sim | 0.0 a 1.0 | Etapa final para usar o condicionamento de pose (padrão: 1.0). |

**Observação:** A entrada `pose_video` é processada apenas para os primeiros `length` quadros. A `reference_image` é processada apenas para a primeira imagem do lote. Quando `reference_image` é fornecida, um latente preenchido com zeros do mesmo tamanho é usado para o condicionamento negativo. Quando `clip_vision_output` é fornecido, ele é aplicado tanto ao condicionamento positivo quanto ao negativo.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `positive` | CONDITIONING | O condicionamento positivo modificado, potencialmente contendo latentes de imagem de referência incorporados, saída do CLIP vision ou latentes de vídeo de pose. |
| `negative` | CONDITIONING | O condicionamento negativo modificado, potencialmente contendo latentes de imagem de referência incorporados, saída do CLIP vision ou latentes de vídeo de pose. |
| `latent` | LATENT | Um tensor latente vazio com formato `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]`. |

---
**Source fingerprint (SHA-256):** `63de4b6fe41fc23ea81c21965a2dbfc82120bb1bad6785b2130af824e015fbcb`
