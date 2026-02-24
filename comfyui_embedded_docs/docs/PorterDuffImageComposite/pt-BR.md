> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PorterDuffImageComposite/pt-BR.md)

O nó PorterDuffImageComposite é projetado para realizar a composição de imagens usando os operadores de composição Porter-Duff. Ele permite a combinação de imagens de origem e destino de acordo com vários modos de mesclagem, possibilitando a criação de efeitos visuais complexos através da manipulação da transparência da imagem e da sobreposição de imagens de maneiras criativas.

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
| --------- | ------------ | ----------- |
| `source`  | `IMAGE`     | O tensor da imagem de origem a ser composto sobre a imagem de destino. Ele desempenha um papel crucial na determinação do resultado visual final com base no modo de composição selecionado. |
| `source_alpha` | `MASK` | O canal alfa da imagem de origem, que especifica a transparência de cada pixel na imagem de origem. Afeta como a imagem de origem se mistura com a imagem de destino. |
| `destination` | `IMAGE` | O tensor da imagem de destino que serve como pano de fundo sobre o qual a imagem de origem é composta. Contribui para a imagem composta final com base no modo de mesclagem. |
| `destination_alpha` | `MASK` | O canal alfa da imagem de destino, definindo a transparência dos pixels da imagem de destino. Influencia a mesclagem das imagens de origem e destino. |
| `mode` | COMBO[STRING] | O modo de composição Porter-Duff a ser aplicado, que determina como as imagens de origem e destino são mescladas. Cada modo cria efeitos visuais diferentes. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
| --------- | ------------ | ----------- |
| `image`   | `IMAGE`     | A imagem composta resultante da aplicação do modo Porter-Duff especificado. |
| `mask`    | `MASK`      | O canal alfa da imagem composta, indicando a transparência de cada pixel. |
