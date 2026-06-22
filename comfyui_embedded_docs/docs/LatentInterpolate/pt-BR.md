# Interpolar Latent

O nó LatentInterpolate foi projetado para realizar interpolação entre dois conjuntos de amostras latentes com base em uma proporção especificada, combinando as características de ambos os conjuntos para produzir um novo conjunto intermediário de amostras latentes.

## Entradas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `amostras1` | O primeiro conjunto de amostras latentes a ser interpolado. Serve como ponto de partida para o processo de interpolação. | `LATENT` |
| `amostras2` | O segundo conjunto de amostras latentes a ser interpolado. Serve como ponto final para o processo de interpolação. | `LATENT` |
| `proporção` | Um valor de ponto flutuante que determina o peso de cada conjunto de amostras na saída interpolada. Uma proporção de 0 produz uma cópia do primeiro conjunto, enquanto uma proporção de 1 produz uma cópia do segundo conjunto. | `FLOAT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `latent` | A saída é um novo conjunto de amostras latentes que representa um estado interpolado entre os dois conjuntos de entrada, com base na proporção especificada. | `LATENT` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentInterpolate/pt-BR.md)
