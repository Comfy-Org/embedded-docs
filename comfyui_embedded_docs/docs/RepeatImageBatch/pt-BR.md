> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RepeatImageBatch/pt-BR.md)

O nó RepeatImageBatch foi projetado para replicar uma determinada imagem um número especificado de vezes, criando um lote de imagens idênticas. Essa funcionalidade é útil para operações que exigem múltiplas instâncias da mesma imagem, como processamento em lote ou aumento de dados.

## Entradas

| Campo   | Tipo de Dados | Descrição                                                                 |
|---------|---------------|---------------------------------------------------------------------------|
| `image` | `IMAGE`       | O parâmetro `image` representa a imagem a ser replicada. É crucial para definir o conteúdo que será duplicado no lote. |
| `amount`| `INT`         | O parâmetro `amount` especifica o número de vezes que a imagem de entrada deve ser replicada. Ele influencia diretamente o tamanho do lote de saída, permitindo uma criação flexível do lote. |

## Saídas

| Campo  | Tipo de Dados | Descrição                                                              |
|--------|---------------|------------------------------------------------------------------------|
| `image`| `IMAGE`       | A saída é um lote de imagens, cada uma idêntica à imagem de entrada, replicada de acordo com o `amount` especificado. |
