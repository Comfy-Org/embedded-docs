> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/pt-BR.md)

O nó Kandinsky5ImageToVideo prepara dados de condicionamento e espaço latente para geração de vídeo usando o modelo Kandinsky. Ele cria um tensor latente de vídeo vazio e pode, opcionalmente, codificar uma imagem inicial para orientar os quadros iniciais do vídeo gerado, modificando o condicionamento positivo e negativo de acordo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | N/A | Os prompts de condicionamento positivo para orientar a geração do vídeo. |
| `negative` | CONDITIONING | Sim | N/A | Os prompts de condicionamento negativo para afastar a geração do vídeo de certos conceitos. |
| `vae` | VAE | Sim | N/A | O modelo VAE usado para codificar a imagem inicial opcional no espaço latente. |
| `width` | INT | Não | 16 a 8192 (passo 16) | A largura do vídeo de saída em pixels (padrão: 768). |
| `height` | INT | Não | 16 a 8192 (passo 16) | A altura do vídeo de saída em pixels (padrão: 512). |
| `length` | INT | Não | 1 a 8192 (passo 4) | O número de quadros no vídeo (padrão: 121). |
| `batch_size` | INT | Não | 1 a 4096 | O número de sequências de vídeo a serem geradas simultaneamente (padrão: 1). |
| `start_image` | IMAGE | Não | N/A | Uma imagem inicial opcional. Se fornecida, ela é codificada e usada para substituir o início ruidoso dos latentes de saída do modelo. |

**Observação:** Quando uma `start_image` é fornecida, ela é redimensionada automaticamente para corresponder à `width` e `height` especificadas usando interpolação bilinear. Os primeiros `length` quadros do lote de imagens são usados para a codificação. O latente codificado é então injetado tanto no condicionamento `positive` quanto no `negative` para orientar a aparência inicial do vídeo.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | O condicionamento positivo modificado, potencialmente atualizado com os dados da imagem inicial codificada. |
| `negative` | CONDITIONING | O condicionamento negativo modificado, potencialmente atualizado com os dados da imagem inicial codificada. |
| `latent` | LATENT | Um tensor latente de vídeo vazio com zeros, formatado para as dimensões especificadas. |
| `cond_latent` | LATENT | A representação latente limpa e codificada das imagens iniciais fornecidas. Isso é usado internamente para substituir o início ruidoso dos latentes de vídeo gerados. |
