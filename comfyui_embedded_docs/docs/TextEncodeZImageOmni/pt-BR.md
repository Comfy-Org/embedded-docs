> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeZImageOmni/pt-BR.md)

O nó TextEncodeZImageOmni é um nó de condicionamento avançado que codifica um prompt de texto juntamente com imagens de referência opcionais em um formato de condicionamento adequado para modelos de geração de imagens. Ele pode processar até três imagens, opcionalmente codificando-as com um codificador de visão e/ou um VAE para produzir latentes de referência, e integra essas referências visuais ao prompt de texto usando uma estrutura de modelo específica.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Sim | | O modelo CLIP usado para tokenizar e codificar o prompt de texto. |
| `image_encoder` | CLIPVision | Não | | Um modelo de codificador de visão opcional. Se fornecido, será usado para codificar as imagens de entrada, e os embeddings resultantes serão adicionados ao condicionamento. |
| `prompt` | STRING | Sim | | O prompt de texto a ser codificado. Este campo suporta entrada multilinha e prompts dinâmicos. |
| `auto_resize_images` | BOOLEAN | Não | | Quando ativado (padrão: Verdadeiro), as imagens de entrada serão redimensionadas automaticamente com base em sua área de pixels antes de serem passadas para o VAE para codificação. |
| `vae` | VAE | Não | | Um modelo VAE opcional. Se fornecido, será usado para codificar as imagens de entrada em representações latentes, que são adicionadas ao condicionamento como latentes de referência. |
| `image1` | IMAGE | Não | | A primeira imagem de referência opcional. |
| `image2` | IMAGE | Não | | A segunda imagem de referência opcional. |
| `image3` | IMAGE | Não | | A terceira imagem de referência opcional. |

**Nota:** O nó pode aceitar no máximo três imagens (`image1`, `image2`, `image3`). As entradas `image_encoder` e `vae` só são utilizadas se pelo menos uma imagem for fornecida. Quando `auto_resize_images` está ativado e um `vae` está conectado, as imagens são redimensionadas para ter uma área total de pixels próxima a 1024x1024 antes da codificação.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | A saída de condicionamento final, que contém o prompt de texto codificado e pode incluir embeddings de imagem codificados e/ou latentes de referência, caso imagens tenham sido fornecidas. |

---
**Source fingerprint (SHA-256):** `daa4205acdf72503180eeedb4142708d239d4ff0f689012a298264ae2d8ea949`
