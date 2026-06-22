# ModelMergeBlocks

ModelMergeBlocks foi projetado para operações avançadas de mesclagem de modelos, permitindo a integração de dois modelos com proporções de mesclagem personalizáveis para diferentes partes dos modelos. Este nó facilita a criação de modelos híbridos ao mesclar seletivamente componentes de dois modelos de origem com base em parâmetros especificados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model1` | O primeiro modelo a ser mesclado. Serve como modelo base sobre o qual patches do segundo modelo são aplicados. | `MODEL` |
| `model2` | O segundo modelo do qual patches são extraídos e aplicados ao primeiro modelo, com base nas proporções de mesclagem especificadas. | `MODEL` |
| `entrada` | Especifica a proporção de mesclagem para a camada de entrada dos modelos. Determina quanto da camada de entrada do segundo modelo é mesclada ao primeiro modelo. | `FLOAT` |
| `meio` | Define a proporção de mesclagem para as camadas intermediárias dos modelos. Este parâmetro controla o nível de integração das camadas intermediárias dos modelos. | `FLOAT` |
| `saída` | Determina a proporção de mesclagem para a camada de saída dos modelos. Afeta a saída final ao ajustar a contribuição da camada de saída do segundo modelo. | `FLOAT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo mesclado resultante, que é um híbrido dos dois modelos de entrada com patches aplicados de acordo com as proporções de mesclagem especificadas. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeBlocks/pt-BR.md)
