> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageToVideoWithAudio/pt-BR.md)

Este documento foi gerado por IA. Se encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageToVideoWithAudio/en.md)

O nó Kling Image(First Frame) to Video with Audio utiliza o modelo de IA Kling para gerar um vídeo curto a partir de uma única imagem inicial e um prompt de texto. Ele cria uma sequência de vídeo que começa com a imagem fornecida e pode opcionalmente incluir áudio gerado por IA para acompanhar os visuais.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model_name` | COMBO | Sim | `"kling-v2-6"` | A versão específica do modelo de IA Kling a ser usada para geração de vídeo. |
| `start_frame` | IMAGE | Sim | - | A imagem que servirá como primeiro quadro do vídeo gerado. A imagem deve ter pelo menos 300x300 pixels e uma proporção de aspecto entre 1:2,5 e 2,5:1. |
| `prompt` | STRING | Sim | - | Prompt de texto positivo. Descreve o conteúdo do vídeo que você deseja gerar. O prompt deve ter entre 1 e 2500 caracteres. |
| `mode` | COMBO | Sim | `"pro"` | O modo operacional para a geração do vídeo. |
| `duration` | COMBO | Sim | `5`<br>`10` | A duração do vídeo a ser gerado, em segundos. |
| `generate_audio` | BOOLEAN | Não | - | Quando ativado, o nó gerará áudio para acompanhar o vídeo. Quando desativado, o vídeo ficará sem som. (padrão: True) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `video` | VIDEO | O arquivo de vídeo gerado, que pode incluir áudio dependendo da entrada `generate_audio`. |

---
**Source fingerprint (SHA-256):** `f161eedbc5d780805e3d0ca32b6be94cc78afcd2749e065c032ea20991b782fc`
