# TextEncodeZImageOmni

TextEncodeZImageOmni codifica um prompt de texto juntamente com até três imagens de referência opcionais em um formato de condicionamento para modelos de geração de imagem. O prompt é tokenizado e codificado com o modelo CLIP, e cada imagem conectada pode, opcionalmente, ser processada por um codificador de visão e/ou por um VAE, para que referências visuais sejam incorporadas junto ao texto. Este nó é marcado como experimental.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para tokenizar e codificar o prompt de texto. | CLIP | Sim |  |
| `codificador_de_imagem` | Um codificador de visão opcional. Se fornecido, ele é usado para codificar as imagens de entrada, e os embeddings resultantes são adicionados ao condicionamento. | CLIP_VISION | Não |  |
| `prompt` | O prompt de texto a ser codificado. Suporta entrada de múltiplas linhas e prompts dinâmicos. | STRING | Sim |  |
| `redimensionar_imagens_automaticamente` | Quando ativado (padrão: True), as imagens de entrada são redimensionadas automaticamente antes da codificação pelo VAE, de modo que sua área total de pixels fique próxima de 1024x1024, com as dimensões arredondadas para múltiplos de 8. | BOOLEAN | Não | True<br>False |
| `vae` | Um modelo VAE opcional. Se fornecido, ele é usado para codificar as imagens de entrada em representações latentes, que são adicionadas ao condicionamento como latentes de referência. | VAE | Não |  |
| `imagem1` | A primeira imagem de referência opcional. | IMAGE | Não |  |
| `imagem2` | A segunda imagem de referência opcional. | IMAGE | Não |  |
| `imagem3` | A terceira imagem de referência opcional. | IMAGE | Não |  |

**Observação:** O nó aceita no máximo três imagens (`image1`, `image2`, `image3`). As entradas `image_encoder` e `vae` são usadas somente quando pelo menos uma imagem é fornecida; quando ambas estão conectadas, cada imagem é processada por ambas. Quando `auto_resize_images` está como True e um `vae` está conectado, as imagens são redimensionadas para ter uma área total de pixels próxima de 1024x1024 antes da codificação.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | A saída de condicionamento final. Ela contém o prompt de texto codificado e, quando imagens são fornecidas, pode incluir embeddings de imagem codificados, latentes de referência e embeddings de texto extras derivados do modelo de espaço reservado da imagem. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeZImageOmni/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b40a3150f536b6f37e2b53e6d9992fcb4fd32dceb540c0a76773a7ba1af9a7b8`
