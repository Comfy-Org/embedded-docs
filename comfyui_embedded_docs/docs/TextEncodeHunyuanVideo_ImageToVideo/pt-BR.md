# TextEncodeHunyuanVideo_ImageToVideo

O nó TextEncodeHunyuanVideo_ImageToVideo cria dados de condicionamento para a geração de vídeo combinando prompts de texto com embeddings de imagem. Ele usa um modelo CLIP para processar tanto a entrada de texto quanto as informações visuais de uma saída de visão CLIP e, em seguida, gera tokens que mesclam essas duas fontes de acordo com a configuração especificada de interpolação de imagem (image interleave).

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para tokenização e codificação | CLIP | Sim | - |
| `clip_vision_output` | Os embeddings visuais de um modelo de visão CLIP que fornecem contexto de imagem | CLIP_VISION_OUTPUT | Sim | - |
| `prompt` | A descrição de texto para orientar a geração de vídeo. Suporta entrada multilinha e prompts dinâmicos. O prompt é formatado usando um modelo que pede ao modelo para descrever o vídeo com base na imagem de referência, cobrindo aspectos como conteúdo principal, detalhes dos objetos, ações, fundo e ângulos de câmera. | STRING | Sim | - |
| `image_interleave` | O quanto a imagem influencia em relação ao prompt de texto. Um número maior significa mais influência do prompt de texto. (padrão: 2, parâmetro avançado) | INT | Sim | 1-512 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CONDITIONING` | Os dados de condicionamento que combinam informações de texto e imagem para a geração de vídeo | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `016b87ead6f7a6ca61eff220e57f59252018cc78e80ec8cff5b83223b8f90f73`
