# Kandinsky5ImageToVideo

O nó Kandinsky5ImageToVideo prepara condicionamento e dados latentes para geração de vídeo usando o modelo Kandinsky. Ele cria um latente de vídeo vazio dimensionado para a largura, altura, comprimento e tamanho do lote solicitados, e pode opcionalmente codificar uma imagem inicial para orientar os quadros iniciais do vídeo gerado, atualizando os condicionamentos positivo e negativo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | Os prompts de condicionamento positivo para orientar a geração do vídeo. | CONDITIONING | Sim | N/A |
| `negative` | Os prompts de condicionamento negativo para afastar a geração do vídeo de certos conceitos. | CONDITIONING | Sim | N/A |
| `vae` | O modelo VAE usado para codificar a imagem inicial opcional no espaço latente. | VAE | Sim | N/A |
| `width` | A largura do vídeo de saída em pixels (padrão: 768). | INT | Sim | 16 a 16384 (passo: 16) |
| `height` | A altura do vídeo de saída em pixels (padrão: 512). | INT | Sim | 16 a 16384 (passo: 16) |
| `length` | O número de quadros no vídeo (padrão: 121). | INT | Sim | 1 a 16384 (passo: 4) |
| `batch_size` | O número de sequências de vídeo a serem geradas simultaneamente (padrão: 1). | INT | Sim | 1 a 4096 |
| `start_image` | Uma imagem inicial opcional ou lote de quadros. Se fornecida, ela é codificada e usada para substituir o início ruidoso dos latentes de saída do modelo. | IMAGE | Não | N/A |

**Nota:** Quando uma `start_image` é fornecida, ela é redimensionada automaticamente para corresponder à `width` e `height` especificadas usando interpolação bilinear. Apenas os primeiros `length` quadros do lote de imagens são usados para codificação; quaisquer quadros adicionais são ignorados. Se o lote de imagens tiver menos de `length` quadros, apenas esses quadros serão usados. Apenas os canais RGB da imagem são codificados. O latente codificado é então injetado tanto no condicionamento `positive` quanto no `negative` para orientar a aparência inicial do vídeo, e os quadros codificados limpos substituem o início ruidoso dos latentes de saída do modelo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | O condicionamento positivo modificado, atualizado com dados codificados da imagem inicial quando uma `start_image` é fornecida. | CONDITIONING |
| `negative` | O condicionamento negativo modificado, atualizado com dados codificados da imagem inicial quando uma `start_image` é fornecida. | CONDITIONING |
| `latent` | Latente de vídeo vazio. Um tensor latente preenchido com zeros, moldado para as dimensões especificadas. | LATENT |
| `cond_latent` | Latente limpo de imagens iniciais codificadas, usado para substituir o início ruidoso dos latentes de saída do modelo. Vazio quando nenhuma `start_image` é fornecida. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7212f0ea912578d3b72dddf1333a20054a881e3f22c2b8abd9645fc21e75a08b`
