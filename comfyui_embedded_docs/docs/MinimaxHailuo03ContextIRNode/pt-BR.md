# MiniMax H3 Context IR (Aprimorador de Prompt)

## Visão geral

Este nó usa o MiniMax H3 Context IR para analisar sua descrição de texto e qualquer mídia anexada e, em seguida, produz um prompt de vídeo estruturado e mais forte. O prompt retornado foi projetado para ser conectado à entrada de prompt de um nó de vídeo MiniMax H3; se você anexar mídia lá, anexe a mesma mídia na mesma ordem, porque o prompt aprimorado se refere à mídia por posição.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a ser usado para aprimoramento do prompt. | DYNAMIC_COMBO | Sim | `"MiniMax H3"` |
| `first_frame` | Primeiro quadro do vídeo que você pretende gerar. Não pode ser combinado com mídia de referência. | IMAGE | Não | Imagem única |
| `last_frame` | Último quadro do vídeo que você pretende gerar. Não pode ser combinado com mídia de referência. | IMAGE | Não | Imagem única |

### Entradas do MiniMax H3

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrição do vídeo que você pretende gerar. Não pode estar vazio. (padrão: `""`) | STRING | Sim | Qualquer texto (não pode estar vazio) |
| `duration` | Duração do vídeo que você pretende gerar, em segundos (4-15). (padrão: 5) | INT | Sim | 4 a 15 |
| `ratio` | Proporção de aspecto do vídeo que você pretende gerar. `"adaptive"` exige pelo menos uma entrada de imagem, vídeo ou áudio. (padrão: `"adaptive"`) | COMBO | Sim | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |

### Entradas de referência

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Imagens de referência de assunto ou estilo, referidas no prompt como "Image 1".."Image 9" na ordem de conexão. Até 9 imagens. Slot expansível: conecte `image_1`...`image_9`. | IMAGE | Não | 0 a 9 imagens |
| `reference_videos` | Vídeos de referência de movimento ou cena, referidos no prompt como "Video 1".."Video 3" na ordem de conexão. Até 3 vídeos, 2-15 segundos cada, 15 segundos no total. Slot expansível: conecte `video_1`...`video_3`. | VIDEO | Não | 0 a 3 vídeos |
| `reference_audios` | Referências de áudio, referidas no prompt como "Audio 1".."Audio 3" na ordem de conexão. Até 3 clipes, 2-15 segundos cada, 15 segundos no total. Não podem ser usadas sem uma imagem ou vídeo de referência. Slot expansível: conecte `audio_1`...`audio_3`. | AUDIO | Não | 0 a 3 clipes |

### Restrições de parâmetros

- As entradas `prompt`, `duration`, `ratio`, `reference_images`, `reference_videos` e `reference_audios` fazem parte do grupo de opções do `model` e aparecem quando "MiniMax H3" está selecionado.
- `first_frame` e `last_frame` não podem ser combinados com nenhuma mídia de referência.
- `reference_audios` não pode ser usado a menos que pelo menos uma `reference_image` ou um `reference_video` também esteja conectado.
- Quando nenhum quadro e nenhuma mídia de referência estiverem conectados, `ratio` não pode ser definido como `"adaptive"`.
- Os vídeos de referência devem ter aproximadamente 2-15 segundos cada, com duração total não superior a 15 segundos. A taxa de quadros deles deve estar entre 23.9 e 60.5 FPS.
- Os áudios de referência devem ter aproximadamente 2-15 segundos cada, com duração total não superior a 15 segundos.
- `first_frame`, `last_frame` e cada imagem de referência devem ter pelo menos 256x256 pixels e uma proporção de aspecto entre 0.4 e 2.5.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `STRING` | O prompt de vídeo estruturado e aprimorado gerado pelo MiniMax H3 Context IR. Ele pode ser conectado à entrada de prompt de um nó de geração de vídeo MiniMax H3. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ContextIRNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `73015517f9c0f55f0aceeef935508a372e0d95668e4733d1c8100b53e4afa7e2`
