O nó **CropMask** foi projetado para recortar uma área específica de uma máscara fornecida. Ele permite que os usuários definam a região de interesse especificando coordenadas e dimensões, extraindo efetivamente uma parte da máscara para processamento ou análise posterior.

## Entradas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `mask` | A entrada `mask` representa a imagem da máscara a ser recortada. É essencial para definir a área a ser extraída com base nas coordenadas e dimensões especificadas. | MASK |
| `x` | A coordenada `x` especifica o ponto inicial no eixo horizontal a partir do qual o recorte deve começar. | INT |
| `y` | A coordenada `y` determina o ponto inicial no eixo vertical para a operação de recorte. | INT |
| `largura` | A `largura` (largura) define a extensão horizontal da área de recorte a partir do ponto inicial. | INT |
| `altura` | A `altura` (altura) especifica a extensão vertical da área de recorte a partir do ponto inicial. | INT |

## Saídas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `mask` | A saída é uma máscara recortada, que é uma porção da máscara original definida pelas coordenadas e dimensões especificadas. | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CropMask/pt-BR.md)
