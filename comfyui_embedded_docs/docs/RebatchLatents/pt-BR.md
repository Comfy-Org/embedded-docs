O nó RebatchLatents foi projetado para reorganizar um lote de representações latentes em uma nova configuração de lote, com base em um tamanho de lote especificado. Ele garante que as amostras latentes sejam agrupadas adequadamente, lidando com variações nas dimensões e tamanhos, para facilitar o processamento posterior ou a inferência do modelo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `latents` | O parâmetro 'latents' representa as representações latentes de entrada a serem reagrupadas. Ele é crucial para determinar a estrutura e o conteúdo do lote de saída. | `LATENT` |
| `tamanho_do_lote` | O parâmetro 'batch_size' especifica o número desejado de amostras por lote na saída. Ele influencia diretamente o agrupamento e a divisão dos latentes de entrada em novos lotes. | `INT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `latent` | A saída é um lote reorganizado de representações latentes, ajustado de acordo com o tamanho de lote especificado. Ele facilita o processamento ou a análise posteriores. | `LATENT` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RebatchLatents/pt-BR.md)
