# MiniMaxH3AddGuide

Este nó ancora uma imagem, um clipe curto, áudio ou um clipe com sua trilha sonora em qualquer quadro escolhido de um vídeo MiniMax H3. Ele adiciona um quadro-chave guia ao condicionamento no índice de quadro especificado, e você pode encadear vários desses nós para ancorar vários quadros no mesmo vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `positive` | O condicionamento ao qual o quadro-chave guia é anexado. | CONDITIONING | Sim | - |
| `latent` | O latente de áudio-vídeo MiniMax H3 que define o vídeo de destino. Deve ser um latente AV MiniMax H3 (aninhado, com dois tensores 5D de 24 canais cada). | LATENT | Sim | - |
| `frame_idx` | Índice do quadro para ancorar a imagem ou o primeiro quadro do clipe. Valores negativos são contados a partir do final do vídeo. (padrão: 0) | INT | Sim | -9999 a 9999 |
| `vae` | VAE de vídeo, necessário quando uma imagem é conectada. | VAE | Não | - |
| `audio_vae` | VAE de áudio, necessário quando um áudio é conectado. | VAE | Não | - |
| `image` | Imagem ou quadros de vídeo para ancorar. Lotes com múltiplos quadros são ancorados como um clipe e cortados para os comprimentos de clipe válidos do modelo: 5, 22, 39... (17k + 5) quadros. Lotes com menos de 5 quadros usam apenas a primeira imagem. | IMAGE | Não | - |
| `audio` | Trilha sonora para ancorar começando no mesmo índice de quadro, cortada para a duração restante do vídeo. | AUDIO | Não | - |

**Restrições:**
- Pelo menos um de `image` ou `audio` deve ser fornecido; caso contrário, o nó gera um erro.
- `vae` é obrigatório quando `image` é conectada.
- `audio_vae` é obrigatório quando `audio` é conectado.
- Lotes de `image` com menos de 5 quadros usam apenas a primeira imagem; lotes de 5 ou mais quadros são cortados para um comprimento de clipe válido (5, 22, 39, etc.).
- `frame_idx` deve posicionar o guia dentro do intervalo de quadros do vídeo, e um clipe de múltiplos quadros deve caber inteiramente no vídeo; caso contrário, o nó gera um erro.
- Quando o áudio é conectado, o índice do quadro não deve ultrapassar o final da trilha de áudio do vídeo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | O condicionamento com o quadro-chave guia adicionado, contendo o índice de quadro resolvido e, quando fornecido, os latentes de imagem ou áudio codificados. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3AddGuide/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7a2f742421cc2655bd9c914258801e4538f1554a7c5e2b0836b2df1577f5a104`
