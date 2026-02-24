> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeAndPadImage/pt-BR.md)

O nó ResizeAndPadImage redimensiona uma imagem para caber dentro de dimensões especificadas, mantendo sua proporção original. Ele reduz a imagem proporcionalmente para que caiba dentro da largura e altura alvo e, em seguida, adiciona preenchimento (padding) nas bordas para preencher qualquer espaço restante. A cor do preenchimento e o método de interpolação podem ser personalizados para controlar a aparência das áreas preenchidas e a qualidade do redimensionamento.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser redimensionada e preenchida |
| `target_width` | INT | Sim | 1 a MAX_RESOLUTION | A largura desejada para a imagem de saída (padrão: 512) |
| `target_height` | INT | Sim | 1 a MAX_RESOLUTION | A altura desejada para a imagem de saída (padrão: 512) |
| `padding_color` | COMBO | Sim | "white"<br>"black" | A cor a ser usada para as áreas de preenchimento ao redor da imagem redimensionada |
| `interpolation` | COMBO | Sim | "area"<br>"bicubic"<br>"nearest-exact"<br>"bilinear"<br>"lanczos" | O método de interpolação usado para redimensionar a imagem |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem de saída redimensionada e com preenchimento |
