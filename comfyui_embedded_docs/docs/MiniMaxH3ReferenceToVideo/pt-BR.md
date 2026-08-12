# MiniMax H3 Referência para Vídeo

### Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `clip` | Modelo CLIP usado para tokenizar o prompt e codificar a mídia de referência em tokens de condicionamento. | CLIP | Sim | |
| `vae` | VAE usado para codificar imagens de referência e quadros de vídeo de referência no espaço latente. | VAE | Sim | |
| `audio_vae` | VAE usado para codificar o áudio de referência no espaço latente (taxa de amostragem de áudio de 32 kHz). | VAE | Sim | |
| `prompt` | Prompt de texto para o vídeo. A mídia de referência pode ser endereçada com as tags `<Picture i>`, `<Video k>` e `<Audio j>` (numeração iniciando em 1 para cada tipo). Suporta prompts multilinha e dinâmicos. | STRING | Sim | |
| `largura` | Largura do vídeo gerado em pixels (padrão: 1344). | INT | Sim | 32 a 16384 (passo 32) |
| `altura` | Altura do vídeo gerado em pixels (padrão: 768). | INT | Sim | 32 a 16384 (passo 32) |
| `duração` | Contagem de quadros a 24 fps; 124 = ~5s; o intervalo treinado é de ~124 a 362 (padrão: 124). | INT | Sim | 5 a 3600 (passo 17) |
| `tamanho_imagem_ref` | Modo de dimensionamento da imagem de referência. `match` apenas reduz cada imagem de referência, mantendo a proporção, até a área de pixels da geração; `max` usa a borda curta de 2048px do pipeline de referência para obter a melhor fidelidade de identidade. Os tokens de referência são mantidos em todas as etapas de amostragem, portanto `max` pode ser várias vezes mais lento (padrão: `match`). | COMBO | Sim | `"match"`<br>`"max"` |
| `imagens_ref` | Imagens de referência opcionais. Cada imagem é reduzida para ter a borda curta de 2048px, se for maior, e nunca é ampliada. É possível fornecer várias imagens. | IMAGE | Não | 0 a 9 |
| `vídeos_ref` | Quadros de vídeo de referência opcionais a 24 fps (2 a 15 s). É possível fornecer vários vídeos. | IMAGE | Não | 0 a 3 |
| `áudios_vídeo_ref` | Trilhas sonoras opcionais associadas aos vídeos de referência por índice; `ref_video_audio_N` é a trilha sonora do `ref_video_N` de mesmo número. | AUDIO | Não | 0 a 3 |
| `áudios_ref` | Clipes de áudio de referência opcionais independentes. | AUDIO | Não | 0 a 3 |

### Notas

- O prompt se refere à mídia de referência com tags de numeração iniciando em 1 por tipo: `<Picture i>` para imagens, `<Video k>` para vídeos e `<Audio j>` para áudio. As referências são apresentadas ao modelo em uma ordem fixa: imagens, depois vídeos (com o rótulo `<Audio j>` de cada trilha sonora logo antes do seu `<Video k>`) e, por fim, áudios independentes.
- Os vídeos de referência devem conter pelo menos 5 quadros (~0,2 segundos a 24 fps); caso contrário, o nó gera um erro. Os quadros do vídeo também são limitados ao `length` selecionado e reduzidos para uma contagem de quadros compatível.

### Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | Condicionamento contendo o prompt codificado em conjunto com os tokens codificados de imagem, vídeo e áudio de referência usados pelo modelo MiniMax H3. | CONDITIONING |
| `latent` | Latente de áudio-vídeo vazio nas `largura`, `altura` e `duração` (contagem de quadros) solicitadas. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `529e51c5c9c63a94176a15851f40ac42f7bd93e7d7c6ad334ed22aa29d04dfde`
