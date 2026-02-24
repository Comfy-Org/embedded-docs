> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCompositeMasked/pt-BR.md)

O nó LatentCompositeMasked é projetado para mesclar duas representações latentes em coordenadas especificadas, opcionalmente usando uma máscara para uma composição mais controlada. Este nó permite a criação de imagens latentes complexas sobrepondo partes de uma imagem em outra, com a capacidade de redimensionar a imagem de origem para um encaixe perfeito.

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `destination` | `LATENT`    | A representação latente sobre a qual outra representação latente será composta. Atua como a camada base para a operação de composição. |
| `source` | `LATENT`    | A representação latente a ser composta sobre o destino. Esta camada de origem pode ser redimensionada e posicionada de acordo com os parâmetros especificados. |
| `x` | `INT`       | A coordenada x na representação latente de destino onde a origem será posicionada. Permite o posicionamento preciso da camada de origem. |
| `y` | `INT`       | A coordenada y na representação latente de destino onde a origem será posicionada, permitindo um posicionamento preciso da sobreposição. |
| `resize_source` | `BOOLEAN` | Um sinalizador booleano que indica se a representação latente de origem deve ser redimensionada para corresponder às dimensões do destino antes da composição. |
| `mask` | `MASK`     | Uma máscara opcional que pode ser usada para controlar a mesclagem da origem sobre o destino. A máscara define quais partes da origem ficarão visíveis na composição final. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | A representação latente resultante após compor a origem sobre o destino, potencialmente usando uma máscara para mesclagem seletiva. |
