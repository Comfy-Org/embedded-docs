# Definir Máscara de Ruído Latent

Este nó é projetado para aplicar uma máscara de ruído a um conjunto de amostras latentes. Ele modifica as amostras de entrada integrando uma máscara específica, alterando assim suas características de ruído.

## Entradas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `amostras` | As amostras latentes às quais a máscara de ruído será aplicada. Este parâmetro é crucial para determinar o conteúdo base que será modificado. | `LATENT` |
| `mask` | A máscara a ser aplicada às amostras latentes. Ela define as áreas e a intensidade da alteração de ruído dentro das amostras. | `MASK` |

## Saídas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `latent` | As amostras latentes modificadas com a máscara de ruído aplicada. | `LATENT` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetLatentNoiseMask/pt-BR.md)
