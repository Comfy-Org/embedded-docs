O nó **ImageScaleBy** foi projetado para redimensionar imagens com base em um fator de escala específico, utilizando diversos métodos de interpolação. Ele permite ajustar o tamanho da imagem de forma flexível, atendendo a diferentes necessidades de redimensionamento.

## Entradas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagem` | A imagem de entrada a ser redimensionada. Este parâmetro é essencial, pois fornece a imagem base que passará pelo processo de redimensionamento. | `IMAGE` |
| `método de upscaling` | Especifica o método de interpolação a ser usado para o redimensionamento. A escolha do método pode afetar a qualidade e as características da imagem redimensionada. | COMBO[STRING] |
| `fator de escala` | O fator pelo qual a imagem será redimensionada. Isso determina o aumento no tamanho da imagem de saída em relação à imagem de entrada. | `FLOAT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagem` | A imagem redimensionada, que é maior que a imagem de entrada de acordo com o fator de escala e o método de interpolação especificados. | `IMAGE` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleBy/pt-BR.md)
