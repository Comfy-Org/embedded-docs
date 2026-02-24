> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskComposite/pt-BR.md)

Este nó é especializado em combinar duas entradas de máscara por meio de uma variedade de operações, como adição, subtração e operações lógicas, para produzir uma nova máscara modificada. Ele lida de forma abstrata com a manipulação de dados de máscara para alcançar efeitos de mascaramento complexos, servindo como um componente crucial em fluxos de trabalho de edição e processamento de imagem baseados em máscaras.

## Entradas

| Parâmetro    | Tipo de Dados | Descrição                                                                                                                                      |
| ------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `destination`| MASK        | A máscara primária que será modificada com base na operação com a máscara de origem. Ela desempenha um papel central na operação de composição, atuando como base para as modificações. |
| `source`     | MASK        | A máscara secundária que será usada em conjunto com a máscara de destino para executar a operação especificada, influenciando a máscara de saída final. |
| `x`          | INT         | O deslocamento horizontal no qual a máscara de origem será aplicada à máscara de destino, afetando o posicionamento do resultado da composição.       |
| `y`          | INT         | O deslocamento vertical no qual a máscara de origem será aplicada à máscara de destino, afetando o posicionamento do resultado da composição.         |
| `operation`  | COMBO[STRING]| Especifica o tipo de operação a ser aplicada entre as máscaras de destino e origem, como 'add', 'subtract' ou operações lógicas, determinando a natureza do efeito de composição. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição                                                                 |
| --------- | ------------ | ---------------------------------------------------------------------------- |
| `mask`    | MASK        | A máscara resultante após aplicar a operação especificada entre as máscaras de destino e origem, representando o resultado da composição. |
