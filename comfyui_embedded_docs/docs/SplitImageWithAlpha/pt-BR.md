> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageWithAlpha/pt-BR.md)

O nó SplitImageWithAlpha foi projetado para separar os componentes de cor e alfa de uma imagem. Ele processa um tensor de imagem de entrada, extraindo os canais RGB como componente de cor e o canal alfa como componente de transparência, facilitando operações que requerem manipulação desses aspectos distintos da imagem.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | O parâmetro `image` representa o tensor de imagem de entrada a partir do qual os canais RGB e alfa serão separados. É crucial para a operação, pois fornece os dados de origem para a divisão. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | A saída `image` representa os canais RGB separados da imagem de entrada, fornecendo o componente de cor sem as informações de transparência. |
| `mask`    | `MASK`      | A saída `mask` representa o canal alfa separado da imagem de entrada, fornecendo as informações de transparência. |
