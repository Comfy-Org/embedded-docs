> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompositeMasked/pt-BR.md)

O nó `ImageCompositeMasked` é projetado para composição de imagens, permitindo a sobreposição de uma imagem de origem sobre uma imagem de destino em coordenadas especificadas, com redimensionamento e mascaramento opcionais.

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|--------------|-----------|
| `destino` | `IMAGE` | A imagem de destino sobre a qual a imagem de origem será composta. Ela serve como plano de fundo para a operação de composição. |
| `fonte` | `IMAGE` | A imagem de origem a ser composta sobre a imagem de destino. Esta imagem pode opcionalmente ser redimensionada para se ajustar às dimensões da imagem de destino. |
| `x` | `INT` | A coordenada x na imagem de destino onde o canto superior esquerdo da imagem de origem será posicionado. |
| `y` | `INT` | A coordenada y na imagem de destino onde o canto superior esquerdo da imagem de origem será posicionado. |
| `redimensionar_fonte` | `BOOLEAN` | Um indicador booleano que define se a imagem de origem deve ser redimensionada para corresponder às dimensões da imagem de destino. |
| `máscara` | `MASK` | Uma máscara opcional que especifica quais partes da imagem de origem devem ser compostas sobre a imagem de destino. Isso permite operações de composição mais complexas, como mesclagem ou sobreposições parciais. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|--------------|-----------|
| `image` | `IMAGE` | A imagem resultante após a operação de composição, que combina elementos de ambas as imagens. |