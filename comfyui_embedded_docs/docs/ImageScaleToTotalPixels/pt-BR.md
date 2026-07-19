# Redimensionar Imagem para Total de Pixels

O nó ImageScaleToTotalPixels é projetado para redimensionar imagens para um número total de pixels especificado, mantendo a proporção original. Ele oferece diversos métodos para aumentar a escala da imagem e atingir a contagem de pixels desejada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagem` | A imagem de entrada a ser ampliada para o número total de pixels especificado. | `IMAGE` |
| `método de upscaling` | O método usado para ampliar a imagem. Afeta a qualidade e as características da imagem ampliada. | COMBO[STRING] |
| `megapixels` | O tamanho alvo da imagem em megapixels. Isso determina o número total de pixels na imagem ampliada. | `FLOAT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagem` | A imagem ampliada com o número total de pixels especificado, mantendo a proporção original. | `IMAGE` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToTotalPixels/pt-BR.md)
