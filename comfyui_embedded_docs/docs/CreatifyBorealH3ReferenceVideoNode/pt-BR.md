# Creatify Boreal-H3 Reference to Video

Creatify Boreal-H3 Reference to Video gera um vídeo com som guiado por imagens, vídeos e áudios de referência, usando o modelo H3 pós-treinado da Creatify, criado para anúncios em vídeo. Nomeie as referências no prompt como `@Image1`, `@Video1` e `@Audio1` para controlar o que cada uma contribui.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Slot expansível para até 9 imagens de referência (`image_1` ... `image_9`), referenciadas no prompt como `@Image1` ... `@Image9` na ordem de conexão. Pelo menos uma imagem ou vídeo é obrigatório, e no máximo 12 referências no total. | IMAGE | Não | Até 9 imagens |
| `reference_videos` | Slot expansível para até 3 vídeos de referência (`video_1` ... `video_3`), cada um com pelo menos 1 segundo de duração. O som deles é reutilizado quando o prompt pede para continuá-lo; uma nova fala no prompt o substitui. No máximo 15 segundos de vídeo de referência são cobrados no total. | VIDEO | Não | Até 3 vídeos |
| `reference_audios` | Slot expansível para até 3 clipes de referência (`audio_1` ... `audio_3`). A fala orienta a voz, e não as palavras, e música instrumental pode se tornar a trilha sonora. | AUDIO | Não | Até 3 clipes |
| `prompt` | Prompt de texto que descreve o vídeo e faz referência às referências conectadas. Deve conter pelo menos um caractere que não seja espaço em branco. | STRING | Sim | Qualquer texto não vazio |
| `resolution` | Resolução do vídeo de saída (padrão: `"768p"`). | COMBO | Sim | `"768p"`<br>`"1088p"`<br>`"2k"` |
| `aspect_ratio` | Proporção de aspecto do vídeo de saída. `"auto"` segue a primeira imagem de referência. Com apenas vídeos de referência em `"1088p"`, o nó escolhe a proporção suportada mais próxima do primeiro vídeo, que pode diferir de sua proporção exata; em outras resoluções, `"auto"` é passado para a Creatify como está (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Duração do vídeo em segundos (padrão: 5). Em `"2k"`, o máximo é 14 segundos. | INT | Sim | 1 a 15 (passo 1) |
| `prompt_enhancement` | Como a Creatify reescreve o prompt antes da renderização: `"auto"` e `"ads"` o transformam em um prompt de anúncio em vídeo e podem adicionar falas, `"general"` o reescreve para qualquer outro vídeo, `"none"` o renderiza como escrito (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"ads"`<br>`"general"`<br>`"none"` |
| `seed` | A semente controla se o nó é executado novamente. Nenhuma semente é enviada ao Boreal-H3, então executar novamente com as mesmas entradas pode produzir um vídeo diferente (padrão: 42). | INT | Sim | 0 a 2147483647 |

**Restrições:** conecte pelo menos uma imagem ou vídeo de referência; apenas áudio não é aceito. Uma tag de referência que aponta para além do número de referências conectadas daquele tipo gera um erro, e o mesmo ocorre com mais de 12 referências no total. Com `"1088p"` e `"auto"` e sem imagem de referência, a proporção de aspecto é obtida a partir do primeiro vídeo de referência.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `VIDEO` | O vídeo gerado com som. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreatifyBorealH3ReferenceVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c6e60b83a8e02262fcbae7c04f4f379cf665a9e25b2fa00836047fe56d0fa064`
