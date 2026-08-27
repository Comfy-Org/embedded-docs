# Kandinsky5ImageToVideo

O nó Kandinsky5ImageToVideo prepara os dados de condicionamento e do espaço latente para a geração de vídeo usando o modelo Kandinsky. Ele cria um tensor latente de vídeo vazio e pode, opcionalmente, codificar uma imagem inicial para orientar os quadros iniciais do vídeo gerado, modificando os condicionamentos positivo e negativo de acordo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | Os prompts de condicionamento positivo para orientar a geração de vídeo. | CONDITIONING | Sim | N/A |
| `negativo` | Os prompts de condicionamento negativo para afastar a geração de vídeo de determinados conceitos. | CONDITIONING | Sim | N/A |
| `vae` | O modelo VAE usado para codificar a imagem inicial opcional no espaço latente. | VAE | Sim | N/A |
| `largura` | A largura do vídeo de saída em pixels (padrão: 768). | INT | Sim | 16 a 16384 (step 16) |
| `altura` | A altura do vídeo de saída em pixels (padrão: 512). | INT | Sim | 16 a 16384 (step 16) |
| `duração` | O número de quadros no vídeo (padrão: 121). | INT | Sim | 1 a 16384 (step 4) |
| `tamanho_do_lote` | O número de sequências de vídeo a serem geradas simultaneamente (padrão: 1). | INT | Sim | 1 a 4096 |
| `imagem_inicial` | Uma imagem inicial opcional ou lote de quadros. Se fornecido, ele é codificado e usado para substituir o início ruidoso dos latentes de saída do modelo. | IMAGE | Não | N/A |

**Nota:** Quando um `start_image` é fornecido, ele é redimensionado automaticamente para corresponder aos valores de `width` e `height` especificados, usando interpolação bilinear. Apenas os primeiros `length` quadros do lote de imagens são usados para codificação; quaisquer quadros adicionais são ignorados. Se o lote de imagens tiver menos quadros que `length`, somente esses quadros serão usados. Somente os canais RGB da imagem são codificados. O latente codificado é então injetado tanto no condicionamento `positive` quanto no `negative` para orientar a aparência inicial do vídeo, e os quadros codificados limpos substituem o início ruidoso dos latentes de saída do modelo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | O condicionamento positivo modificado, potencialmente atualizado com os dados da imagem inicial codificada. | CONDITIONING |
| `negativo` | O condicionamento negativo modificado, potencialmente atualizado com os dados da imagem inicial codificada. | CONDITIONING |
| `latente` | Latente de vídeo vazio. Um tensor latente preenchido com zeros, com o formato das dimensões especificadas. | LATENT |
| `latente_cond` | Latente contendo as imagens iniciais codificadas limpas, usado para substituir o início ruidoso dos latentes de saída do modelo. Vazio quando nenhum `start_image` é fornecido. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7212f0ea912578d3b72dddf1333a20054a881e3f22c2b8abd9645fc21e75a08b`
