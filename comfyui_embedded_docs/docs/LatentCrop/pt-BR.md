O nó **LatentCrop** foi projetado para realizar operações de corte em representações latentes de imagens. Ele permite especificar as dimensões e a posição do corte, possibilitando modificações direcionadas no espaço latente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `amostras` | O parâmetro `amostras` representa as representações latentes a serem cortadas. É essencial para definir os dados sobre os quais a operação de corte será realizada. | `LATENT` |
| `largura` | Especifica a largura da área de corte. Influencia diretamente as dimensões da representação latente de saída. | `INT` |
| `altura` | Especifica a altura da área de corte, afetando o tamanho da representação latente resultante após o corte. | `INT` |
| `x` | Determina a coordenada x inicial da área de corte, influenciando a posição do corte dentro da representação latente original. | `INT` |
| `y` | Determina a coordenada y inicial da área de corte, definindo a posição do corte dentro da representação latente original. | `INT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `latent` | A saída é uma representação latente modificada com o corte especificado aplicado. | `LATENT` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCrop/pt-BR.md)
