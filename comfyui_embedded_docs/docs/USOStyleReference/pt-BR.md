# USOStyleReference

O nó USOStyleReference aplica informações de estilo de uma imagem de referência a um modelo Flux. Ele constrói um embedding de estilo a partir da saída do CLIP vision e, em seguida, aplica um patch em um clone do modelo para que, durante a geração, o embedding de estilo seja inserido antes do condicionamento do prompt de texto.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo base para aplicar o patch de referência de estilo | MODEL | Sim | - |
| `model_patch` | O patch do modelo contendo as informações de referência de estilo | MODEL_PATCH | Sim | - |
| `clip_vision_output` | As características visuais codificadas extraídas do processamento do CLIP vision. O nó combina os estados ocultos das camadas -20 e -11 juntamente com os penúltimos estados ocultos para construir o embedding de estilo | CLIP_VISION_OUTPUT | Sim | - |

Nota: Todas as três entradas são obrigatórias. Este nó está marcado como experimental.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com o patch de referência de estilo aplicado | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9033dddb76fafb388c67dcd09d96102a7ab3e5bc416cec61bf18d088da37a0f0`
