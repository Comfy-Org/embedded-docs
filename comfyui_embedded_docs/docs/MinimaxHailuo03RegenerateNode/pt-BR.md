# MinimaxHailuo03RegenerateNode

Este nó re-renderiza uma saída de vídeo MiniMax H3 768P em resolução 2K. Ele envia o vídeo de origem e o prompt exato usado para criá-lo, inicia um trabalho de regeneração MiniMax H3 e retorna o vídeo 2K re-renderizado. Se a geração original usou primeiro ou último quadro ou mídia de referência, anexe as mesmas entradas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|-------------|-----------|
| `model` | O modelo a ser usado para regeneração de vídeo. Selecionar este modelo revela as configurações de prompt, resolução e mídia de referência documentadas abaixo. | COMBO | Sim | "MiniMax H3" |
| `prompt` | O prompt exato usado para gerar o vídeo de origem. Não deve estar vazio. | STRING | Sim | Text |
| `resolution` | Resolução para re-renderizar o vídeo de origem. | COMBO | Sim | "2K" |
| `reference_images` | Imagens de referência da geração original, na mesma ordem. Até 9 imagens. | IMAGE | Não | 0-9 imagens |
| `reference_videos` | Vídeos de referência da geração original, na mesma ordem. Até 3 vídeos, de 2 a 15 segundos cada, 15 segundos no total. | VIDEO | Não | 0-3 vídeos |
| `reference_audios` | Referências de áudio da geração original, na mesma ordem. Até 3 clipes, de 2 a 15 segundos cada, 15 segundos no total. Não podem ser usadas sem uma imagem ou vídeo de referência. | AUDIO | Não | 0-3 clipes |
| `video` | O vídeo de saída MiniMax H3 768P a ser re-renderizado. Conecte a saída não modificada de um nó de vídeo MiniMax H3 (24 FPS, 4 a 15 segundos). Saídas 2K não podem ser usadas. | VIDEO | Sim | 24 FPS, 4 a 15 segundos |
| `first_frame` | Imagem do primeiro quadro da geração original, se um foi usado. | IMAGE | Não | Imagem |
| `last_frame` | Imagem do último quadro da geração original, se um foi usado. | IMAGE | Não | Imagem |
| `watermark` | Se deve adicionar uma marca d'água AIGC ao vídeo. O padrão é false. | BOOLEAN | Sim | false / true |

### Restrições

- O `video` de origem deve ser uma saída MiniMax H3 768P não modificada: largura e altura divisíveis por 32, no máximo 1.032.192 pixels no total, 24 FPS e 107 a 362 quadros em passos de 17 (4 a 15 segundos a 24 FPS). Saídas 2K não podem ser usadas como fonte.
- `first_frame` / `last_frame` e mídia de referência (`reference_images`, `reference_videos`, `reference_audios`) são mutuamente exclusivos. Use quadros para um prompt de imagem para vídeo, ou mídia de referência para um prompt de referência para vídeo.
- `reference_audios` exige pelo menos uma entrada `reference_images` ou `reference_videos`.
- `reference_images`: cada imagem deve ter uma proporção de aspecto entre 0,4 e 2,5 e ter pelo menos 256x256 pixels.
- `reference_videos`: cada vídeo deve ter 23,976 a 60 FPS e duração de 2 a 15 segundos; a duração total não pode exceder 15 segundos.
- `reference_audios`: cada clipe deve ter duração de 2 a 15 segundos; a duração total não pode exceder 15 segundos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `video` | O vídeo MiniMax H3 re-renderizado em resolução 2K. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03RegenerateNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4b5aa6dee12364cf6f44e7ee78b984c3568529b97051637a6ac62db9761d3a77`
