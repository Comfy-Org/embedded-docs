# HeyGen Video 1.0 Reference to Video

Gere um vídeo com diálogo e som sincronizados a partir de um prompt de texto usando o HeyGen Video 1.0, opcionalmente guiado por material de referência conectado. Imagens de pessoas, produtos ou lugares, vídeos para reutilizar e clipes de áudio que fornecem uma voz podem ser usados como referências. Mencione cada referência no prompt como @Image1, @Video1 ou @Audio1, numeradas por tipo na ordem em que as entradas são conectadas: essas tags são reescritas nos rótulos que o HeyGen espera, e uma tag que aponta para uma referência que não está conectada gera um erro. Sem qualquer imagem ou vídeo de referência, o nó executa como geração de texto para vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Versão do modelo usada para geração. (padrão: `"heygen-video-1"`) | DYNAMIC_COMBO | Sim | `"heygen-video-1"` |
| `prompt` | Descrição do vídeo, incluindo qualquer diálogo. Consulte as referências conectadas como @Image1, @Video1, @Audio1, numeradas por tipo na ordem de entrada. (padrão: string vazia) | STRING | Sim | 1 a 32000 caracteres |
| `duration` | Duração do vídeo de saída em segundos. (padrão: 5) | INT | Sim | 5 a 15 |
| `resolution` | Resolução de saída. 2k exige uma proporção de aspecto de 16:9 ou 9:16; `"auto"` só funciona em 2k sem referências. (padrão: `"768p"`) | COMBO | Sim | `"768p"`<br>`"480p"`<br>`"2k"` |
| `aspect_ratio` | Proporção de aspecto de saída. `"auto"` é 16:9 quando nenhuma referência está conectada, caso contrário, segue a primeira imagem de referência, ou o primeiro vídeo de referência quando nenhuma imagem está conectada. (padrão: `"auto"`) | COMBO | Sim | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"` |
| `seed` | Seed para a geração. Os resultados ainda podem variar entre execuções com a mesma seed. (padrão: 42) | INT | Sim | 0 a 4294967295 |
| `reference_images` | Slot expansível: imagens de pessoas, produtos ou lugares para usar no vídeo (`image_1` ... `image_9`); consulte-as como @Image1, @Image2, ... Cada entrada deve conter exatamente uma imagem, e cada imagem deve ter uma proporção de aspecto entre 1:4 e 4:1. | IMAGE | Não | 0 a 9 imagens |
| `reference_videos` | Slot expansível: vídeos para usar como referências (`video_1` ... `video_3`); consulte-os como @Video1, @Video2, ... | VIDEO | Não | 0 a 3 vídeos |
| `reference_audios` | Slot expansível: clipes de áudio, como uma voz para um falante (`audio_1` ... `audio_3`); consulte-os como @Audio1, @Audio2, ... Requer pelo menos uma imagem ou vídeo de referência. Uma referência de voz precisa de alguns segundos de fala limpa, e clipes com menos de cerca de 2 segundos geralmente são ignorados. | AUDIO | Não | 0 a 3 clipes de áudio |

### Restrições dos parâmetros

- **Limite de referências:** no máximo 12 referências no total entre `reference_images`, `reference_videos` e `reference_audios`; conectar mais gera um erro.
- **Áudio precisa de imagem ou vídeo:** o áudio de referência é rejeitado quando nenhuma imagem de referência e nenhum vídeo de referência estão conectados.
- **Regras de imagem de referência:** cada entrada `reference_images` deve conter exatamente uma imagem (um lote é rejeitado), e cada imagem deve ter proporção de aspecto entre 1:4 e 4:1.
- **Tags de prompt:** `@ImageN`, `@VideoN` e `@AudioN` são correspondidas sem distinção entre maiúsculas e minúsculas. O número não deve exceder a contagem de referências conectadas desse tipo, e o prompt deve ser não vazio após remover espaços em branco.
- **Modo:** com pelo menos uma imagem ou vídeo de referência, a solicitação é uma execução de referência para vídeo; sem nenhum, é uma execução simples de texto para vídeo.
- **Resolução 2k:** `resolution` `"2k"` exige `aspect_ratio` `"16:9"` ou `"9:16"`; `"auto"` só é aceito em 2k quando nenhuma imagem e nenhum vídeo de referência estão conectados.
- **Seed:** a seed apenas decide se o nó será executado novamente; os resultados não são reproduzíveis com a mesma seed.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `VIDEO` | O vídeo gerado com diálogo e som sincronizados. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenReferenceToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f3fae5dce59c90d65ad8eff2c992819f29a71e3a3e13fa91c1e7479a9cd6fcdc`
