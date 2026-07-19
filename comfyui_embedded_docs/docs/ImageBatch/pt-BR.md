# Imagens em Lote

O nó `ImageBatch` é projetado para combinar duas imagens em um único lote. Se as dimensões das imagens não coincidirem, ele redimensiona automaticamente a segunda imagem para corresponder às dimensões da primeira antes de combiná-las.

## Entradas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `imagem1` | A primeira imagem a ser combinada no lote. Ela serve como referência para as dimensões às quais a segunda imagem será ajustada, se necessário. | `IMAGE` |
| `imagem2` | A segunda imagem a ser combinada no lote. Ela é automaticamente redimensionada para corresponder às dimensões da primeira imagem, caso sejam diferentes. | `IMAGE` |

## Saídas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `image` | O lote combinado de imagens, com a segunda imagem redimensionada para corresponder às dimensões da primeira, se necessário. | `IMAGE` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBatch/pt-BR.md)
