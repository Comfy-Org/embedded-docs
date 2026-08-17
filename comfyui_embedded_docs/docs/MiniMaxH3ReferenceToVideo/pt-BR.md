# MiniMax H3 Referência para Vídeo

### Visão Geral

O MiniMax H3 Reference to Video cria o condicionamento de texto e o latente de áudio-vídeo vazio necessários para a geração de vídeo por referência do MiniMax H3. Você fornece um prompt mais imagens, vídeos e clipes de áudio de referência opcionais, e o nó codifica essas referências em tokens que o modelo pode usar durante a geração. O prompt se refere às referências com as tags `<Picture i>`, `<Video k>` e `<Audio j>`.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Range |
|-----------|-------------|-----------|----------|-------|
| `clip` | Modelo CLIP usado para tokenizar o prompt e codificar a mídia de referência em tokens de condicionamento. | CLIP | Sim | |
| `vae` | VAE usado para codificar imagens de referência e quadros de vídeo de referência no espaço latente. | VAE | Sim | |
| `audio_vae` | VAE usado para codificar o áudio de referência no espaço latente (taxa de amostragem de áudio de 32 kHz). | VAE | Sim | |
| `prompt` | Prompt de texto para o vídeo. A mídia de referência pode ser endereçada com as tags `<Picture i>`, `<Video k>` e `<Audio j>` (baseadas em 1, por tipo). Suporta prompts multilinha e dinâmicos. | STRING | Sim | |
| `width` | Largura do vídeo gerado em pixels (padrão: 1344). | INT | Sim | 32 to 16384 (step 32) |
| `height` | Altura do vídeo gerado em pixels (padrão: 768). | INT | Sim | 32 to 16384 (step 32) |
| `length` | Contagem de quadros a 24 fps; 124 = ~5s, a faixa de treinamento é ~124-362 (padrão: 124). | INT | Sim | 5 to 3600 (step 17) |
| `ref_image_size` | Modo de dimensionamento da imagem de referência. `match` reduz cada imagem de referência, mantendo a proporção, para a área de pixels da geração; `max` usa a borda curta de 2048px do pipeline de referência para melhor fidelidade de identidade. Os tokens de referência percorrem cada etapa de amostragem, então `max` pode ser várias vezes mais lento (padrão: `match`). | COMBO | Sim | `"match"`<br>`"max"` |
| `ref_images` | Imagens de referência opcionais. Cada imagem é reduzida para uma borda curta de 2048px se for maior e nunca é ampliada. Várias imagens podem ser fornecidas. | IMAGE | Não | 0 to 9 |
| `ref_videos` | Quadros de vídeo de referência opcionais a 24 fps (2-15s). Vários vídeos podem ser fornecidos. | IMAGE | Não | 0 to 3 |
| `ref_video_audios` | Trilhas sonoras opcionais pareadas com os vídeos de referência por índice; `ref_video_audio_N` é a trilha sonora do `ref_video_N` de mesmo número. | AUDIO | Não | 0 to 3 |
| `ref_audios` | Clipes de áudio de referência independentes opcionais. | AUDIO | Não | 0 to 3 |

Notas:
- O prompt se refere à mídia de referência com tags baseadas em 1, por tipo: `<Picture i>` para imagens, `<Video k>` para vídeos e `<Audio j>` para áudio. As referências são apresentadas ao modelo em uma ordem fixa: imagens, depois vídeos (com o rótulo `<Audio j>` de cada trilha sonora imediatamente antes do seu `<Video k>`), e então áudio independente.
- Os vídeos de referência devem conter pelo menos 5 quadros (~0,2 segundos a 24 fps), caso contrário o nó gera um erro. Os quadros de vídeo são limitados ao `length` selecionado e ajustados para uma contagem de quadros suportada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | Condicionamento contendo o prompt codificado juntamente com os tokens de imagem, vídeo e áudio de referência codificados, usados pelo modelo MiniMax H3. | CONDITIONING |
| `latent` | Latente de áudio-vídeo vazio com os valores de `width`, `height` e `length` (contagem de quadros) solicitados. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d9a444e712cdc255d7c56a3ab38d0523659f198b3228b9283a7028cfd0e4f3f9`
