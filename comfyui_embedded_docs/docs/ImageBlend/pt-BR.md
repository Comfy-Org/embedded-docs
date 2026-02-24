> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBlend/pt-BR.md)

O nó `ImageBlend` é projetado para mesclar duas imagens com base em um modo de mesclagem e um fator de mesclagem especificados. Ele suporta vários modos de mesclagem, como normal, multiplicar, tela, sobreposição, luz suave e diferença, permitindo técnicas versáteis de manipulação e composição de imagens. Este nó é essencial para criar imagens compostas ajustando a interação visual entre duas camadas de imagem.

## Entradas

| Campo         | Tipo de Dados | Descrição                                                                       |
|---------------|-------------|-----------------------------------------------------------------------------------|
| `image1`      | `IMAGE`     | A primeira imagem a ser mesclada. Serve como a camada base para a operação de mesclagem. |
| `image2`      | `IMAGE`     | A segunda imagem a ser mesclada. Dependendo do modo de mesclagem, ela modifica a aparência da primeira imagem. |
| `blend_factor`| `FLOAT`     | Determina o peso da segunda imagem na mesclagem. Um fator de mesclagem mais alto dá mais destaque à segunda imagem no resultado final. |
| `blend_mode`  | COMBO[STRING] | Especifica o método de mesclagem das duas imagens. Suporta modos como normal, multiplicar, tela, sobreposição, luz suave e diferença, cada um produzindo um efeito visual único. |

## Saídas

| Campo | Tipo de Dados | Descrição                                                              |
|-------|-------------|--------------------------------------------------------------------------|
| `image`| `IMAGE`     | A imagem resultante após a mesclagem das duas imagens de entrada de acordo com o modo e fator de mesclagem especificados. |
