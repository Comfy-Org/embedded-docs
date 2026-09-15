# MiniMax H3 Referência para Vídeo

O MiniMax H3 Reference to Video cria o condicionamento de texto e o latente vazio de áudio-vídeo necessários para a geração de referência para vídeo do MiniMax H3. Você fornece um prompt e, opcionalmente, imagens, vídeos e clipes de áudio de referência, e o nó codifica essas referências em condicionamento que o modelo pode usar durante a geração. O prompt se refere às referências com as tags `<Picture i>`, `<Video k>` e `<Audio j>`.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `clip` | Modelo CLIP usado para tokenizar o prompt e codificar a mídia de referência em tokens de condicionamento. | CLIP | Sim | |
| `vae` | VAE de vídeo. Sem ele, imagens/vídeos de referência apenas condicionam o codificador de texto. | VAE | Não | |
| `audio_vae` | VAE de áudio. Sem ele, o áudio de referência apenas condiciona o codificador de texto. | VAE | Não | |
| `prompt` | Prompt de texto para o vídeo. A mídia de referência pode ser referenciada com as tags `<Picture i>`, `<Video k>` e `<Audio j>` (indexadas a partir de 1 por tipo). Suporta prompts multilinha e dinâmicos. | STRING | Sim | |
| `largura` | Largura do vídeo gerado em pixels (padrão: 1344). | INT | Sim | 32 a 16384 (passo 32) |
| `altura` | Altura do vídeo gerado em pixels (padrão: 768). | INT | Sim | 32 a 16384 (passo 32) |
| `duração` | Número de quadros a 24 fps, (124 = ~5s, a faixa treinada é ~124-362) (padrão: 124). | INT | Sim | 5 a 3600 (passo 17) |
| `tamanho_imagem_ref` | Dimensionamento da imagem de referência. `match` redimensiona cada referência (somente para baixo, mantendo a proporção) para a área de pixels da geração; `max` usa a borda menor de 2048px do pipeline de referência para melhor fidelidade de identidade. Os tokens de referência são propagados por cada etapa de amostragem, então `max` pode ser várias vezes mais lento (padrão: `match`). | COMBO | Sim | `"match"`<br>`"max"` |
| `imagens_ref` | Slot expansível: conecte até 9 imagens de referência (`ref_image_1` ... `ref_image_9`). Imagem de referência (reduzida para a borda menor de 2048 se for maior, nunca ampliada). | IMAGE | Não | 0 a 9 |
| `vídeos_ref` | Slot expansível: conecte até 3 vídeos de referência (`ref_video_1` ... `ref_video_3`). Quadros de vídeo de referência a 24 fps (2-15s). | IMAGE | Não | 0 a 3 |
| `áudios_vídeo_ref` | Slot expansível: conecte até 3 trilhas sonoras (`ref_video_audio_1` ... `ref_video_audio_3`). Trilha sonora do vídeo de referência de mesmo número. | AUDIO | Não | 0 a 3 |
| `áudios_ref` | Slot expansível: conecte até 3 clipes de áudio de referência independentes (`ref_audio_1` ... `ref_audio_3`). Áudio de referência independente. | AUDIO | Não | 0 a 3 |

Observações:

- O prompt se refere à mídia de referência com tags indexadas a partir de 1 por tipo: `<Picture i>` para imagens, `<Video k>` para vídeos e `<Audio j>` para áudio. As referências são apresentadas ao modelo em uma ordem fixa: imagens, depois vídeos (com o rótulo `<Audio j>` de cada trilha sonora imediatamente antes de seu `<Video k>`), depois áudio independente.
- Uma trilha sonora conectada a `ref_video_audio_N` é usada com o vídeo de referência conectado a `ref_video_N`.
- Os vídeos de referência devem conter pelo menos 5 quadros (~0,2 segundos a 24 fps), caso contrário o nó gera um erro. Quadros além do `length` solicitado são cortados, e o número de quadros restante é ajustado para um valor suportado pelo modelo.
- O `length` solicitado é alinhado a um número de quadros suportado antes que o latente seja criado.
- Sem `vae`, imagens e vídeos de referência apenas condicionam o codificador de texto (nenhum latente de referência é produzido). Sem `audio_vae`, o áudio de referência apenas condiciona o codificador de texto.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | Condicionamento contendo o prompt codificado. Quando a mídia de referência e os VAEs relevantes são fornecidos, ele também contém o conteúdo codificado de imagem, vídeo e áudio de referência usado pelo modelo MiniMax H3. | CONDITIONING |
| `latent` | Latente vazio de áudio-vídeo com os valores solicitados de `width`, `height` e `length` (número de quadros), incluindo o latente de vídeo alinhado e o latente de áudio. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `47df0d6d13cb02aa4f69b50a7f8d0f6c1639c1fb5e0f69bf8fc57dd4cb752db8`
