# MiniMax H3 Image Conditioning

Transforma um prompt em condicionamento e em um latent vazio para uma imagem estática com o MiniMax H3 Image. Sem imagens, é texto para imagem; com imagens conectadas, ele as edita, e o prompt se refere a elas como `<Picture 1>`, `<Picture 2>` e assim por diante.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP do MiniMax H3 Image, que tokeniza o prompt com quaisquer imagens de referência e codifica o condicionamento. | CLIP | Sim | - |
| `vae` | O VAE do MiniMax H3 Image. Com ele, as imagens também são ancoradas como latents de referência; sem ele, elas apenas condicionam o codificador de texto. | VAE | Não | - |
| `prompt` | O que gerar, ou como editar as imagens de referência. | STRING | Sim | Texto multilinha |
| `width` | Largura da saída em pixels. 0 usa a largura de `image_1` após seu redimensionamento de referência, ou 2048 sem imagens. Padrão: 0. | INT | Sim | 0 a MAX_RESOLUTION (passo: 32) |
| `height` | Altura da saída em pixels. 0 usa a altura de `image_1` após seu redimensionamento de referência, ou 2048 sem imagens. Padrão: 0. | INT | Sim | 0 a MAX_RESOLUTION (passo: 32) |
| `images` | Grupo expansível de imagens de referência, de `image_1` em diante; `image_1` é a imagem a ser editada. O prompt se refere a elas como `<Picture n>`. | AUTOGROW | Não | 0 a 100 imagens |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento para o amostrador do MiniMax H3 Image, com os latents de referência anexados quando imagens estão conectadas. | CONDITIONING |
| `latent` | Latent vazio para uma imagem, 24 canais com um dezesseis avos do tamanho da saída. | LATENT |

Nota: O modelo é ajustado para uma área de 2048x2048 pixels, então deixe `width` e `height` em 0, a menos que uma tela diferente seja necessária.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b0927bbc44ac82e8a23b1edb5470c0cc8945844c326a352d75495ed801d11b1d`
