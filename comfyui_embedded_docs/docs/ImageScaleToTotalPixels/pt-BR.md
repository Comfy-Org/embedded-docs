> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToTotalPixels/pt-BR.md)

O nó ImageScaleToTotalPixels é projetado para redimensionar imagens para um número total especificado de pixels, mantendo a proporção original. Ele oferece vários métodos para ampliar a imagem a fim de atingir a contagem de pixels desejada.

## Entradas

| Parâmetro       | Tipo de Dados | Descrição                                                                 |
|-----------------|---------------|---------------------------------------------------------------------------|
| `image`         | `IMAGE`       | A imagem de entrada a ser ampliada para o número total de pixels especificado. |
| `upscale_method`| COMBO[STRING] | O método utilizado para ampliar a imagem. Afeta a qualidade e as características da imagem ampliada. |
| `megapixels`    | `FLOAT`       | O tamanho alvo da imagem em megapixels. Isso determina o número total de pixels na imagem ampliada. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição                                                                                |
|-----------|---------------|------------------------------------------------------------------------------------------|
| `image`   | `IMAGE`       | A imagem ampliada com o número total de pixels especificado, mantendo a proporção original. |
