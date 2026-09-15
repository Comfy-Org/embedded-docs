# ModelMergeQwenImage

Este nó mescla dois modelos de imagem Qwen combinando seus componentes individuais com pesos ajustáveis. Cada peso controla o quanto a parte correspondente do segundo modelo contribui para o resultado mesclado, permitindo misturar embeddings posicionais, camadas de processamento de texto, camadas de entrada de imagem, todos os 60 blocos transformer e a projeção de saída separadamente. O resultado final é um único MODEL que você pode usar onde um modelo normal é esperado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model1` | O primeiro modelo a mesclar | MODEL | Sim | - |
| `model2` | O segundo modelo a mesclar | MODEL | Sim | - |
| `pos_embeds.` | Peso para mesclagem de embeddings posicionais (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `img_in.` | Peso para mesclagem do processamento de entrada de imagem (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `txt_norm.` | Peso para mesclagem da normalização de texto (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `txt_in.` | Peso para mesclagem do processamento de entrada de texto (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `time_text_embed.` | Peso para mesclagem de embedding de tempo e texto (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `transformer_blocks.0.` a `transformer_blocks.59.` | Peso para mesclagem de cada bloco transformer (padrão: 1.0). O nó expõe um peso para cada um dos 60 blocos transformer. | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `proj_out.` | Peso para mesclagem da projeção de saída (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |

Observação: Todas as entradas de peso são obrigatórias e compartilham os mesmos limites — um padrão de 1.0 com um intervalo válido de 0.0 a 1.0, ajustável em passos de 0.01.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo mesclado, combinando componentes de ambos os modelos de entrada com os pesos especificados | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5f31f91f3d54d4c5085c684a98f64afd0a0f704693b6dd4f19bc35d3c5f74529`
