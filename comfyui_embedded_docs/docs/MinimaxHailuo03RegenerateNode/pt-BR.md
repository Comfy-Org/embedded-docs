# MiniMax H3 Regenerar para 2K

Este nó renderiza novamente uma saída de vídeo MiniMax H3 768P em resolução 2K. Ele faz upload do vídeo 768P não modificado e do prompt exato usado para gerá-lo, inicia uma tarefa de regeneração do MiniMax H3 e retorna o vídeo 2K renderizado novamente. Se a geração original usou primeiro ou último quadro ou mídia de referência, anexe as mesmas entradas.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo a ser usado para regeneração de vídeo. Selecionar "MiniMax H3" revela as configurações de prompt, resolução e mídia de referência. | DYNAMIC_COMBO | Sim | "MiniMax H3" |
| `video` | O vídeo de saída MiniMax H3 768P a ser renderizado novamente. Conecte a saída não modificada de um nó de vídeo MiniMax H3 (24 FPS, 4-15 segundos). Saídas 2K não podem ser usadas. | VIDEO | Sim | 24 FPS, 4-15 segundos |
| `first_frame` | Imagem do primeiro quadro da geração original, se uma foi usada. | IMAGE | Não | Imagem |
| `last_frame` | Imagem do último quadro da geração original, se uma foi usada. | IMAGE | Não | Imagem |
| `watermark` | Se deve adicionar uma marca d'água AIGC ao vídeo. O padrão é false. | BOOLEAN | Sim | false / true |

### Entradas do MiniMax H3

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | O prompt exato usado para gerar o vídeo de origem. Não deve estar vazio. | STRING | Sim | Texto (multilinha) |
| `resolution` | Resolução na qual renderizar novamente o vídeo de origem. | COMBO | Sim | "2K" |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Slot expansível: conecte `image_1` até `image_9` (até 9 imagens). Imagens de referência da geração original, na mesma ordem. | IMAGE | Não | 0-9 imagens |
| `reference_videos` | Slot expansível: conecte `video_1` até `video_3` (até 3 vídeos). Vídeos de referência da geração original, na mesma ordem. | VIDEO | Não | 0-3 vídeos |
| `reference_audios` | Slot expansível: conecte `audio_1` até `audio_3` (até 3 clipes). Referências de áudio da geração original, na mesma ordem. Não pode ser usado sem uma imagem ou vídeo de referência. | AUDIO | Não | 0-3 clipes |

### Restrições

- O `prompt` não deve estar vazio.
- O `video` de origem deve ser uma saída MiniMax H3 768P não modificada: 24 FPS, largura e altura divisíveis por 32, no máximo 1,032,192 pixels totais, e 107 a 362 quadros em incrementos de 17 (4 a 15 segundos a 24 FPS). Saídas 2K não podem ser usadas como origem.
- `first_frame` e `last_frame` são mutuamente exclusivos com mídia de referência (`reference_images`, `reference_videos`, `reference_audios`). Use quadros para um prompt de imagem para vídeo, ou mídia de referência para um prompt de referência para vídeo.
- `reference_audios` requer pelo menos uma entrada `reference_images` ou `reference_videos`.
- `first_frame`, `last_frame` e cada `reference_image` devem ter uma proporção de aspecto entre 0.4 e 2.5 e pelo menos 256x256 pixels.
- `reference_videos`: cada vídeo deve ter de 23.976 a 60 FPS e de 2 a 15 segundos de duração; a duração total não pode exceder 15 segundos.
- `reference_audios`: cada clipe deve ter de 2 a 15 segundos de duração; a duração total não pode exceder 15 segundos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O vídeo MiniMax H3 renderizado novamente em resolução 2K. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03RegenerateNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4b5aa6dee12364cf6f44e7ee78b984c3568529b97051637a6ac62db9761d3a77`
