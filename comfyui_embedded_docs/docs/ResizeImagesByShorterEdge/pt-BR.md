> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByShorterEdge/pt-BR.md)

Este nó redimensiona imagens de forma que a borda mais curta corresponda a um comprimento especificado, preservando a proporção original. Ele calcula novas dimensões com base no comprimento alvo para o lado menor e retorna a imagem redimensionada.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser redimensionada. |
| `borda_menor` | INT | Não | 1 a 8192 | Comprimento alvo para a borda mais curta. (padrão: 512) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `image` | IMAGE | A imagem redimensionada com a borda mais curta correspondendo ao comprimento alvo especificado. |

---
**Source fingerprint (SHA-256):** `011949390faa9032587aec210d9e38d55b79e474c7a6dcd5d3c0e75594a1fc29`
