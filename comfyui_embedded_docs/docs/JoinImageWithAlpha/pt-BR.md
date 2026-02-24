> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JoinImageWithAlpha/pt-BR.md)

Este nó é projetado para operações de composição, especificamente para unir uma imagem com sua máscara alfa correspondente e produzir uma única imagem de saída. Ele combina efetivamente o conteúdo visual com informações de transparência, permitindo a criação de imagens onde certas áreas são transparentes ou semitransparentes.

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | O conteúdo visual principal a ser combinado com uma máscara alfa. Representa a imagem sem informações de transparência. |
| `alpha`   | `MASK`      | A máscara alfa que define a transparência da imagem correspondente. É usada para determinar quais partes da imagem devem ser transparentes ou semitransparentes. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | A saída é uma única imagem que combina a imagem de entrada com a máscara alfa, incorporando as informações de transparência ao conteúdo visual. |
