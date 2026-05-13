> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ReferenceVideoApi/pt-BR.md)

Este nó gera um vídeo apresentando uma pessoa ou objeto com base em materiais de referência fornecidos. Ele utiliza o modelo Wan 2.7 para criar vídeos a partir de um prompt de texto, suportando performances de um único personagem e interações de múltiplos personagens. Você deve fornecer pelo menos um vídeo ou imagem de referência para que a geração funcione.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | COMBO | Sim | `"wan2.7-r2v"` | O modelo específico a ser usado para geração de vídeo. |
| `model.prompt` | STRING | Sim | - | Prompt descrevendo o vídeo. Use identificadores como 'character1' e 'character2' para se referir aos personagens de referência. |
| `model.negative_prompt` | STRING | Não | - | Prompt negativo descrevendo o que evitar no vídeo gerado (padrão: vazio). |
| `model.resolution` | COMBO | Sim | `"720P"`<br>`"1080P"` | A resolução do vídeo de saída. |
| `model.ratio` | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | A proporção de aspecto do vídeo de saída. |
| `model.duration` | INT | Sim | 2 a 10 | A duração do vídeo gerado em segundos (padrão: 5). |
| `model.reference_videos` | VIDEO | Não | - | Uma lista de vídeos de referência. Você pode adicionar até 3 vídeos. |
| `model.reference_images` | IMAGE | Não | - | Uma lista de imagens de referência. Você pode adicionar até 5 imagens. |
| `seed` | INT | Não | 0 a 2147483647 | Semente a ser usada para geração, que ajuda a controlar a aleatoriedade da saída (padrão: 0). |
| `watermark` | BOOLEAN | Não | - | Se deve adicionar uma marca d'água gerada por IA ao resultado (padrão: False). Esta é uma configuração avançada. |

**Restrições Importantes:**
*   Você deve fornecer pelo menos um vídeo de referência ou imagem de referência nas entradas `model.reference_videos` ou `model.reference_images`.
*   O número total combinado de vídeos e imagens de referência não pode exceder 5.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O arquivo de vídeo gerado. |

---
**Source fingerprint (SHA-256):** `f28a765e310410fc62241e11dbfe25562c7ae16e8e6ffbfb004face7a7e2b727`
