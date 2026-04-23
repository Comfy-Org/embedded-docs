> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorTransfer/pt-BR.md)

O nó ColorTransfer ajusta a paleta de cores de uma imagem alvo para corresponder às cores de uma imagem de referência. Ele utiliza diferentes algoritmos matemáticos para analisar e transferir as características cromáticas, como brilho, contraste e distribuição de matiz, da referência para o alvo. Isso é útil para criar consistência visual entre múltiplas imagens ou aplicar uma gradação de cor específica.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `image_target` | IMAGE | Sim | - | Imagem(ns) à qual aplicar a transformação de cor. |
| `image_ref` | IMAGE | Não | - | Imagem(ns) de referência para correspondência de cores. Se não for fornecida, o processamento é ignorado e a imagem alvo é retornada sem alterações. |
| `method` | COMBO | Sim | `"reinhard_lab"`<br>`"mkl_lab"`<br>`"histogram"` | O algoritmo de transferência de cor a ser utilizado. |
| `source_stats` | DYNAMICCOMBO | Sim | `"per_frame"`<br>`"uniform"`<br>`"target_frame"` | Determina como as estatísticas de cor são calculadas a partir da(s) imagem(ns) de origem (alvo). |
| `strength` | FLOAT | Sim | 0.0 a 10.0 | A intensidade do efeito de transferência de cor. Um valor de 1.0 aplica a transformação completa, enquanto 0.0 retorna a imagem original. Padrão: 1.0 |

**Detalhes dos Parâmetros:**
*   **Opções de `source_stats`:**
    *   **`per_frame`**: Cada quadro em um lote é combinado individualmente com `image_ref`.
    *   **`uniform`**: As estatísticas de cor são agrupadas em todos os quadros de origem para criar uma única linha de base, que é então combinada com `image_ref`.
    *   **`target_frame`**: Utiliza um quadro selecionado do lote alvo como linha de base para calcular a transformação para `image_ref`. Essa transformação é então aplicada uniformemente a todos os quadros, preservando as diferenças relativas de cor entre eles. Quando esta opção é selecionada, um parâmetro adicional `target_index` fica disponível.
*   **`target_index`** (aparece quando `source_stats` é `"target_frame"`): O índice do quadro (começando em 0) usado como linha de base de origem para calcular a transformação. Padrão: 0. Deve estar entre 0 e 10000.

**Restrições:**
*   Se `image_ref` não for fornecida ou `strength` estiver definido como 0.0, o nó retorna a `image_target` original sem processamento.
*   Quando `source_stats` está definido como `"target_frame"`, o `target_index` deve ser um índice válido dentro do lote de `image_target`. Se exceder o número de quadros, o último quadro é utilizado.
*   Para o método `histogram` com `source_stats` definido como `"per_frame"`, se o tamanho do lote de `image_ref` for maior que 1, cada quadro alvo é combinado com o quadro de referência correspondente pelo índice. Se o lote de referência tiver apenas um quadro, ele é usado para todos os quadros alvo.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `image` | IMAGE | A(s) imagem(ns) resultante(s) após a aplicação da transferência de cor. |