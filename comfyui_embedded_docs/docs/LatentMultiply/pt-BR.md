# Multiplicar Latent

O nó LatentMultiply foi projetado para escalar a representação latente de amostras por um multiplicador especificado. Esta operação permite ajustar a intensidade ou magnitude das características dentro do espaço latente, possibilitando o refinamento do conteúdo gerado ou a exploração de variações em uma determinada direção latente.

## Entradas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `amostras` | O parâmetro 'samples' representa as representações latentes a serem escaladas. É crucial para definir os dados de entrada sobre os quais a operação de multiplicação será realizada. | `LATENT` |
| `multiplicador` | O parâmetro 'multiplier' especifica o fator de escala a ser aplicado às amostras latentes. Ele desempenha um papel fundamental no ajuste da magnitude das características latentes, permitindo um controle preciso sobre a saída gerada. | `FLOAT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `latent` | A saída é uma versão modificada das amostras latentes de entrada, escaladas pelo multiplicador especificado. Isso permite a exploração de variações dentro do espaço latente ao ajustar a intensidade de suas características. | `LATENT` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentMultiply/pt-BR.md)
