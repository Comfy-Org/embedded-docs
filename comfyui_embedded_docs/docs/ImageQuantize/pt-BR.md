> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageQuantize/pt-BR.md)

O nó ImageQuantize é projetado para reduzir o número de cores em uma imagem para uma quantidade especificada, aplicando opcionalmente técnicas de *dithering* para manter a qualidade visual. Este processo é útil para criar imagens baseadas em paleta ou reduzir a complexidade de cores para certas aplicações.

## Entradas

| Campo   | Tipo de Dados | Descrição                                                                       |
|---------|-------------|-----------------------------------------------------------------------------------|
| `image` | `IMAGE`     | O tensor de imagem de entrada a ser quantizado. Afeta a execução do nó por ser o dado principal sobre o qual a redução de cores é realizada. |
| `colors`| `INT`       | Especifica o número de cores para o qual a imagem será reduzida. Influencia diretamente o processo de quantização ao determinar o tamanho da paleta de cores. |
| `dither`| COMBO[STRING] | Determina a técnica de *dithering* a ser aplicada durante a quantização, afetando a qualidade visual e a aparência da imagem de saída. |

## Saídas

| Campo | Tipo de Dados | Descrição                                                                   |
|-------|-------------|-------------------------------------------------------------------------------|
| `image`| `IMAGE`     | A versão quantizada da imagem de entrada, com complexidade de cores reduzida e opcionalmente com *dithering* aplicado para manter a qualidade visual. |
