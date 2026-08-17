# ModelMergeQwenImage

O nó `ModelMergeQwenImage` mescla dois modelos de IA combinando seus componentes com pesos ajustáveis. Ele permite combinar partes específicas dos modelos de imagem Qwen, incluindo blocos do transformador, embeddings posicionais e componentes de processamento de texto. Você pode controlar o quanto de influência cada modelo exerce sobre diferentes seções do resultado mesclado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model1` | O primeiro modelo a mesclar (padrão: nenhum) | MODEL | Sim | - |
| `model2` | O segundo modelo a mesclar (padrão: nenhum) | MODEL | Sim | - |
| `pos_embeds.` | Peso para mesclagem de embeddings posicionais (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `img_in.` | Peso para mesclagem do processamento de entrada de imagem (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `txt_norm.` | Peso para mesclagem da normalização de texto (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `txt_in.` | Peso para mesclagem do processamento de entrada de texto (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `time_text_embed.` | Peso para mesclagem do embedding de tempo e texto (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `transformer_blocks.0.` a `transformer_blocks.59.` | Peso para mesclagem de cada bloco do transformador (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `proj_out.` | Peso para mesclagem da projeção de saída (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |

Observação: há 60 entradas de peso individuais para blocos do transformador (`transformer_blocks.0.` até `transformer_blocks.59.`), uma para cada bloco do transformador no modelo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo mesclado que combina componentes de ambos os modelos de entrada com os pesos especificados | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5f31f91f3d54d4c5085c684a98f64afd0a0f704693b6dd4f19bc35d3c5f74529`
