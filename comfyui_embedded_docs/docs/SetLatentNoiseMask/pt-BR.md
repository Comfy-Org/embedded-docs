> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetLatentNoiseMask/pt-BR.md)

Este nó é projetado para aplicar uma máscara de ruído a um conjunto de amostras latentes. Ele modifica as amostras de entrada integrando uma máscara especificada, alterando assim suas características de ruído.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | As amostras latentes às quais a máscara de ruído será aplicada. Este parâmetro é crucial para determinar o conteúdo base que será modificado. |
| `mask`    | `MASK`      | A máscara a ser aplicada às amostras latentes. Ela define as áreas e a intensidade da alteração de ruído dentro das amostras. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | As amostras latentes modificadas com a máscara de ruído aplicada. |
