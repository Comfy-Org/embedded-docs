> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RebatchLatents/pt-BR.md)

O nó RebatchLatents é projetado para reorganizar um lote de representações latentes em uma nova configuração de lote, com base em um tamanho de lote especificado. Ele garante que as amostras latentes sejam agrupadas adequadamente, lidando com variações nas dimensões e tamanhos, para facilitar o processamento subsequente ou a inferência do modelo.

## Entradas

| Parâmetro    | Tipo de Dado | Descrição |
|--------------|-------------|-------------|
| `latents`    | `LATENT`    | O parâmetro 'latents' representa as representações latentes de entrada a serem reagrupadas. É crucial para determinar a estrutura e o conteúdo do lote de saída. |
| `batch_size` | `INT`      | O parâmetro 'batch_size' especifica o número desejado de amostras por lote na saída. Ele influencia diretamente o agrupamento e a divisão dos latentes de entrada em novos lotes. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | A saída é um lote reorganizado de representações latentes, ajustado de acordo com o tamanho de lote especificado. Facilita o processamento ou análise subsequente. |
