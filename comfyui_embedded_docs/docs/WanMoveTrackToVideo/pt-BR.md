# WanMoveTrackToVideo

O nó WanMoveTrackToVideo prepara os dados de condicionamento e de espaço latente para a geração de vídeo, incorporando informações opcionais de rastreamento de movimento. Ele codifica uma sequência de imagens inicial em uma representação latente e pode incorporar dados posicionais das trajetórias de objetos para orientar o movimento no vídeo gerado. O nó gera condicionamentos positivo e negativo modificados, juntamente com um tensor latente vazio pronto para um modelo de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | A entrada de condicionamento positivo a ser modificada. | CONDITIONING | Sim | - |
| `negativo` | A entrada de condicionamento negativo a ser modificada. | CONDITIONING | Sim | - |
| `vae` | O modelo VAE usado para codificar a imagem inicial no espaço latente. | VAE | Sim | - |
| `trilhas` | Dados opcionais de rastreamento de movimento contendo as trajetórias de objetos. | TRACKS | Não | - |
| `força` | Intensidade do condicionamento por trajetórias. (padrão: 1.0) | FLOAT | Sim | 0.0 - 100.0 |
| `largura` | A largura do vídeo de saída. Deve ser divisível por 16. (padrão: 832) | INT | Sim | 16 - MAX_RESOLUTION |
| `altura` | A altura do vídeo de saída. Deve ser divisível por 16. (padrão: 480) | INT | Sim | 16 - MAX_RESOLUTION |
| `comprimento` | O número de quadros na sequência de vídeo, em incrementos de 4. (padrão: 81) | INT | Sim | 1 - MAX_RESOLUTION |
| `tamanho_do_lote` | O tamanho do lote para a saída latente. (padrão: 1) | INT | Sim | 1 - 4096 |
| `imagem_inicial` | A imagem inicial ou sequência de imagens a ser codificada. | IMAGE | Sim | - |
| `clip_vision_output` | Saída opcional do modelo de visão CLIP a ser adicionada ao condicionamento. | CLIP_VISION_OUTPUT | Não | - |

**Observação:** O parâmetro `strength` só tem efeito quando `tracks` é fornecido e `strength` é maior que 0.0; o condicionamento por trajetórias é aplicado somente quando `start_image` também é fornecido. Se `tracks` não for fornecido ou `strength` for 0.0, a combinação de trajetórias é ignorada. Quando a combinação de trajetórias está ativa, o condicionamento positivo recebe a imagem latente mesclada com as trajetórias, enquanto o condicionamento negativo recebe a imagem latente não modificada. Se `start_image` não for fornecido, nenhum condicionamento de imagem latente e máscara é criado; os condicionamentos positivo e negativo passam inalterados (exceto que `clip_vision_output` ainda é adicionado se fornecido), e o nó emite um latente vazio.

**Observação:** Quando `start_image` é fornecido, a sequência de imagens é redimensionada para a `width` e `height` alvo e truncada para os primeiros `length` quadros. Se a sequência for mais curta que `length`, os quadros restantes são preenchidos com quadros cinza neutros (valor 0.5) antes da codificação pelo VAE. O condicionamento resultante inclui um `concat_mask` com valor 0 nas posições temporais correspondentes aos quadros da imagem inicial e 1 nas demais.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positivo` | O condicionamento positivo modificado, potencialmente contendo `concat_latent_image`, `concat_mask` e `clip_vision_output`. | CONDITIONING |
| `negativo` | O condicionamento negativo modificado, potencialmente contendo `concat_latent_image`, `concat_mask` e `clip_vision_output`. | CONDITIONING |
| `latent` | Um tensor latente vazio com formato `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]`, determinado pelas entradas `batch_size`, `length`, `height` e `width`. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b02a1a359d349a0136d84ed77a510c46cb2c8b565650ed54d5fca6c87cd0ab1f`
