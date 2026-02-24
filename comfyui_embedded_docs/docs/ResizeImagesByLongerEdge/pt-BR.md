> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByLongerEdge/pt-BR.md)

O nó **Redimensionar Imagens pela Borda Mais Longa** redimensiona uma ou mais imagens para que seu lado mais longo corresponda a um comprimento alvo especificado. Ele determina automaticamente se a largura ou a altura é maior e dimensiona a outra dimensão proporcionalmente para preservar a proporção original da imagem. Isso é útil para padronizar tamanhos de imagem com base em sua maior dimensão.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada ou lote de imagens a ser redimensionado. |
| `longer_edge` | INT | Não | 1 - 8192 | Comprimento alvo para a borda mais longa. A borda mais curta será dimensionada proporcionalmente. (padrão: 1024) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem ou lote de imagens redimensionado. A saída terá o mesmo número de imagens que a entrada, com a borda mais longa de cada uma correspondendo ao comprimento `longer_edge` especificado. |
