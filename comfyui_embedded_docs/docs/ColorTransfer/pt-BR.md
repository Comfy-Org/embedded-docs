O nó ColorTransfer ajusta a paleta de cores de uma imagem alvo para corresponder às cores de uma imagem de referência. Ele utiliza diferentes algoritmos matemáticos para analisar e transferir as características de cor, como brilho, contraste e distribuição de matiz, da referência para o alvo. Isso é útil para criar consistência visual entre múltiplas imagens ou aplicar uma gradação de cor específica.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `image_target` | Imagem(ns) na(s) qual(is) aplicar a transformação de cor. | IMAGE | Sim | - |
| `image_ref` | Imagem(ns) de referência para corresponder as cores. | IMAGE | Sim | - |
| `method` | O algoritmo de transferência de cor a ser utilizado. | COMBO | Sim | `"reinhard_lab"`<br>`"mkl_lab"`<br>`"histogram"` |
| `source_stats` | Determina como as estatísticas de cor são calculadas a partir da(s) imagem(ns) de origem (alvo). | DYNAMICCOMBO | Sim | `"per_frame"`<br>`"uniform"`<br>`"target_frame"` |
| `strength` | A intensidade do efeito de transferência de cor. Um valor de 1.0 aplica a transformação completa, enquanto 0.0 retorna a imagem original. Padrão: 1.0 | FLOAT | Sim | 0.0 a 10.0 |

**Detalhes dos Parâmetros:**
*   **Opções de `source_stats`:**
    *   **`per_frame`**: Cada quadro em um lote é correspondido ao `image_ref` individualmente.
    *   **`uniform`**: As estatísticas de cor são agrupadas em todos os quadros de origem para criar uma única linha de base, que é então correspondida ao `image_ref`.
    *   **`target_frame`**: Utiliza um quadro escolhido do lote alvo como linha de base para calcular a transformação para o `image_ref`. Essa transformação é então aplicada uniformemente a todos os quadros, o que preserva as diferenças relativas de cor entre eles. Quando esta opção é selecionada, um parâmetro adicional `target_index` fica disponível.
*   **`target_index`** (aparece quando `source_stats` é `"target_frame"`): O índice do quadro (começando em 0) usado como linha de base de origem para calcular a transformação. Padrão: 0. Deve estar entre 0 e 10000.

**Restrições:**
*   Se `strength` for definido como 0.0 ou `image_ref` for `None`, o nó retorna o `image_target` original sem processamento.
*   Quando `source_stats` é definido como `"target_frame"`, o `target_index` deve ser um índice válido dentro do lote de `image_target`. Se exceder o número de quadros, o último quadro é utilizado.
*   Para o método `histogram` com `source_stats` definido como `"per_frame"`, se o tamanho do lote de `image_ref` for maior que 1, cada quadro alvo é correspondido ao quadro de referência correspondente pelo índice. Se o lote de referência tiver apenas um quadro, ele é utilizado para todos os quadros alvo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `image` | A(s) imagem(ns) resultante(s) após a transferência de cor ter sido aplicada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorTransfer/pt-BR.md)

---
**Source fingerprint (SHA-256):** `93a8447def4d2263a8a859c0474de694e6567dc6d32377032c2ddae2420bb10c`
