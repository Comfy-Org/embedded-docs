# HeyGen Video 1.0 Referência para Vídeo

Gere um vídeo com diálogo e som sincronizados a partir de um prompt de texto usando o HeyGen Video 1.0, opcionalmente guiado por material de referência conectado. Imagens de pessoas, produtos ou lugares, vídeos para reutilização e clipes de áudio que fornecem uma voz podem todos ser usados como referências. Mencione cada referência no prompt como @Image1, @Video1 ou @Audio1, numeradas por tipo na ordem em que as entradas são conectadas: essas tags são reescritas nos rótulos que o HeyGen espera, e uma tag que aponta para uma referência não conectada gera um erro. Sem qualquer imagem ou vídeo de referência, o nó é executado como geração de texto para vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Versão do modelo usada para geração. (padrão: `"heygen-video-1"`) | DYNAMIC_COMBO | Sim | `"heygen-video-1"` |
| `prompt` | Descrição do vídeo, incluindo qualquer diálogo. Refira-se às referências conectadas como @Image1, @Video1, @Audio1, numeradas por tipo na ordem das entradas. (padrão: string vazia) | STRING | Sim | 1 a 16000 caracteres |
| `duration` | Duração do vídeo de saída em segundos. Mais de 15 segundos está disponível apenas sem imagens e vídeos de referência. (padrão: 5) | INT | Sim | 5 a 30 |
| `resolution` | Resolução de saída. 1080p e 2k exigem a proporção 16:9 ou 9:16; `"auto"` funciona nessas resoluções apenas sem referências. (padrão: `"768p"`) | COMBO | Sim | `"768p"`<br>`"480p"`<br>`"1080p"`<br>`"2k"` |
| `aspect_ratio` | Proporção de aspecto da saída. `"auto"` é 16:9 quando nenhuma referência está conectada; caso contrário, segue a primeira imagem de referência ou o primeiro vídeo de referência quando nenhuma imagem está conectada. (padrão: `"auto"`) | COMBO | Sim | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"` |
| `seed` | Semente para a geração. Os resultados ainda podem variar entre execuções com a mesma semente. (padrão: 42) | INT | Sim | 0 a 4294967295 |
| `reference_images` | Slot expansível: imagens de pessoas, produtos ou lugares para usar no vídeo (`image_1` ... `image_9`); refira-se a elas como @Image1, @Image2, ... Cada entrada deve conter exatamente uma imagem, e cada imagem deve ter uma proporção entre 1:4 e 4:1. | IMAGE | Não | 0 a 9 imagens |
| `reference_videos` | Slot expansível: vídeos para usar como referências (`video_1` ... `video_3`); refira-se a eles como @Video1, @Video2, ... No máximo 15 segundos de filmagem são usados no total. | VIDEO | Não | 0 a 3 vídeos |
| `reference_audios` | Slot expansível: clipes de áudio, como uma voz para um falante (`audio_1` ... `audio_3`); refira-se a eles como @Audio1, @Audio2, ... Requer pelo menos uma imagem ou vídeo de referência. Uma referência de voz precisa de alguns segundos de fala limpa, e clipes com menos de cerca de 2 segundos geralmente são ignorados. | AUDIO | Não | 0 a 3 clipes de áudio |
| `auto_duration` | Quando habilitado, a duração do vídeo segue o diálogo entre aspas no prompt (8 a 30 segundos, ou 8 a 15 com imagens ou vídeos de referência) e `duration` é ignorado. (padrão: `"disabled"`) | COMBO | Não | `"disabled"`<br>`"enabled"` |

### Restrições dos parâmetros

- **Limite de referências:** no máximo 15 referências no total: até 9 imagens, 3 vídeos e 3 clipes de áudio. Conectar mais gera um erro.
- **Áudio precisa de imagem ou vídeo:** o áudio de referência é rejeitado quando nenhuma imagem de referência e nenhum vídeo de referência estão conectados.
- **Regras para imagens de referência:** cada entrada `reference_images` deve conter exatamente uma imagem (um lote é rejeitado), e cada imagem deve ter proporção entre 1:4 e 4:1.
- **Tags do prompt:** `@ImageN`, `@VideoN` e `@AudioN` são correspondidas sem diferenciar maiúsculas de minúsculas. O número não deve exceder a contagem de referências conectadas desse tipo, e o prompt deve ser não vazio após remover espaços em branco das extremidades.
- **Modo:** com pelo menos uma imagem ou vídeo de referência, a requisição é uma execução de referência para vídeo; sem nenhuma, é uma execução simples de texto para vídeo.
- **Resolução 1080p e 2k:** `resolution` `"1080p"` ou `"2k"` exige `aspect_ratio` `"16:9"` ou `"9:16"`; `"auto"` é aceito nessas resoluções apenas quando nenhuma imagem de referência e nenhum vídeo de referência estão conectados.
- **Duração:** com imagens ou vídeos de referência, o vídeo gerado permanece em 15 segundos ou menos. Vídeos mais longos não precisam de imagens ou vídeos de referência; `auto_duration` apenas faz `duration` ser ignorado (8 a 30 segundos a partir do diálogo, 8 a 15 com referências), e não eleva esse limite.
- **Semente:** a semente apenas decide se o nó será reexecutado; os resultados não são reproduzíveis com a mesma semente.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `VIDEO` | O vídeo gerado com diálogo e som sincronizados. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenReferenceToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `415ffca1c385936e35bdb0451a23f03756e936b3b871d8d6a958da1ef8c56c36`
