> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentFlip/pt-BR.md)

O nó LatentFlip foi projetado para manipular representações latentes, invertendo-as vertical ou horizontalmente. Esta operação permite a transformação do espaço latente, potencialmente revelando novas variações ou perspectivas dentro dos dados.

## Entradas

| Parâmetro     | Tipo de Dado | Descrição |
|---------------|--------------|-------------|
| `amostras`     | `LATENT`     | O parâmetro 'samples' representa as representações latentes a serem invertidas. A operação de inversão altera essas representações, vertical ou horizontalmente, dependendo do parâmetro 'flip_method', transformando assim os dados no espaço latente. |
| `método_de_inversão` | COMBO[STRING] | O parâmetro 'flip_method' especifica o eixo ao longo do qual as amostras latentes serão invertidas. Pode ser 'x-axis: vertically' (eixo x: verticalmente) ou 'y-axis: horizontally' (eixo y: horizontalmente), determinando a direção da inversão e, portanto, a natureza da transformação aplicada às representações latentes. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|--------------|-------------|
| `latent`  | `LATENT`     | A saída é uma versão modificada das representações latentes de entrada, tendo sido invertidas de acordo com o método especificado. Esta transformação pode introduzir novas variações dentro do espaço latente. |