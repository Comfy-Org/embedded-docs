O nó `ImageBlend` foi projetado para mesclar duas imagens com base em um modo de mesclagem e um fator de mesclagem especificados. Ele suporta vários modos de mesclagem, como normal, multiplicar, tela, sobreposição, luz suave e diferença, permitindo técnicas versáteis de manipulação e composição de imagens. Este nó é essencial para criar imagens compostas ao ajustar a interação visual entre duas camadas de imagem.

## Entradas

| Campo | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagem1` | A primeira imagem a ser mesclada. Ela serve como camada base para a operação de mesclagem. | `IMAGE` |
| `imagem2` | A segunda imagem a ser mesclada. Dependendo do modo de mesclagem, ela modifica a aparência da primeira imagem. | `IMAGE` |
| `fator_de_mistura` | Determina o peso da segunda imagem na mesclagem. Um fator de mesclagem maior dá mais destaque à segunda imagem no resultado final. | `FLOAT` |
| `modo_de_mistura` | Especifica o método de mesclagem das duas imagens. Suporta modos como normal, multiplicar, tela, sobreposição, luz suave e diferença, cada um produzindo um efeito visual único. | COMBO[STRING] |

## Saídas

| Campo | Descrição | Tipo de Dado |
| --- | --- | --- |
| `image` | A imagem resultante após mesclar as duas imagens de entrada de acordo com o modo e o fator de mesclagem especificados. | `IMAGE` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBlend/pt-BR.md)
