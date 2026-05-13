> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageDeduplication/pt-BR.md)

Este nó remove imagens duplicadas ou muito semelhantes de um lote. Ele funciona criando um hash perceptual para cada imagem — uma impressão digital numérica simples baseada em seu conteúdo visual — e então as compara. Imagens cujos hashes são mais semelhantes do que um limite definido são consideradas duplicatas e filtradas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `images` | IMAGE | Sim | - | O lote de imagens a ser processado para deduplicação. |
| `similarity_threshold` | FLOAT | Não | 0.0 - 1.0 | Limite de similaridade (0-1). Quanto maior, mais semelhante. Imagens acima deste limite são consideradas duplicatas. (padrão: 0.95) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `images` | IMAGE | A lista filtrada de imagens com duplicatas removidas. |

---
**Source fingerprint (SHA-256):** `8904f9dee4ca911821e76d2317983cbc230c4821a9ee7876180bd7dbe42b9a54`
