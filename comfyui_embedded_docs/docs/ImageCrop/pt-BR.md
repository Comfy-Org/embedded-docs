> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCrop/pt-BR.md)

O nó `ImageCrop` é projetado para recortar imagens para uma largura e altura especificadas, começando de uma coordenada x e y fornecida. Essa funcionalidade é essencial para focar em regiões específicas de uma imagem ou para ajustar o tamanho da imagem para atender a certos requisitos.

## Entradas

| Campo | Tipo de Dados | Descrição |
|-------|-------------|-----------|
| `image` | `IMAGE` | A imagem de entrada a ser recortada. Este parâmetro é crucial, pois define a imagem de origem da qual uma região será extraída com base nas dimensões e coordenadas especificadas. |
| `width` | `INT` | Especifica a largura da imagem recortada. Este parâmetro determina a largura da imagem recortada resultante. |
| `height` | `INT` | Especifica a altura da imagem recortada. Este parâmetro determina a altura da imagem recortada resultante. |
| `x` | `INT` | A coordenada x do canto superior esquerdo da área de recorte. Este parâmetro define o ponto de partida para a dimensão de largura do recorte. |
| `y` | `INT` | A coordenada y do canto superior esquerdo da área de recorte. Este parâmetro define o ponto de partida para a dimensão de altura do recorte. |

## Saídas

| Campo | Tipo de Dados | Descrição |
|-------|-------------|-----------|
| `image` | `IMAGE` | A imagem recortada como resultado da operação de recorte. Esta saída é significativa para processamento ou análise posterior da região de imagem especificada. |
