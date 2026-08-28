# ModelMergeQwenImage

O ModelMergeQwenImage mescla dois modelos de IA combinando seus componentes com pesos ajustáveis. Ele permite que você misture partes específicas dos modelos de imagem Qwen, incluindo blocos transformer, embeddings posicionais e componentes de processamento de texto. Você pode controlar o quanto de influência cada modelo exerce em diferentes seções do resultado mesclado.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model1` | O primeiro modelo a ser mesclado | MODEL | Sim | - |
| `model2` | O segundo modelo a ser mesclado | MODEL | Sim | - |
| `pos_embeds.` | Peso para a mesclagem de embeddings posicionais (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (step: 0.01) |
| `img_in.` | Peso para a mesclagem do processamento de entrada de imagem (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (step: 0.01) |
| `txt_norm.` | Peso para a mesclagem da normalização de texto (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (step: 0.01) |
| `txt_in.` | Peso para a mesclagem do processamento de entrada de texto (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (step: 0.01) |
| `time_text_embed.` | Peso para a mesclagem de embeddings de tempo e texto (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (step: 0.01) |
| `transformer_blocks.0.` a `transformer_blocks.59.` | Peso para a mesclagem de cada bloco transformer (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (step: 0.01) |
| `proj_out.` | Peso para a mesclagem da projeção de saída (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (step: 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo mesclado que combina componentes dos dois modelos de entrada com os pesos especificados | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5f31f91f3d54d4c5085c684a98f64afd0a0f704693b6dd4f19bc35d3c5f74529`
