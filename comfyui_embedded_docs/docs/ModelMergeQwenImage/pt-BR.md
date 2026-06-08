O nó ModelMergeQwenImage mescla dois modelos de IA combinando seus componentes com pesos ajustáveis. Ele permite que você misture partes específicas de modelos de imagem Qwen, incluindo blocos transformadores, embeddings posicionais e componentes de processamento de texto. Você pode controlar quanta influência cada modelo tem em diferentes seções do resultado mesclado.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model1` | O primeiro modelo a ser mesclado (padrão: nenhum) | MODEL | Sim | - |
| `model2` | O segundo modelo a ser mesclado (padrão: nenhum) | MODEL | Sim | - |
| `pos_embeds.` | Peso para mesclagem de embeddings posicionais (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `img_in.` | Peso para mesclagem do processamento de entrada de imagem (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `txt_norm.` | Peso para mesclagem da normalização de texto (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `txt_in.` | Peso para mesclagem do processamento de entrada de texto (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `time_text_embed.` | Peso para mesclagem de embeddings de tempo e texto (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `transformer_blocks.0.` a `transformer_blocks.59.` | Peso para mesclagem de cada bloco transformador (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `proj_out.` | Peso para mesclagem da projeção de saída (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo mesclado combinando componentes de ambos os modelos de entrada com os pesos especificados | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a0424a3f4d4ffe170471ba463350d741f67ff1b1f5a8a016ad844c111033f97c`
