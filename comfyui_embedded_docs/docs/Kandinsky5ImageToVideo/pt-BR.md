O nó Kandinsky5ImageToVideo prepara dados de condicionamento e espaço latente para geração de vídeo usando o modelo Kandinsky. Ele cria um tensor latente de vídeo vazio e pode opcionalmente codificar uma imagem inicial para guiar os primeiros quadros do vídeo gerado, modificando o condicionamento positivo e negativo de acordo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | Os prompts de condicionamento positivo para guiar a geração do vídeo. | CONDITIONING | Sim | N/A |
| `negativo` | Os prompts de condicionamento negativo para afastar a geração do vídeo de certos conceitos. | CONDITIONING | Sim | N/A |
| `vae` | O modelo VAE usado para codificar a imagem inicial opcional no espaço latente. | VAE | Sim | N/A |
| `largura` | A largura do vídeo de saída em pixels (padrão: 768). | INT | Não | 16 a 8192 (passo 16) |
| `altura` | A altura do vídeo de saída em pixels (padrão: 512). | INT | Não | 16 a 8192 (passo 16) |
| `duração` | O número de quadros no vídeo (padrão: 121). | INT | Não | 1 a 8192 (passo 4) |
| `tamanho_do_lote` | O número de sequências de vídeo a serem geradas simultaneamente (padrão: 1). | INT | Não | 1 a 4096 |
| `imagem_inicial` | Uma imagem inicial opcional. Se fornecida, é codificada e usada para substituir o início ruidoso dos latentes de saída do modelo. | IMAGE | Não | N/A |

**Observação:** Quando uma `start_image` é fornecida, ela é automaticamente redimensionada para corresponder à `width` e `height` especificadas usando interpolação bilinear. Os primeiros `length` quadros do lote de imagens são usados para codificação. O latente codificado é então injetado tanto no condicionamento `positive` quanto no `negative` para guiar a aparência inicial do vídeo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | O condicionamento positivo modificado, potencialmente atualizado com dados da imagem inicial codificada. | CONDITIONING |
| `negativo` | O condicionamento negativo modificado, potencialmente atualizado com dados da imagem inicial codificada. | CONDITIONING |
| `latent` | Um tensor latente de vídeo vazio com zeros, formatado para as dimensões especificadas. | LATENT |
| `cond_latent` | A representação latente limpa e codificada das imagens iniciais fornecidas. Isso é usado internamente para substituir o início ruidoso dos latentes do vídeo gerado. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `19d3b60be18f5adcd659563329988bce2511a1b27b33fd0ab3a9d93e265557f2`
