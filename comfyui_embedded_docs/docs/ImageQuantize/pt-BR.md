> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageQuantize/pt-BR.md)

O nó ImageQuantize foi projetado para reduzir o número de cores em uma imagem para uma quantidade especificada, aplicando opcionalmente técnicas de pontilhamento para manter a qualidade visual. Esse processo é útil para criar imagens baseadas em paletas ou reduzir a complexidade de cores para determinadas aplicações.

## Entradas

| Campo   | Tipo de Dado | Descrição                                                                       |
|---------|--------------|---------------------------------------------------------------------------------|
| `imagem` | `IMAGE`      | O tensor de imagem de entrada a ser quantizado. Ele afeta a execução do nó por ser o dado principal sobre o qual a redução de cores é realizada. |
| `cores`| `INT`        | Especifica o número de cores para reduzir a imagem. Influencia diretamente o processo de quantização ao determinar o tamanho da paleta de cores. |
| `dithering`| COMBO[STRING]| Determina a técnica de pontilhamento a ser aplicada durante a quantização, afetando a qualidade visual e a aparência da imagem de saída. |

## Saídas

| Campo | Tipo de Dado | Descrição                                                                   |
|-------|--------------|-----------------------------------------------------------------------------|
| `imagem`| `IMAGE`      | A versão quantizada da imagem de entrada, com complexidade de cores reduzida e, opcionalmente, pontilhada para manter a qualidade visual. |