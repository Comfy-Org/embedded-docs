# USOStyleReference

O nó USOStyleReference aplica uma referência de estilo a um modelo combinando características de visão do CLIP com um patch de modelo, e retorna uma cópia corrigida do modelo de entrada. Ele é destinado a modelos Flux e está marcado como experimental. As informações de estilo visual são combinadas com o condicionamento de texto do modelo para que possam influenciar a geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo base ao qual o patch de referência de estilo é aplicado. | MODEL | Sim | - |
| `model_patch` | O patch de modelo que contém o modelo de projeção usado para codificar as características da imagem de referência. | MODEL_PATCH | Sim | - |
| `clip_vision_output` | As características visuais codificadas extraídas do processamento de visão CLIP da imagem de referência. | CLIP_VISION_OUTPUT | Sim | - |

Nota: O `clip_vision_output` deve vir de um modelo de visão CLIP que forneça os estados ocultos completos e o penúltimo estado oculto. O nó combina o 20º a partir do final, o 11º a partir do final e o penúltimo estado oculto no embedding de estilo. O `model_patch` deve expor um modelo de projeção por meio de seu atributo `model` que converte essas características de imagem no embedding de estilo. Durante a amostragem, o embedding de estilo é adicionado ao início do condicionamento de texto para que possa influenciar a geração.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com o patch de referência de estilo aplicado. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9033dddb76fafb388c67dcd09d96102a7ab3e5bc416cec61bf18d088da37a0f0`
