> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByShorterEdge/pt-BR.md)

Este nó redimensiona imagens ajustando suas dimensões para que o comprimento do lado mais curto corresponda a um valor alvo especificado. Ele calcula novas dimensões para manter a proporção original da imagem. A imagem redimensionada é retornada.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser redimensionada. |
| `shorter_edge` | INT | Não | 1 a 8192 | Comprimento alvo para a borda mais curta. (padrão: 512) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem redimensionada. |
