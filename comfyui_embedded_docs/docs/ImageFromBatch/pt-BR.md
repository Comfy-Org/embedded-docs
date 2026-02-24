> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFromBatch/pt-BR.md)

O nó `ImageFromBatch` é projetado para extrair um segmento específico de imagens de um lote com base no índice e comprimento fornecidos. Ele permite um controle mais granular sobre as imagens em lote, possibilitando operações em imagens individuais ou subconjuntos dentro de um lote maior.

## Entradas

| Campo          | Tipo de Dados | Descrição                                                                           |
|----------------|-------------|---------------------------------------------------------------------------------------|
| `image`        | `IMAGE`     | O lote de imagens do qual um segmento será extraído. Este parâmetro é crucial para especificar o lote de origem. |
| `batch_index`  | `INT`       | O índice inicial dentro do lote a partir do qual a extração começa. Ele determina a posição inicial do segmento a ser extraído do lote. |
| `length`       | `INT`       | O número de imagens a extrair do lote, começando a partir do `batch_index`. Este parâmetro define o tamanho do segmento a ser extraído. |

## Saídas

| Campo | Tipo de Dados | Descrição                                                                                   |
|-------|-------------|-----------------------------------------------------------------------------------------------|
| `image` | `IMAGE`    | O segmento de imagens extraído do lote especificado. Esta saída representa um subconjunto do lote original, determinado pelos parâmetros `batch_index` e `length`. |
