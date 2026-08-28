# MiniMax H3 Referência para Vídeo

MiniMax H3 Reference to Video cria o condicionamento de texto e o latent de áudio-vídeo vazio necessários para a geração de referência para vídeo do MiniMax H3. Você fornece um prompt além de imagens, vídeos e clipes de áudio de referência opcionais, e o nó codifica essas referências em tokens que o modelo pode usar durante a geração. O prompt se refere às referências com as tags `<Picture i>`, `<Video k>` e `<Audio j>`.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `clip` | Modelo CLIP usado para tokenizar o prompt e codificar a mídia de referência em tokens de condicionamento. | CLIP | Sim | |
| `vae` | VAE usado para codificar imagens de referência e quadros de vídeo de referência no espaço latente. | VAE | Sim | |
| `audio_vae` | VAE usado para codificar o áudio de referência no espaço latente. O áudio é reamostrado para a taxa de amostragem do VAE de áudio (32 kHz por padrão). | VAE | Sim | |
| `prompt` | Prompt de texto para o vídeo. A mídia de referência pode ser endereçada com as tags `<Picture i>`, `<Video k>` e `<Audio j>` (com numeração a partir de 1 por tipo). Suporta prompts multilinha e dinâmicos. | STRING | Sim | |
| `largura` | Largura do vídeo gerado em pixels (padrão: 1344). | INT | Sim | 32 a 16384 (passo 32) |
| `altura` | Altura do vídeo gerado em pixels (padrão: 768). | INT | Sim | 32 a 16384 (passo 32) |
| `duração` | Contagem de quadros a 24 fps; 124 = ~5s, a faixa treinada é ~124-362 (padrão: 124). | INT | Sim | 5 a 3600 (passo 17) |
| `tamanho_imagem_ref` | Dimensionamento da imagem de referência. `match` reduz cada imagem de referência somente, mantendo a proporção, para a área de pixels da geração; `max` usa a borda curta de 2048px do pipeline de referência para a melhor fidelidade de identidade. Os tokens de referência percorrem cada etapa de amostragem, então `max` pode ser várias vezes mais lento (padrão: `match`). | COMBO | Sim | `"match"`<br>`"max"` |
| `imagens_ref` | Slot expansível: conecte de 1 a 9 imagens de referência (`ref_image_1` ... `ref_image_9`). Cada imagem é reduzida para uma borda curta de 2048px se for maior, e nunca é ampliada. | IMAGE | Não | 0 a 9 |
| `vídeos_ref` | Slot expansível: conecte de 1 a 3 vídeos de referência (`ref_video_1` ... `ref_video_3`). Quadros de vídeo de referência a 24 fps (2-15s). | IMAGE | Não | 0 a 3 |
| `áudios_vídeo_ref` | Slot expansível: conecte de 1 a 3 trilhas sonoras (`ref_video_audio_1` ... `ref_video_audio_3`). Trilha sonora do vídeo de referência de mesmo número. | AUDIO | Não | 0 a 3 |
| `áudios_ref` | Slot expansível: conecte de 1 a 3 clipes de áudio de referência independentes (`ref_audio_1` ... `ref_audio_3`). | AUDIO | Não | 0 a 3 |

Notas:

- O prompt se refere à mídia de referência com tags com numeração a partir de 1 por tipo: `<Picture i>` para imagens, `<Video k>` para vídeos e `<Audio j>` para áudio. As referências são apresentadas ao modelo em uma ordem fixa: imagens, depois vídeos (com o rótulo `<Audio j>` de cada trilha sonora imediatamente antes do seu `<Video k>`), e então o áudio independente.
- Os vídeos de referência devem conter pelo menos 5 quadros (~0,2 segundos a 24 fps), caso contrário o nó gera um erro. Os quadros de vídeo também são limitados ao `length` selecionado e ajustados para uma contagem de quadros suportada.
- O `length` solicitado é alinhado a uma contagem de quadros suportada antes da criação do latent.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positivo` | Condicionamento contendo o prompt codificado em conjunto com os tokens codificados de imagem, vídeo e áudio de referência usados pelo modelo MiniMax H3. | CONDITIONING |
| `latent` | Latent de áudio-vídeo vazio com o `width`, `height` e `length` solicitados (contagem de quadros). | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d9a444e712cdc255d7c56a3ab38d0523659f198b3228b9283a7028cfd0e4f3f9`
