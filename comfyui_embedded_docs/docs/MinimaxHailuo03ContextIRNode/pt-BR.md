# MinimaxHailuo03ContextIRNode

Este nó usa o MiniMax H3 Context IR para analisar sua descrição de texto e qualquer mídia anexada e, em seguida, produz um prompt de vídeo estruturado e reforçado. O prompt retornado é projetado para ser conectado à entrada de prompt de um nó de vídeo MiniMax H3; se você anexar mídia lá, anexe a mesma mídia na mesma ordem, pois o prompt aprimorado se refere à mídia por posição.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `model` | Modelo a ser usado para aprimoramento de prompt. | COMBO | Sim | `"MiniMax H3"` |
| `prompt` | Descrição do vídeo que você pretende gerar. Não pode estar vazio. (padrão: `""`) | STRING | Sim | Qualquer texto |
| `duration` | Duração do vídeo que você pretende gerar, em segundos (4-15). (padrão: 5) | INT | Sim | 4 a 15 |
| `ratio` | Proporção de aspecto do vídeo que você pretende gerar. `"adaptive"` exige pelo menos uma entrada de imagem, vídeo ou áudio. (padrão: `"adaptive"`) | COMBO | Sim | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `reference_images` | Imagens de referência de assunto ou estilo, referidas no prompt como "Image 1"..."Image 9" na ordem de conexão. Até 9 imagens. | IMAGE | Não | 0 a 9 imagens |
| `reference_videos` | Vídeos de referência de movimento ou cena, referidos no prompt como "Video 1"..."Video 3" na ordem de conexão. Até 3 vídeos, de 2 a 15 segundos cada, 15 segundos no total. | VIDEO | Não | 0 a 3 vídeos |
| `reference_audios` | Referências de áudio, referidas no prompt como "Audio 1"..."Audio 3" na ordem de conexão. Até 3 clipes, de 2 a 15 segundos cada, 15 segundos no total. Não podem ser usadas sem uma imagem ou vídeo de referência. | AUDIO | Não | 0 a 3 clipes |
| `first_frame` | Primeiro quadro do vídeo que você pretende gerar. Não pode ser combinado com mídia de referência. | IMAGE | Não | Imagem única |
| `last_frame` | Último quadro do vídeo que você pretende gerar. Não pode ser combinado com mídia de referência. | IMAGE | Não | Imagem única |

### Restrições de parâmetros

- As entradas `prompt`, `duration`, `ratio`, `reference_images`, `reference_videos` e `reference_audios` fazem parte do grupo de opções do `model`.
- `first_frame` e `last_frame` não podem ser combinados com qualquer mídia de referência.
- `reference_audios` não pode ser usado a menos que pelo menos uma `reference_image` ou `reference_video` também esteja conectada.
- Quando nenhum quadro e nenhuma mídia de referência estiverem conectados, `ratio` não pode ser definido como `"adaptive"`.
- Os vídeos de referência devem ter aproximadamente 2 a 15 segundos cada, com duração total de no máximo 15 segundos. A taxa de quadros deve estar entre 23.9 e 60.5 FPS.
- Os áudios de referência devem ter aproximadamente 2 a 15 segundos cada, com duração total de no máximo 15 segundos.
- `first_frame`, `last_frame` e cada imagem de referência devem ter pelo menos 256x256 pixels e ter uma proporção de aspecto entre 0.4 e 2.5.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `STRING` | O prompt de vídeo estruturado e aprimorado gerado pelo MiniMax H3 Context IR. Ele pode ser conectado à entrada de prompt de um nó de geração de vídeo MiniMax H3. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ContextIRNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `73015517f9c0f55f0aceeef935508a372e0d95668e4733d1c8100b53e4afa7e2`
