> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CropMask/pt-BR.md)

O nó CropMask é projetado para recortar uma área específica de uma máscara fornecida. Ele permite que os usuários definam a região de interesse especificando coordenadas e dimensões, extraindo efetivamente uma porção da máscara para processamento ou análise posterior.

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `mask`    | MASK        | A entrada `mask` representa a imagem de máscara a ser recortada. É essencial para definir a área a ser extraída com base nas coordenadas e dimensões especificadas. |
| `x`       | INT         | A coordenada `x` especifica o ponto de partida no eixo horizontal a partir do qual o recorte deve começar. |
| `y`       | INT         | A coordenada `y` determina o ponto de partida no eixo vertical para a operação de recorte. |
| `width`   | INT         | A largura (`width`) define a extensão horizontal da área de recorte a partir do ponto inicial. |
| `height`  | INT         | A altura (`height`) especifica a extensão vertical da área de recorte a partir do ponto inicial. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `mask`    | MASK        | A saída é uma máscara recortada, que é uma porção da máscara original definida pelas coordenadas e dimensões especificadas. |
