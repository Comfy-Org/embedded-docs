O nó **PorterDuffImageComposite** é projetado para realizar composição de imagens usando os operadores de composição Porter-Duff. Ele permite a combinação de imagens de origem e destino de acordo com vários modos de mesclagem, possibilitando a criação de efeitos visuais complexos ao manipular a transparência da imagem e sobrepor imagens de maneiras criativas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `source` | O tensor da imagem de origem a ser composta sobre a imagem de destino. Ele desempenha um papel crucial na determinação do resultado visual final com base no modo de composição selecionado. | `IMAGE` |
| `source_alpha` | O canal alfa da imagem de origem, que especifica a transparência de cada pixel na imagem de origem. Ele afeta como a imagem de origem se mescla com a imagem de destino. | `MASK` |
| `destination` | O tensor da imagem de destino que serve como fundo sobre o qual a imagem de origem é composta. Ele contribui para a imagem final composta com base no modo de mesclagem. | `IMAGE` |
| `destination_alpha` | O canal alfa da imagem de destino, definindo a transparência dos pixels da imagem de destino. Ele influencia a mesclagem das imagens de origem e destino. | `MASK` |
| `mode` | O modo de composição Porter-Duff a ser aplicado, que determina como as imagens de origem e destino são mescladas. Cada modo cria efeitos visuais diferentes. | COMBO[STRING] |

## Saídas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `image` | A imagem composta resultante da aplicação do modo Porter-Duff especificado. | `IMAGE` |
| `mask` | O canal alfa da imagem composta, indicando a transparência de cada pixel. | `MASK` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PorterDuffImageComposite/pt-BR.md)
