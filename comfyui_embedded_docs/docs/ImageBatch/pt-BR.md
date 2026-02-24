> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBatch/pt-BR.md)

O nó `ImageBatch` é projetado para combinar duas imagens em um único lote. Se as dimensões das imagens não coincidirem, ele redimensiona automaticamente a segunda imagem para corresponder às dimensões da primeira antes de combiná-las.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `image1`  | `IMAGE`     | A primeira imagem a ser combinada no lote. Serve como referência para as dimensões às quais a segunda imagem será ajustada, se necessário. |
| `image2`  | `IMAGE`     | A segunda imagem a ser combinada no lote. É redimensionada automaticamente para corresponder às dimensões da primeira imagem se elas forem diferentes. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | O lote combinado de imagens, com a segunda imagem redimensionada para corresponder às dimensões da primeira, se necessário. |
