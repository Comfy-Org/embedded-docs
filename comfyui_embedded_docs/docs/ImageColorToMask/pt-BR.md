> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorToMask/pt-BR.md)

O nó `ImageColorToMask` é projetado para converter uma cor específica em uma imagem em uma máscara. Ele processa uma imagem e uma cor alvo, gerando uma máscara onde a cor especificada é destacada, facilitando operações como segmentação baseada em cor ou isolamento de objetos.

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | O parâmetro `image` representa a imagem de entrada a ser processada. É crucial para determinar as áreas da imagem que correspondem à cor especificada para serem convertidas em uma máscara. |
| `color`   | `INT`       | O parâmetro `color` especifica a cor alvo na imagem a ser convertida em uma máscara. Ele desempenha um papel fundamental na identificação das áreas de cor específicas a serem destacadas na máscara resultante. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `mask`    | `MASK`      | A saída é uma máscara que destaca as áreas da imagem de entrada que correspondem à cor especificada. Esta máscara pode ser usada para tarefas posteriores de processamento de imagem, como segmentação ou isolamento de objetos. |
