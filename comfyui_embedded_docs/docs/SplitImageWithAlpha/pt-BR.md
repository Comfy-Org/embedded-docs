O nó **SplitImageWithAlpha** foi projetado para separar os componentes de cor e alfa de uma imagem. Ele processa um tensor de imagem de entrada, extraindo os canais RGB como o componente de cor e o canal alfa como o componente de transparência, facilitando operações que exigem manipulação desses aspectos distintos da imagem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `imagem` | O parâmetro 'image' representa o tensor da imagem de entrada do qual os canais RGB e alfa serão separados. Ele é essencial para a operação, pois fornece os dados de origem para a divisão. | `IMAGE` |

## Saídas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `imagem` | A saída 'image' representa os canais RGB separados da imagem de entrada, fornecendo o componente de cor sem as informações de transparência. | `IMAGE` |
| `mask` | A saída 'mask' representa o canal alfa separado da imagem de entrada, fornecendo as informações de transparência. | `MASK` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageWithAlpha/pt-BR.md)
