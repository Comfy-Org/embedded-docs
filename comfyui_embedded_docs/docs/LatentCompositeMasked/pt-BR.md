O nó LatentCompositeMasked foi projetado para combinar duas representações latentes em coordenadas específicas, utilizando opcionalmente uma máscara para uma composição mais controlada. Este nó permite a criação de imagens latentes complexas sobrepondo partes de uma imagem sobre outra, com a capacidade de redimensionar a imagem de origem para um encaixe perfeito.

## Entradas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `destino` | A representação latente sobre a qual outra representação latente será composta. Atua como a camada base para a operação de composição. | `LATENT` |
| `origem` | A representação latente a ser composta sobre o destino. Esta camada de origem pode ser redimensionada e posicionada de acordo com os parâmetros especificados. | `LATENT` |
| `x` | A coordenada x na representação latente de destino onde a origem será posicionada. Permite o posicionamento preciso da camada de origem. | `INT` |
| `y` | A coordenada y na representação latente de destino onde a origem será posicionada, permitindo um posicionamento preciso da sobreposição. | `INT` |
| `redimensionar_origem` | Um indicador booleano que determina se a representação latente de origem deve ser redimensionada para corresponder às dimensões do destino antes da composição. | `BOOLEAN` |
| `máscara` | Uma máscara opcional que pode ser usada para controlar a mesclagem da origem sobre o destino. A máscara define quais partes da origem ficarão visíveis na composição final. | `MASK` |

## Saídas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `latent` | A representação latente resultante após a composição da origem sobre o destino, potencialmente utilizando uma máscara para mesclagem seletiva. | `LATENT` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCompositeMasked/pt-BR.md)
