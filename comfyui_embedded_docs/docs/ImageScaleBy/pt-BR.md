> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleBy/pt-BR.md)

O nó ImageScaleBy é projetado para aumentar a escala de imagens por um fator de escala especificado usando vários métodos de interpolação. Ele permite o ajuste do tamanho da imagem de maneira flexível, atendendo a diferentes necessidades de aumento de escala.

## Entradas

| Parâmetro       | Tipo de Dados | Descrição                                                                 |
|-----------------|-------------|----------------------------------------------------------------------------|
| `image`         | `IMAGE`     | A imagem de entrada a ser ampliada. Este parâmetro é crucial, pois fornece a imagem base que passará pelo processo de aumento de escala. |
| `upscale_method`| COMBO[STRING] | Especifica o método de interpolação a ser usado para o aumento de escala. A escolha do método pode afetar a qualidade e as características da imagem ampliada. |
| `scale_by`      | `FLOAT`     | O fator pelo qual a imagem será ampliada. Isso determina o aumento no tamanho da imagem de saída em relação à imagem de entrada. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição                                                   |
|-----------|-------------|---------------------------------------------------------------|
| `image`   | `IMAGE`     | A imagem ampliada, que é maior do que a imagem de entrada de acordo com o fator de escala e o método de interpolação especificados. |
