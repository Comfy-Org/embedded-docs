> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextImageScale/pt-BR.md)

Este nó redimensiona a imagem de entrada para um tamanho ideal utilizado durante o treinamento do modelo Flux Kontext usando o algoritmo Lanczos, com base na proporção de aspecto da imagem de entrada. Este nó é particularmente útil ao inserir imagens de grande tamanho, pois entradas excessivamente grandes podem levar à degradação da qualidade da saída do modelo ou a problemas como a aparição de múltiplos sujeitos na saída.

## Entradas

| Nome do Parâmetro | Tipo de Dados | Tipo de Entrada | Valor Padrão | Faixa de Valores | Descrição |
|----------------|-----------|------------|---------------|-------------|-------------|
| `image` | IMAGE | Obrigatório | - | - | Imagem de entrada a ser redimensionada |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | Imagem redimensionada |

## Lista de Tamanhos Predefinidos

A seguir está uma lista dos tamanhos padrão utilizados durante o treinamento do modelo. O nó selecionará o tamanho mais próximo da proporção de aspecto da imagem de entrada:

| Largura | Altura | Proporção de Aspecto |
|-------|--------|--------------|
| 672   | 1568   | 0.429       |
| 688   | 1504   | 0.457       |
| 720   | 1456   | 0.494       |
| 752   | 1392   | 0.540       |
| 800   | 1328   | 0.603       |
| 832   | 1248   | 0.667       |
| 880   | 1184   | 0.743       |
| 944   | 1104   | 0.855       |
| 1024  | 1024   | 1.000       |
| 1104  | 944    | 1.170       |
| 1184  | 880    | 1.345       |
| 1248  | 832    | 1.500       |
| 1328  | 800    | 1.660       |
| 1392  | 752    | 1.851       |
| 1456  | 720    | 2.022       |
| 1504  | 688    | 2.186       |
| 1568  | 672    | 2.333       |
