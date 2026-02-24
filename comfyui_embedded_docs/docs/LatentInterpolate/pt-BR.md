> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentInterpolate/pt-BR.md)

O nó LatentInterpolate é projetado para realizar a interpolação entre dois conjuntos de amostras latentes com base em uma proporção especificada, mesclando as características de ambos os conjuntos para produzir um novo conjunto intermediário de amostras latentes.

## Entradas

| Parâmetro    | Tipo de Dados | Descrição |
|--------------|-------------|-------------|
| `samples1`   | `LATENT`    | O primeiro conjunto de amostras latentes a ser interpolado. Serve como ponto de partida para o processo de interpolação. |
| `samples2`   | `LATENT`    | O segundo conjunto de amostras latentes a ser interpolado. Serve como ponto final para o processo de interpolação. |
| `ratio`      | `FLOAT`     | Um valor de ponto flutuante que determina o peso de cada conjunto de amostras na saída interpolada. Uma proporção de 0 produz uma cópia do primeiro conjunto, enquanto uma proporção de 1 produz uma cópia do segundo conjunto. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | A saída é um novo conjunto de amostras latentes que representa um estado interpolado entre os dois conjuntos de entrada, com base na proporção especificada. |
