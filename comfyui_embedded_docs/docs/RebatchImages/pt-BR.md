> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RebatchImages/pt-BR.md)

O nó RebatchImages é projetado para reorganizar um lote de imagens em uma nova configuração de lote, ajustando o tamanho do lote conforme especificado. Este processo é essencial para gerenciar e otimizar o processamento de dados de imagem em operações em lote, garantindo que as imagens sejam agrupadas de acordo com o tamanho de lote desejado para um manuseio eficiente.

## Entradas

| Campo       | Tipo de Dados | Descrição                                                                         |
|-------------|-------------|-------------------------------------------------------------------------------------|
| `images`    | `IMAGE`     | Uma lista de imagens a serem reagrupadas em lotes. Este parâmetro é crucial para determinar os dados de entrada que passarão pelo processo de reagrupamento. |
| `batch_size`| `INT`       | Especifica o tamanho desejado dos lotes de saída. Este parâmetro influencia diretamente como as imagens de entrada são agrupadas e processadas, impactando a estrutura da saída. |

## Saídas

| Campo | Tipo de Dados | Descrição                                                                   |
|-------|-------------|-------------------------------------------------------------------------------|
| `image`| `IMAGE`     | A saída consiste em uma lista de lotes de imagens, reorganizados de acordo com o tamanho de lote especificado. Isso permite um processamento flexível e eficiente dos dados de imagem em operações em lote. |
