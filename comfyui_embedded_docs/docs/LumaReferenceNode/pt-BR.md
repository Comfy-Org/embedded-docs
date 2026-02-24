> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaReferenceNode/pt-BR.md)

Este nó mantém uma imagem e um valor de peso para uso com o nó Luma Generate Image. Ele cria uma cadeia de referência que pode ser passada para outros nós Luma para influenciar a geração de imagens. O nó pode iniciar uma nova cadeia de referência ou adicionar a uma existente.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | Imagem a ser usada como referência. |
| `weight` | FLOAT | Sim | 0.0 - 1.0 | Peso da referência de imagem (padrão: 1.0). |
| `luma_ref` | LUMA_REF | Não | - | Cadeia de referência Luma existente opcional à qual adicionar. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `luma_ref` | LUMA_REF | A cadeia de referência Luma contendo a imagem e o peso. |
