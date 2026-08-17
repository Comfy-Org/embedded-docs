# TextEncodeZImageOmni

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para tokenizar e codificar o prompt de texto. | CLIP | Sim |  |
| `image_encoder` | Um codificador de visão opcional. Se fornecido, será usado para codificar as imagens de entrada, e os embeddings resultantes serão adicionados ao condicionamento. | CLIPVision | Não |  |
| `prompt` | O prompt de texto a ser codificado. Este campo aceita entrada multilinha e prompts dinâmicos. | STRING | Sim |  |
| `auto_resize_images` | Quando ativado (padrão: True), as imagens de entrada serão redimensionadas automaticamente com base em sua área de pixel antes de serem passadas ao VAE para codificação. Esta é uma configuração avançada. | BOOLEAN | Não |  |
| `vae` | Um modelo VAE opcional. Se fornecido, será usado para codificar as imagens de entrada em representações latentes, que são adicionadas ao condicionamento como latentes de referência. | VAE | Não |  |
| `image1` | A primeira imagem de referência opcional. | IMAGE | Não |  |
| `image2` | A segunda imagem de referência opcional. | IMAGE | Não |  |
| `image3` | A terceira imagem de referência opcional. | IMAGE | Não |  |

**Nota:** O nó aceita no máximo três imagens (`image1`, `image2`, `image3`). As entradas `image_encoder` e `vae` só são utilizadas se pelo menos uma imagem for fornecida. Quando `auto_resize_images` está definido como True e um `vae` está conectado, as imagens são redimensionadas para ter uma área total de pixels próxima a 1024x1024 pixels, com dimensões arredondadas para múltiplos de 8, antes da codificação. Se nenhuma imagem for fornecida, o nó codifica o prompt de texto sem referências visuais.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | A saída de condicionamento final, que contém o prompt de texto codificado e pode incluir embeddings de imagem codificados e/ou latentes de referência, caso imagens tenham sido fornecidas. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeZImageOmni/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b40a3150f536b6f37e2b53e6d9992fcb4fd32dceb540c0a76773a7ba1af9a7b8`
