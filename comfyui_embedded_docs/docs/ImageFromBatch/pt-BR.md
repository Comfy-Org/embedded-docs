O nó `ImageFromBatch` foi projetado para extrair um segmento específico de imagens de um lote com base no índice e comprimento fornecidos. Ele permite um controle mais granular sobre as imagens em lote, possibilitando operações em imagens individuais ou subconjuntos dentro de um lote maior.

## Entradas

| Campo | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagem` | O lote de imagens do qual um segmento será extraído. Este parâmetro é essencial para especificar o lote de origem. | `IMAGE` |
| `índice_do_lote` | O índice inicial dentro do lote a partir do qual a extração começa. Ele determina a posição inicial do segmento a ser extraído do lote. | `INT` |
| `comprimento` | O número de imagens a serem extraídas do lote a partir do `índice_do_lote`. Este parâmetro define o tamanho do segmento a ser extraído. | `INT` |

## Saídas

| Campo | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagem` | O segmento extraído de imagens do lote especificado. Esta saída representa um subconjunto do lote original, determinado pelos parâmetros `índice_do_lote` e `comprimento`. | `IMAGE` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFromBatch/pt-BR.md)
