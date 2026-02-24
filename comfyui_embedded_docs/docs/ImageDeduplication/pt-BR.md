> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageDeduplication/pt-BR.md)

Este nó remove imagens duplicadas ou muito similares de um lote. Ele funciona criando um hash perceptual para cada imagem — uma impressão digital numérica simples baseada em seu conteúdo visual — e então comparando-os. Imagens cujos hashes são mais similares do que um limite definido são consideradas duplicadas e filtradas.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sim | - | O lote de imagens a ser processado para deduplicação. |
| `similarity_threshold` | FLOAT | Não | 0.0 - 1.0 | Limite de similaridade (0-1). Valores mais altos significam maior similaridade. Imagens acima deste limite são consideradas duplicadas. (padrão: 0.95) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `images` | IMAGE | A lista filtrada de imagens com os duplicados removidos. |
