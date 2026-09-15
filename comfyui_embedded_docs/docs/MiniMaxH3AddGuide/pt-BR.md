# Adicionar guia para MiniMax H3

Este nó ancora uma imagem, um clipe curto, áudio ou um clipe com sua trilha sonora em qualquer frame de um vídeo do MiniMax H3. Ele adiciona um keyframe de guia ao condicionamento no índice de frame escolhido, e você pode encadear vários desses nós para ancorar vários frames no mesmo vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `positive` | O condicionamento ao qual o keyframe de guia é anexado. | CONDITIONING | Sim | - |
| `vae` | VAE de vídeo, necessário quando uma imagem está conectada. | VAE | Não | - |
| `audio_vae` | VAE de áudio, necessário quando um áudio está conectado. | VAE | Não | - |
| `latent` | O latent de áudio e vídeo do MiniMax H3 que define o vídeo de destino. Deve ser um latent AV do MiniMax H3 (aninhado, com dois tensores 5D, sendo que o tensor de vídeo tem 24 canais). | LATENT | Sim | - |
| `image` | Imagem ou frames de vídeo a ancorar. Lotes de múltiplos frames são ancorados como um clipe e recortados para os comprimentos de clipe válidos do modelo: 5, 22, 39... (17k + 5) frames. Lotes com menos de 5 frames usam apenas a primeira imagem. | IMAGE | Não | - |
| `audio` | Trilha sonora a ancorar começando no mesmo índice de frame, recortada para a duração restante do vídeo. | AUDIO | Não | - |
| `frame_idx` | Índice de frame no qual ancorar a imagem ou o primeiro frame do clipe. Valores negativos são contados a partir do fim do vídeo. (padrão: 0) | INT | Sim | -9999 a 9999 |

**Restrições:**
- Pelo menos um entre `image` ou `audio` deve ser fornecido; caso contrário, o nó lança um erro.
- `vae` é obrigatório quando `image` está conectado.
- `audio_vae` é obrigatório quando `audio` está conectado.
- Lotes de `image` com menos de 5 frames usam apenas a primeira imagem; lotes com 5 frames ou mais são recortados para um comprimento de clipe válido (5, 22, 39 etc.).
- `frame_idx` deve posicionar o keyframe de guia dentro do intervalo de frames do vídeo, e um clipe de múltiplos frames deve caber inteiramente no vídeo; caso contrário, o nó lança um erro.
- Quando áudio está conectado, o índice de frame não pode ultrapassar o fim da faixa de áudio do vídeo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | O condicionamento com o keyframe de guia adicionado, contendo o índice de frame resolvido e, quando fornecidos, os latents de imagem ou áudio codificados. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3AddGuide/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7a2f742421cc2655bd9c914258801e4538f1554a7c5e2b0836b2df1577f5a104`
