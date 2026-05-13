> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/pt-BR.md)

O nó TextEncodeHunyuanVideo_ImageToVideo cria dados de condicionamento para geração de vídeo combinando prompts de texto com embeddings de imagem. Ele utiliza um modelo CLIP para processar tanto a entrada de texto quanto as informações visuais de uma saída de visão CLIP, gerando então tokens que mesclam essas duas fontes de acordo com a configuração especificada de intercalação de imagem.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `clip` | CLIP | Sim | - | O modelo CLIP usado para tokenização e codificação |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Sim | - | Os embeddings visuais de um modelo de visão CLIP que fornecem contexto de imagem |
| `prompt` | STRING | Sim | - | A descrição textual para guiar a geração de vídeo, suporta entrada multilinha e prompts dinâmicos |
| `image_interleave` | INT | Sim | 1-512 | O quanto a imagem influencia em relação ao prompt de texto. Um número maior significa mais influência do prompt de texto. (padrão: 2) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `CONDITIONING` | CONDITIONING | Os dados de condicionamento que combinam informações de texto e imagem para geração de vídeo |

---
**Source fingerprint (SHA-256):** `ee748bd1fb1733593eb4cb1187c5cc279171163cfbc389f039378d0e366fc231`
