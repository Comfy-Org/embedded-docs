> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/pt-BR.md)

O nó ModelMergeQwenImage mescla dois modelos de IA combinando seus componentes com pesos ajustáveis. Ele permite que você misture partes específicas dos modelos de imagem Qwen, incluindo blocos transformadores, embeddings posicionais e componentes de processamento de texto. Você pode controlar quanto influência cada modelo tem em diferentes seções do resultado mesclado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sim | - | O primeiro modelo a ser mesclado (padrão: nenhum) |
| `model2` | MODEL | Sim | - | O segundo modelo a ser mesclado (padrão: nenhum) |
| `pos_embeds.` | FLOAT | Sim | 0.0 a 1.0 | Peso para a mesclagem de embeddings posicionais (padrão: 1.0) |
| `img_in.` | FLOAT | Sim | 0.0 a 1.0 | Peso para a mesclagem do processamento de entrada de imagem (padrão: 1.0) |
| `txt_norm.` | FLOAT | Sim | 0.0 a 1.0 | Peso para a mesclagem da normalização de texto (padrão: 1.0) |
| `txt_in.` | FLOAT | Sim | 0.0 a 1.0 | Peso para a mesclagem do processamento de entrada de texto (padrão: 1.0) |
| `time_text_embed.` | FLOAT | Sim | 0.0 a 1.0 | Peso para a mesclagem de embeddings de tempo e texto (padrão: 1.0) |
| `transformer_blocks.0.` a `transformer_blocks.59.` | FLOAT | Sim | 0.0 a 1.0 | Peso para a mesclagem de cada bloco transformador (padrão: 1.0) |
| `proj_out.` | FLOAT | Sim | 0.0 a 1.0 | Peso para a mesclagem da projeção de saída (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo mesclado que combina componentes de ambos os modelos de entrada com os pesos especificados |
