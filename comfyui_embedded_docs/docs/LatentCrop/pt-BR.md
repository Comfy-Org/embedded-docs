> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCrop/pt-BR.md)

O nó LatentCrop é projetado para realizar operações de recorte em representações latentes de imagens. Ele permite a especificação das dimensões e posição do recorte, possibilitando modificações direcionadas do espaço latente.

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | O parâmetro `samples` representa as representações latentes a serem recortadas. É crucial para definir os dados sobre os quais a operação de recorte será realizada. |
| `width`   | `INT`       | Especifica a largura da área de recorte. Influencia diretamente as dimensões da representação latente de saída. |
| `height`  | `INT`       | Especifica a altura da área de recorte, afetando o tamanho da representação latente recortada resultante. |
| `x`       | `INT`       | Determina a coordenada x inicial da área de recorte, influenciando a posição do recorte dentro da representação latente original. |
| `y`       | `INT`       | Determina a coordenada y inicial da área de recorte, definindo a posição do recorte dentro da representação latente original. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | A saída é uma representação latente modificada com o recorte especificado aplicado. |
