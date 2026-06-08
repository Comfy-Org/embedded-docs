O nó TextEncodeHunyuanVideo_ImageToVideo cria dados de condicionamento para geração de vídeo combinando prompts de texto com embeddings de imagem. Ele utiliza um modelo CLIP para processar tanto a entrada de texto quanto as informações visuais de uma saída de visão CLIP, gerando então tokens que mesclam essas duas fontes de acordo com a configuração especificada de intercalação de imagem.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para tokenização e codificação | CLIP | Sim | - |
| `clip_vision_output` | Os embeddings visuais de um modelo de visão CLIP que fornecem contexto de imagem | CLIP_VISION_OUTPUT | Sim | - |
| `prompt` | A descrição textual para guiar a geração de vídeo, suporta entrada multilinha e prompts dinâmicos | STRING | Sim | - |
| `image_interleave` | O quanto a imagem influencia em relação ao prompt de texto. Um número maior significa mais influência do prompt de texto. (padrão: 2) | INT | Sim | 1-512 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | Os dados de condicionamento que combinam informações de texto e imagem para geração de vídeo | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ee748bd1fb1733593eb4cb1187c5cc279171163cfbc389f039378d0e366fc231`
