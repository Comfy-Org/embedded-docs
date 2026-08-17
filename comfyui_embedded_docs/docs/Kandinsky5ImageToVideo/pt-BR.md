# Kandinsky5ImageToVideo

O nó Kandinsky5ImageToVideo prepara os dados de condicionamento e de espaço latente para a geração de vídeos usando o modelo Kandinsky. Ele cria um tensor latente de vídeo vazio e pode, opcionalmente, codificar uma imagem inicial para guiar os primeiros quadros do vídeo gerado, modificando o condicionamento positivo e negativo de acordo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | Os prompts de condicionamento positivo para guiar a geração do vídeo. | CONDITIONING | Sim | N/A |
| `negative` | Os prompts de condicionamento negativo para afastar a geração do vídeo de certos conceitos. | CONDITIONING | Sim | N/A |
| `vae` | O modelo VAE usado para codificar a imagem inicial opcional no espaço latente. | VAE | Sim | N/A |
| `width` | A largura do vídeo de saída em pixels (padrão: 768). | INT | Sim | 16 a 8192 (passo 16) |
| `height` | A altura do vídeo de saída em pixels (padrão: 512). | INT | Sim | 16 a 8192 (passo 16) |
| `length` | O número de quadros no vídeo (padrão: 121). | INT | Sim | 1 a 8192 (passo 4) |
| `batch_size` | O número de sequências de vídeo a serem geradas simultaneamente (padrão: 1). | INT | Sim | 1 a 4096 |
| `start_image` | Uma imagem inicial opcional. Se for fornecida, ela é codificada e usada para substituir o início ruidoso dos latentes de saída do modelo. | IMAGE | Não | N/A |

**Nota:** Quando uma `start_image` é fornecida, ela é redimensionada para corresponder à `width` e à `height` especificadas usando interpolação bilinear. Apenas os primeiros `length` quadros da imagem são usados para a codificação. O latente codificado é então injetado tanto no condicionamento `positive` quanto no `negative`, juntamente com uma máscara que marca os quadros iniciais, de modo que a imagem codificada limpa substitui o início ruidoso do vídeo gerado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | O condicionamento positivo modificado, potencialmente atualizado com os dados da imagem inicial codificada. | CONDITIONING |
| `negative` | O condicionamento negativo modificado, potencialmente atualizado com os dados da imagem inicial codificada. | CONDITIONING |
| `latent` | Um tensor latente de vídeo vazio, preenchido com zeros, com formato de acordo com `batch_size`, `length`, `height` e `width` especificados. | LATENT |
| `cond_latent` | A representação latente limpa e codificada das imagens iniciais fornecidas. Usada para substituir o início ruidoso dos latentes de saída do modelo. Vazia quando nenhuma `start_image` é fornecida. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7212f0ea912578d3b72dddf1333a20054a881e3f22c2b8abd9645fc21e75a08b`
