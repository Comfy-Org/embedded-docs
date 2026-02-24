> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBatchSeedBehavior/pt-BR.md)

O nó LatentBatchSeedBehavior foi projetado para modificar o comportamento da semente (seed) de um lote de amostras latentes. Ele permite randomizar ou fixar a semente ao longo do lote, influenciando assim o processo de geração ao introduzir variabilidade ou manter consistência nas saídas geradas.

## Entradas

| Parâmetro       | Tipo de Dados | Descrição |
|-----------------|--------------|-------------|
| `samples`       | `LATENT`     | O parâmetro 'samples' representa o lote de amostras latentes a ser processado. Sua modificação depende do comportamento de semente escolhido, afetando a consistência ou a variabilidade das saídas geradas. |
| `seed_behavior`  | COMBO[STRING] | O parâmetro 'seed_behavior' determina se a semente para o lote de amostras latentes deve ser randomizada ou fixada. Essa escolha impacta significativamente o processo de geração, seja introduzindo variabilidade ou garantindo consistência em todo o lote. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | A saída é uma versão modificada das amostras latentes de entrada, com ajustes feitos com base no comportamento de semente especificado. Ela mantém ou altera o índice do lote para refletir o comportamento de semente escolhido. |
