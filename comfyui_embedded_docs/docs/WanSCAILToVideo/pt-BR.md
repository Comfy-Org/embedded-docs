# WanSCAILToVideo

O nó WanSCAILToVideo prepara o condicionamento e um espaço latente vazio para geração de vídeos. Ele processa entradas opcionais como imagens de referência, vídeos de pose e saídas do CLIP vision, incorporando-as no condicionamento positivo e negativo para um modelo de vídeo. O nó gera o condicionamento modificado e um tensor latente em branco com as dimensões de vídeo especificadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | A entrada de condicionamento positivo. | CONDITIONING | Sim | - |
| `negativo` | A entrada de condicionamento negativo. | CONDITIONING | Sim | - |
| `vae` | O modelo VAE usado para codificar imagens e quadros de vídeo. | VAE | Sim | - |
| `largura` | A largura do vídeo de saída em pixels (padrão: 512). Deve ser divisível por 8. | INT | Sim | 32 a MAX_RESOLUTION |
| `altura` | A altura do vídeo de saída em pixels (padrão: 896). Deve ser divisível por 8. | INT | Sim | 32 a MAX_RESOLUTION |
| `duração` | O número de quadros no vídeo (padrão: 81). Deve ser divisível por 4. | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | O número de vídeos a serem gerados em um lote (padrão: 1). | INT | Sim | 1 a 4096 |
| `clip_vision_output` | Saída opcional do CLIP vision para condicionamento. | CLIP_VISION_OUTPUT | Não | - |
| `imagem_de_referência` | Uma imagem de referência opcional para condicionamento. | IMAGE | Não | - |
| `vídeo_de_pose` | Vídeo usado para condicionamento de pose. Será redimensionado para metade da resolução do vídeo principal. | IMAGE | Não | - |
| `força_da_pose` | Intensidade do latente de pose (padrão: 1.0). | FLOAT | Sim | 0.0 a 10.0 |
| `início_da_pose` | Etapa inicial para usar o condicionamento de pose (padrão: 0.0). | FLOAT | Sim | 0.0 a 1.0 |
| `fim_da_pose` | Etapa final para usar o condicionamento de pose (padrão: 1.0). | FLOAT | Sim | 0.0 a 1.0 |

**Observação:** A entrada `pose_video` é processada apenas para os primeiros `length` quadros. A `reference_image` é processada apenas para a primeira imagem do lote. Quando `reference_image` é fornecida, um latente preenchido com zeros do mesmo tamanho é usado para o condicionamento negativo. Quando `clip_vision_output` é fornecido, ele é aplicado tanto ao condicionamento positivo quanto ao negativo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | O condicionamento positivo modificado, potencialmente contendo latentes de imagem de referência incorporados, saída do CLIP vision ou latentes de vídeo de pose. | CONDITIONING |
| `negativo` | O condicionamento negativo modificado, potencialmente contendo latentes de imagem de referência incorporados, saída do CLIP vision ou latentes de vídeo de pose. | CONDITIONING |
| `latent` | Um tensor latente vazio com formato `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]`. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `63de4b6fe41fc23ea81c21965a2dbfc82120bb1bad6785b2130af824e015fbcb`
