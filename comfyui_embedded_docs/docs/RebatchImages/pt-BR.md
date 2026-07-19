# Reagrupar Imagens

O nó RebatchImages foi projetado para reorganizar um lote de imagens em uma nova configuração de lote, ajustando o tamanho do lote conforme especificado. Esse processo é essencial para gerenciar e otimizar o processamento de dados de imagem em operações em lote, garantindo que as imagens sejam agrupadas de acordo com o tamanho de lote desejado para um manuseio eficiente.

## Entradas

| Campo | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagens` | Uma lista de imagens a ser reagrupada. Este parâmetro é crucial para determinar os dados de entrada que passarão pelo processo de reagrupamento. | `IMAGE` |
| `tamanho do lote` | Especifica o tamanho desejado dos lotes de saída. Este parâmetro influencia diretamente como as imagens de entrada são agrupadas e processadas, impactando a estrutura da saída. | `INT` |

## Saídas

| Campo | Descrição | Tipo de Dado |
| --- | --- | --- |
| `image` | A saída consiste em uma lista de lotes de imagens, reorganizados de acordo com o tamanho de lote especificado. Isso permite o processamento flexível e eficiente de dados de imagem em operações em lote. | `IMAGE` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RebatchImages/pt-BR.md)
