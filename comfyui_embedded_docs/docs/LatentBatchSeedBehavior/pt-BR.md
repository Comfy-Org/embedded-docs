O nó **LatentBatchSeedBehavior** é projetado para modificar o comportamento da semente (*seed*) em um lote de amostras latentes. Ele permite aleatorizar ou fixar a semente em todo o lote, influenciando o processo de geração ao introduzir variabilidade ou manter consistência nos resultados gerados.

## Entradas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `amostras` | O parâmetro 'samples' representa o lote de amostras latentes a ser processado. Sua modificação depende do comportamento da semente escolhido, afetando a consistência ou variabilidade dos resultados gerados. | `LATENT` |
| `comportamento_da_semente` | O parâmetro 'seed_behavior' determina se a semente para o lote de amostras latentes deve ser aleatorizada ou fixa. Essa escolha impacta significativamente o processo de geração, seja introduzindo variabilidade ou garantindo consistência em todo o lote. | COMBO[STRING] |

## Saídas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `latent` | A saída é uma versão modificada das amostras latentes de entrada, com ajustes baseados no comportamento da semente especificado. Ela mantém ou altera o índice do lote para refletir o comportamento da semente escolhido. | `LATENT` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBatchSeedBehavior/pt-BR.md)
